import asyncio
import json

import pytest

from top_divar.divar.errors import DivarHTTPError, DivarUnavailableError
from top_divar.divar.fetcher import DivarFetcher, build_search_body


class FakeTransport:
    """حمل ساختگی: پاسخ‌های از پیش تنظیم‌شده به‌ازای URL."""

    def __init__(self, routes):
        self.routes = routes
        self.calls = []

    async def __call__(self, method, url, headers, body=None):
        self.calls.append(
            {
                "method": method,
                "url": url,
                "headers": dict(headers),
                "body": json.loads(body.decode("utf-8")) if body else None,
            }
        )
        for prefix, responder in self.routes:
            if url.startswith(prefix):
                if callable(responder):
                    return responder(self.calls[-1])
                return responder
        raise AssertionError(f"مسیر تنظیم‌نشده: {url}")


def _json_response(payload, status=200):
    return (status, {}, json.dumps(payload, ensure_ascii=False).encode("utf-8"))


@pytest.fixture()
def search_config():
    return {
        "id": "test-search",
        "city_ids": ["1"],
        "place_ids": ["1"],
        "sort": "sort_date",
        "form_data": {
            "category": {"str": {"value": "apartment-sell"}},
            "districts": {"repeated_string": {"value": ["198", "399"]}},
        },
    }


class TestBuildSearchBody:
    def test_form_data_passes_through_verbatim(self, search_config):
        body = build_search_body(search_config)
        assert body["search_data"]["form_data"]["data"] == search_config["form_data"]
        assert body["source_view"] == "FILTER"
        assert body["city_ids"] == ["1"]
        assert body["user_selected_location"] == {"places": [{"place_id": "1"}]}

    def test_sort_via_server_payload_not_form_data(self, search_config):
        body = build_search_body(search_config)
        assert body["search_data"]["server_payload"]["additional_form_data"]["data"] == {
            "sort": {"str": {"value": "sort_date"}}
        }
        assert "sort" not in body["search_data"]["form_data"]["data"]

    def test_pagination_data_echoed(self, search_config):
        pagination = {"page": 1, "search_uid": "uid", "viewed_tokens": "H4sIA..."}
        body = build_search_body(search_config, pagination_data=pagination)
        assert body["pagination_data"] == pagination

    def test_no_district_injection(self, search_config):
        # برنامه هرگز شناسهٔ محله تزریق نمی‌کند (ADR-0006)
        body = build_search_body(search_config)
        assert body["search_data"]["form_data"]["data"]["districts"] == {
            "repeated_string": {"value": ["198", "399"]}
        }


class TestFetcherSearch:
    def test_search_parses_response(self, search_config):
        payload = {
            "list_widgets": [
                {
                    "widget_type": "POST_ROW",
                    "data": {
                        "title": "تست",
                        "action": {
                            "payload": {
                                "token": "tok1",
                                "web_info": {"district_persian": "پونک", "city_persian": "تهران"},
                            }
                        },
                        "middle_description_text": "۱,۰۰۰ تومان",
                        "image_count": 2,
                    },
                    "action_log": {
                        "server_side_info": {"info": {"sort_date": "2026-09-15T14:29:17Z"}}
                    },
                }
            ],
            "pagination": {"has_next_page": True, "data": {"page": 1}},
        }
        transport = FakeTransport([("https://api.divar.ir/v8/postlist/w/search", _json_response(payload))])
        fetcher = DivarFetcher(transport=transport)
        page = asyncio.run(fetcher.search(search_config))
        assert page.cards[0].token == "tok1"
        call = transport.calls[0]
        assert call["method"] == "POST"
        assert call["headers"]["content-type"] == "application/json"
        assert call["headers"]["referer"] == "https://divar.ir/"
        assert call["headers"]["x-web-serving-mode"] == "desktop"
        assert call["body"]["search_data"]["form_data"]["data"] == search_config["form_data"]

    def test_search_http_error_raises(self, search_config):
        transport = FakeTransport(
            [("https://api.divar.ir/v8/postlist/w/search", (429, {"retry-after": "7"}, b""))]
        )
        fetcher = DivarFetcher(transport=transport)
        with pytest.raises(DivarHTTPError) as excinfo:
            asyncio.run(fetcher.search(search_config))
        assert excinfo.value.status == 429
        assert excinfo.value.retry_after == "7"


class TestFetcherGetPost:
    def _detail_payload(self):
        return {
            "sections": [
                {
                    "section_name": "LIST_DATA",
                    "widgets": [
                        {
                            "widget_type": "GROUP_INFO_ROW",
                            "data": {"items": [{"title": "متراژ", "value": "۹۷"}]},
                        }
                    ],
                }
            ],
            "seo": {"web_info": {"district_persian": "یوسف‌آباد", "city_persian": "تهران"}},
            "share": {"web_url": "https://divar.ir/v/gap5-Twe"},
            "webengage": {"token": "gap5-Twe"},
        }

    def test_json_detail(self):
        transport = FakeTransport(
            [("https://api.divar.ir/v8/posts-v2/web/", _json_response(self._detail_payload()))]
        )
        fetcher = DivarFetcher(transport=transport)
        detail = asyncio.run(fetcher.get_post("gap5-Twe"))
        assert detail.token == "gap5-Twe"
        assert detail.size == 97
        assert transport.calls[0]["url"].endswith("/gap5-Twe")
        assert "content-type" not in transport.calls[0]["headers"]  # GET بدون content-type

    def test_403_falls_back_to_html(self):
        html = (
            "<html><script>window.__PRELOADED_STATE__ = "
            + json.dumps(
                {
                    "currentPost": {
                        "post": {
                            "token": "gap5-Twe",
                            "sections": {
                                "LIST_DATA": [
                                    {
                                        "widgetType": "GROUP_INFO_ROW",
                                        "dto": {
                                            "widget_type": "GROUP_INFO_ROW",
                                            "data": {
                                                "items": [{"title": "متراژ", "value": "۹۷"}]
                                            }
                                        },
                                    }
                                ]
                            },
                            "seo": {
                                "webInfo": {
                                    "district_persian": "یوسف‌آباد",
                                    "city_persian": "تهران",
                                }
                            },
                        }
                    }
                },
                ensure_ascii=True,
            )
            + ";</script></html>"
        )
        transport = FakeTransport(
            [
                ("https://api.divar.ir/v8/posts-v2/web/", (403, {}, b"")),
                ("https://divar.ir/v/", (200, {}, html.encode("utf-8"))),
            ]
        )
        fetcher = DivarFetcher(transport=transport)
        detail = asyncio.run(fetcher.get_post("gap5-Twe"))
        assert detail.size == 97
        assert detail.token == "gap5-Twe"
        assert len(transport.calls) == 2

    def test_non_json_200_falls_back_to_html(self):
        transport = FakeTransport(
            [
                ("https://api.divar.ir/v8/posts-v2/web/", (200, {}, b"<html>guard</html>")),
                ("https://divar.ir/v/", (200, {}, "<html>خالی</html>".encode("utf-8"))),
            ]
        )
        fetcher = DivarFetcher(transport=transport)
        with pytest.raises(DivarUnavailableError):
            asyncio.run(fetcher.get_post("tok"))

    def test_rate_limit_does_not_fall_back(self):
        transport = FakeTransport(
            [("https://api.divar.ir/v8/posts-v2/web/", (503, {}, b""))]
        )
        fetcher = DivarFetcher(transport=transport)
        with pytest.raises(DivarHTTPError):
            asyncio.run(fetcher.get_post("tok"))
        assert len(transport.calls) == 1  # fallback HTML نرفت
