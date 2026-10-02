"""آداپتور DivarFetcher — تنها نقطهٔ تماس با دیوار (ADR-0004؛ مرحلهٔ ۳).

- search(): POST postlist/w/search با بدنهٔ ساختهشده از کانفیگ (form_data عیناً)
- get_post(): GET posts-v2/web/{token} با fallback صفحهٔ HTML (ADR-0009)
- درخواست‌ها در صورت وجود صف، از صف سریال عبور می‌کنند (AGENTS.md)
- حمل HTTP با urllib کتابخانهٔ استاندارد، در تسک جدا برای حلقهٔ رویداد (ADR-0012)
"""

import asyncio
import json

from top_divar.divar.errors import (
    DivarHTTPError,
    DivarSchemaError,
    DivarUnavailableError,
)
from top_divar.divar.models import PostDetail, SearchPage
from top_divar.divar.parsing import (
    POST_DETAIL_BASE_URL,
    POST_PAGE_BASE_URL,
    SEARCH_BASE_URL,
    parse_post_detail,
    parse_post_detail_html,
    parse_search_page,
)
from top_divar.shared.logging import get_logger

_log = get_logger("divar.fetcher")

DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64; rv:144.0) Gecko/20100101 Firefox/144.0"
)
DEFAULT_SORT = "sort_date"
DEFAULT_TIMEOUT_SECONDS = 20.0

_BASE_HEADERS = {
    "accept": "application/json, text/plain, */*",
    "referer": "https://divar.ir/",
    "user-agent": DEFAULT_USER_AGENT,
    "x-web-serving-mode": "desktop",
}

_RATE_LIMIT_STATUS_THRESHOLD = 500


class _UrllibTransport:
    """حمل HTTP با urllib؛ چون sync است از asyncio.to_thread عبور می‌کند."""

    def __init__(self, *, timeout: float = DEFAULT_TIMEOUT_SECONDS, user_agent: str):
        self._timeout = timeout
        self._user_agent = user_agent

    async def __call__(self, method: str, url: str, headers: dict, body: bytes = None):
        return await asyncio.to_thread(self._call, method, url, headers, body)

    def _call(self, method: str, url: str, headers: dict, body):
        import urllib.error
        import urllib.request

        request = urllib.request.Request(url=url, data=body, method=method)
        for name, value in headers.items():
            request.add_header(name, value)
        request.add_header("user-agent", self._user_agent)
        try:
            with urllib.request.urlopen(request, timeout=self._timeout) as response:
                return (
                    response.status,
                    {name.lower(): value for name, value in response.headers.items()},
                    response.read(),
                )
        except urllib.error.HTTPError as exc:
            body_bytes = b""
            try:
                body_bytes = exc.read()
            except Exception:  # noqa: BLE001 - بدنهٔ خطا اختیاری است
                pass
            return (
                exc.code,
                {name.lower(): value for name, value in (exc.headers or {}).items()},
                body_bytes,
            )


def build_search_body(search: dict, *, pagination_data: dict = None) -> dict:
    """بدنهٔ درخواست search از کانفیگ جستجو — form_data عیناً و بدون ترجمه (بخش ۳)."""
    body = {
        "source_view": "FILTER",
        "city_ids": list(search.get("city_ids") or ["1"]),
        "user_selected_location": {
            "places": [{"place_id": place_id} for place_id in search.get("place_ids") or []]
        },
        "search_data": {
            "form_data": {"data": search.get("form_data") or {}},
            "server_payload": {
                "additional_form_data": {
                    "data": {"sort": {"str": {"value": search.get("sort") or DEFAULT_SORT}}}
                }
            },
        },
    }
    if pagination_data is not None:
        body["pagination_data"] = pagination_data
    return body


class DivarFetcher:
    """قرارداد واکشی: search و get_post (تنها نقطهٔ تماس با دیوار)."""

    def __init__(self, *, queue=None, transport=None, user_agent: str = DEFAULT_USER_AGENT, timeout: float = DEFAULT_TIMEOUT_SECONDS):
        self._queue = queue
        self._transport = transport or _UrllibTransport(timeout=timeout, user_agent=user_agent)

    async def search(self, search: dict, *, pagination_data: dict = None) -> SearchPage:
        body = build_search_body(search, pagination_data=pagination_data)
        headers = dict(_BASE_HEADERS)
        headers["content-type"] = "application/json"
        payload = json.dumps(body, ensure_ascii=False).encode("utf-8")

        async def action():
            status, response_headers, response_body = await self._transport(
                "POST", SEARCH_BASE_URL, headers, payload
            )
            if status != 200:
                self._log_http_failure("search", SEARCH_BASE_URL, status, response_headers)
                raise DivarHTTPError(
                    f"درخواست search با وضعیت {status} رد شد.",
                    status=status,
                    url=SEARCH_BASE_URL,
                    retry_after=response_headers.get("retry-after"),
                )
            return parse_search_page(_decode_json(response_body, what="search"))

        if self._queue is None:
            return await action()
        return await self._queue.run_search(action)

    async def get_post(self, token: str) -> PostDetail:
        detail_url = f"{POST_DETAIL_BASE_URL}/{token}"
        page_url = f"{POST_PAGE_BASE_URL}/{token}"

        async def action():
            status, response_headers, response_body = await self._transport(
                "GET", detail_url, dict(_BASE_HEADERS), None
            )
            if status == 200:
                payload = _try_decode_json(response_body)
                if isinstance(payload, dict) and isinstance(payload.get("sections"), list):
                    return parse_post_detail(payload)
            elif status != 403:
                self._log_http_failure("post_detail", detail_url, status, response_headers)
                raise DivarHTTPError(
                    f"درخواست جزئیات آگهی {token} با وضعیت {status} رد شد.",
                    status=status,
                    url=detail_url,
                    retry_after=response_headers.get("retry-after"),
                )
            _log.warning(
                "جزئیات JSON برای %s در دسترس نبود (وضعیت %s) — تلاش fallback HTML.",
                token,
                status,
                extra={"fields": {"event": "post_detail_fallback", "token": token, "status": status}},
            )
            return await self._fetch_html_detail(token, page_url)

        if self._queue is None:
            return await action()
        return await self._queue.run_detail(action)

    async def _fetch_html_detail(self, token: str, page_url: str) -> PostDetail:
        headers = dict(_BASE_HEADERS)
        headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        status, response_headers, response_body = await self._transport(
            "GET", page_url, headers, None
        )
        if status != 200:
            self._log_http_failure("post_page_fallback", page_url, status, response_headers)
            raise DivarUnavailableError(
                f"fallback HTML آگهی {token} هم با وضعیت {status} رد شد."
            )
        html = response_body.decode("utf-8", errors="replace")
        try:
            detail = parse_post_detail_html(html)
        except DivarSchemaError as exc:
            raise DivarUnavailableError(
                f"fallback HTML آگهی {token} ویجت قابل پارسی نداشت: {exc}"
            ) from exc
        if not detail.raw.get("sections"):
            raise DivarUnavailableError(f"fallback HTML آگهی {token} ویجت نداشت.")
        return detail

    @staticmethod
    def _log_http_failure(what: str, url: str, status: int, headers: dict) -> None:
        fields = {"event": "divar_http_error", "what": what, "status": status}
        retry_after = headers.get("retry-after")
        if retry_after is not None:
            fields["retry_after"] = retry_after
        log = _log.error if status == 429 or status >= _RATE_LIMIT_STATUS_THRESHOLD else _log.warning
        log("درخواست دیوار رد شد: %s → وضعیت %s", url, status, extra={"fields": fields})


def _decode_json(body: bytes, *, what: str) -> dict:
    payload = _try_decode_json(body)
    if not isinstance(payload, dict):
        raise DivarSchemaError(f"پاسخ {what} آبجکت JSON نیست.")
    return payload


def _try_decode_json(body: bytes):
    try:
        return json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return None
