import asyncio
import datetime
import sqlite3
import threading

from top_divar.storage import database
from top_divar.storage.errors import DuplicateTokenError, DuplicateUsernameError, StorageError
from top_divar.storage.timestamps import (
    canonical_utc,
    to_utc_datetime,
    utc_now,
    utc_now_iso,
)

SCORING_STATES = ("pending", "scored")
DELIVERY_STATUSES = ("pending", "sent", "dead")
LAST_ERROR_MAX_CHARS = 500

_AD_COLUMNS = (
    "title",
    "price",
    "price_per_square",
    "size",
    "rooms",
    "construction_year",
    "building_age",
    "floor",
    "total_floors",
    "has_parking",
    "has_elevator",
    "has_warehouse",
    "district",
    "city",
    "is_promoted",
    "image_count",
    "published_at",
    "last_bumped_at",
    "last_updated_at",
    "raw_json",
)


def _optional_int(value, name: str):
    if value is None or (isinstance(value, int) and not isinstance(value, bool)):
        return value
    raise StorageError(f"فیلد «{name}» آگهی باید عدد صحیح یا null باشد («{value!r}»).")


def _optional_bool(value, name: str):
    if value is None:
        return None
    if isinstance(value, bool):
        return int(value)
    raise StorageError(f"فیلد «{name}» آگهی باید بولی یا null باشد («{value!r}»).")


def _optional_text(value, name: str):
    if value is None or isinstance(value, str):
        return value
    raise StorageError(f"فیلد «{name}» آگهی باید رشته یا null باشد («{value!r}»).")


def _prepare_ad_columns(record: dict) -> dict:
    """اعتبارسنجی و آماده‌سازی فیلدهای مشترک آگهی برای درج/به‌روزرسانی (مرحلهٔ ۴)."""
    if record.get("sort_date") is None:
        raise StorageError("sort_date آگهی لازم است و نمی‌تواند null باشد.")
    values = {
        "title": _optional_text(record.get("title"), "title"),
        "price": _optional_int(record.get("price"), "price"),
        "price_per_square": _optional_int(
            record.get("price_per_square"), "price_per_square"
        ),
        "size": _optional_int(record.get("size"), "size"),
        "rooms": _optional_int(record.get("rooms"), "rooms"),
        "construction_year": _optional_int(
            record.get("construction_year"), "construction_year"
        ),
        "building_age": _optional_int(record.get("building_age"), "building_age"),
        "floor": _optional_int(record.get("floor"), "floor"),
        "total_floors": _optional_int(record.get("total_floors"), "total_floors"),
        "has_parking": _optional_bool(record.get("has_parking"), "has_parking"),
        "has_elevator": _optional_bool(record.get("has_elevator"), "has_elevator"),
        "has_warehouse": _optional_bool(record.get("has_warehouse"), "has_warehouse"),
        "district": _optional_text(record.get("district"), "district"),
        "city": _optional_text(record.get("city"), "city"),
        "is_promoted": _optional_bool(record.get("is_promoted", False), "is_promoted"),
        "image_count": _optional_int(record.get("image_count"), "image_count"),
        "sort_date": canonical_utc(record["sort_date"], what="sort_date"),
        "published_at": (
            canonical_utc(record["published_at"], what="published_at")
            if record.get("published_at") is not None
            else None
        ),
        "last_bumped_at": (
            canonical_utc(record["last_bumped_at"], what="last_bumped_at")
            if record.get("last_bumped_at") is not None
            else None
        ),
        "last_updated_at": (
            canonical_utc(record["last_updated_at"], what="last_updated_at")
            if record.get("last_updated_at") is not None
            else None
        ),
        "raw_json": _optional_text(record.get("raw_json"), "raw_json"),
    }
    return values


class SqliteRepository:
    def __init__(self, db_path):
        self._db_path = db_path
        self._conn = database.connect(db_path)
        self._lock = threading.Lock()
        try:
            self._version = database.migrate(self._conn)
        except StorageError:
            self._conn.close()
            raise

    @property
    def db_path(self):
        return self._db_path

    @property
    def schema_version(self) -> int:
        return self._version

    def close(self) -> None:
        with self._lock:
            self._conn.close()

    def _run(self, fn):
        with self._lock:
            try:
                result = fn(self._conn)
            except BaseException:
                self._conn.rollback()
                raise
            self._conn.commit()
            return result

    async def _call(self, fn):
        return await asyncio.to_thread(self._run, fn)

    async def insert_ad(
        self,
        token: str,
        sort_date,
        *,
        title=None,
        price=None,
        price_per_square=None,
        size=None,
        rooms=None,
        construction_year=None,
        building_age=None,
        floor=None,
        total_floors=None,
        has_parking=None,
        has_elevator=None,
        has_warehouse=None,
        district=None,
        city=None,
        is_promoted=False,
        image_count=None,
        published_at=None,
        last_bumped_at=None,
        last_updated_at=None,
        raw_json=None,
        scoring_state: str = "pending",
    ) -> int:
        if not isinstance(token, str) or not token.strip():
            raise StorageError("توکن آگهی باید رشتهٔ غیرخالی باشد.")
        if scoring_state not in SCORING_STATES:
            raise StorageError(
                f"scoring_state نامعتبر است («{scoring_state}»); مقادیر مجاز: "
                + "، ".join(SCORING_STATES)
                + "."
            )
        values = {
            "token": token,
            "title": _optional_text(title, "title"),
            "price": _optional_int(price, "price"),
            "price_per_square": _optional_int(price_per_square, "price_per_square"),
            "size": _optional_int(size, "size"),
            "rooms": _optional_int(rooms, "rooms"),
            "construction_year": _optional_int(
                construction_year, "construction_year"
            ),
            "building_age": _optional_int(building_age, "building_age"),
            "floor": _optional_int(floor, "floor"),
            "total_floors": _optional_int(total_floors, "total_floors"),
            "has_parking": _optional_bool(has_parking, "has_parking"),
            "has_elevator": _optional_bool(has_elevator, "has_elevator"),
            "has_warehouse": _optional_bool(has_warehouse, "has_warehouse"),
            "district": _optional_text(district, "district"),
            "city": _optional_text(city, "city"),
            "is_promoted": _optional_bool(is_promoted, "is_promoted"),
            "image_count": _optional_int(image_count, "image_count"),
            "sort_date": canonical_utc(sort_date, what="sort_date"),
            "published_at": (
                canonical_utc(published_at, what="published_at")
                if published_at is not None
                else None
            ),
            "last_bumped_at": (
                canonical_utc(last_bumped_at, what="last_bumped_at")
                if last_bumped_at is not None
                else None
            ),
            "last_updated_at": (
                canonical_utc(last_updated_at, what="last_updated_at")
                if last_updated_at is not None
                else None
            ),
            "raw_json": _optional_text(raw_json, "raw_json"),
            "scoring_state": scoring_state,
        }
        now = utc_now_iso()
        values["created_at"] = now
        values["updated_at"] = now
        columns = list(values)
        placeholders = ", ".join("?" for _ in columns)
        sql = (
            f"INSERT INTO ads ({', '.join(columns)}) VALUES ({placeholders})"
        )

        def op(conn: sqlite3.Connection):
            cursor = conn.execute(sql, [values[column] for column in columns])
            return int(cursor.lastrowid)

        try:
            return await self._call(op)
        except sqlite3.IntegrityError as exc:
            raise DuplicateTokenError(
                f"آگهی با توکن «{token}» از قبل ذخیره شده است؛ توکن تکراری رد می‌شود."
            ) from exc

    async def get_ad_by_token(self, token: str):
        def op(conn: sqlite3.Connection):
            row = conn.execute(
                "SELECT * FROM ads WHERE token = ?", (token,)
            ).fetchone()
            return dict(row) if row is not None else None

        return await self._call(op)

    async def refresh_ad(self, token: str, record: dict) -> bool:
        """به‌روزرسانی کامل ردیف آگهی بعد از نردبان/ویرایش (bump — مرحلهٔ ۴).

        record همان فیلدهای insert_ad (شامل sort_date تازه) است؛
        scoring_state به «pending» برمی‌گردد تا خط لولهٔ امتیازدهی دسته
        دوباره آن را بگیرد (ADR-0001 — تصمیم ۱۹) و نتیجهٔ امتیاز قبلی
        پاک می‌شود (امتیاز تازه مال امتیازدهی بعدی است).
        """
        if not isinstance(token, str) or not token.strip():
            raise StorageError("توکن آگهی باید رشتهٔ غیرخالی باشد.")
        values = _prepare_ad_columns(record)
        values["scoring_state"] = "pending"
        values["score"] = None
        values["score_breakdown"] = None
        values["updated_at"] = utc_now_iso()
        assignments = ", ".join(f"{column} = ?" for column in values)

        def op(conn: sqlite3.Connection):
            cursor = conn.execute(
                f"UPDATE ads SET {assignments} WHERE token = ?",
                [*values.values(), token],
            )
            return cursor.rowcount > 0

        return await self._call(op)

    async def refresh_ad_from_card(
        self,
        token: str,
        sort_date,
        *,
        title=None,
        is_promoted=False,
        image_count=None,
    ) -> bool:
        """به‌روزرسانی سبک نردبان وقتی جزئیات درنیامد: فقط فیلدهای کارت search.

        فیلدهای وابسته به جزئیات (متراژ، قیمت‌متری، امکانات، …) دست‌نخورده
        می‌مانند تا دادهٔ قبلی از دست نرود (divar-api.md بخش ۹.۹).
        """
        if not isinstance(token, str) or not token.strip():
            raise StorageError("توکن آگهی باید رشتهٔ غیرخالی باشد.")
        values = {
            "sort_date": canonical_utc(sort_date, what="sort_date"),
            "title": _optional_text(title, "title"),
            "is_promoted": _optional_bool(is_promoted, "is_promoted"),
            "image_count": _optional_int(image_count, "image_count"),
            "updated_at": utc_now_iso(),
        }
        assignments = ", ".join(f"{column} = ?" for column in values)

        def op(conn: sqlite3.Connection):
            cursor = conn.execute(
                f"UPDATE ads SET {assignments} WHERE token = ?",
                [*values.values(), token],
            )
            return cursor.rowcount > 0

        return await self._call(op)

    async def record_search_match(self, ad_id: int, search_id: str) -> bool:
        """ثبت ارتباط (آگهی، جستجو)؛ True یعنی ردیف تازه ساخته شد (ADR-0007).

        توکن سراسری بین جستجوهاست؛ جستجوی بعدی فقط همین فهرست را کامل
        می‌کند — بدون ذخیره یا جزئیات دوباره (divar-api.md بخش ۹.۱۰).
        """
        if not isinstance(search_id, str) or not search_id.strip():
            raise StorageError("شناسهٔ جستجو باید رشتهٔ غیرخالی باشد.")

        def op(conn: sqlite3.Connection):
            if (
                conn.execute("SELECT 1 FROM ads WHERE id = ?", (ad_id,)).fetchone()
                is None
            ):
                raise StorageError(f"آگهی با شناسهٔ {ad_id} پیدا نشد.")
            cursor = conn.execute(
                """
                INSERT OR IGNORE INTO matched_searches (ad_id, search_id, first_seen_at)
                VALUES (?, ?, ?)
                """,
                (ad_id, search_id, utc_now_iso()),
            )
            return cursor.rowcount > 0

        return await self._call(op)

    async def get_matched_searches(self, ad_id: int) -> list:
        def op(conn: sqlite3.Connection):
            rows = conn.execute(
                """
                SELECT search_id FROM matched_searches
                WHERE ad_id = ? ORDER BY first_seen_at, id
                """,
                (ad_id,),
            ).fetchall()
            return [row["search_id"] for row in rows]

        return await self._call(op)

    async def touch_tombstone(self, token: str, sort_date):
        """به‌روزرسانی آخرین sort_date دیده‌شدهٔ سنگ قبر؛ فقط جلو رفتن.

        None یعنی سنگ قبری برای این توکن نیست (آگهی هنوز دیده نشده یا
        purge نشده). سنگ قبر ساخته نمی‌شود — purge صاحب ساختش است.
        """
        new_iso = canonical_utc(sort_date, what="sort_date")

        def op(conn: sqlite3.Connection):
            row = conn.execute(
                "SELECT last_sort_date FROM tombstones WHERE token = ?", (token,)
            ).fetchone()
            if row is None:
                return None
            if new_iso <= row["last_sort_date"]:
                return row["last_sort_date"]
            conn.execute(
                "UPDATE tombstones SET last_sort_date = ? WHERE token = ?",
                (new_iso, token),
            )
            return new_iso

        return await self._call(op)

    async def set_scoring_state(self, token: str, scoring_state: str) -> bool:
        if scoring_state not in SCORING_STATES:
            raise StorageError(
                f"scoring_state نامعتبر است («{scoring_state}»); مقادیر مجاز: "
                + "، ".join(SCORING_STATES)
                + "."
            )

        def op(conn: sqlite3.Connection):
            cursor = conn.execute(
                "UPDATE ads SET scoring_state = ?, updated_at = ? WHERE token = ?",
                (scoring_state, utc_now_iso(), token),
            )
            return cursor.rowcount > 0

        return await self._call(op)

    async def get_pending_ads(self) -> list:
        """آگهی‌های در انتظار امتیاز، قدیمی‌ترین اول (خط لولهٔ دسته — مرحلهٔ ۵)."""

        def op(conn: sqlite3.Connection):
            rows = conn.execute(
                """
                SELECT * FROM ads WHERE scoring_state = 'pending'
                ORDER BY created_at, id
                """
            ).fetchall()
            return [dict(row) for row in rows]

        return await self._call(op)

    async def store_score(self, token: str, score, breakdown_json=None) -> bool:
        """ثبت نتیجهٔ امتیاز مطلق: scoring_state=scored + امتیاز و شکست آن."""
        if isinstance(score, bool) or not isinstance(score, int):
            raise StorageError("امتیاز آگهی باید عدد صحیح باشد.")
        if breakdown_json is not None and not isinstance(breakdown_json, str):
            raise StorageError("شکست امتیاز باید رشتهٔ JSON یا null باشد.")

        def op(conn: sqlite3.Connection):
            cursor = conn.execute(
                """
                UPDATE ads SET
                    scoring_state = 'scored',
                    score = ?,
                    score_breakdown = ?,
                    updated_at = ?
                WHERE token = ?
                """,
                (score, breakdown_json, utc_now_iso(), token),
            )
            return cursor.rowcount > 0

        return await self._call(op)

    async def update_watermark(self, search_id: str, sort_date) -> str:
        if not isinstance(search_id, str) or not search_id.strip():
            raise StorageError("شناسهٔ جستجو باید رشتهٔ غیرخالی باشد.")
        new_iso = canonical_utc(sort_date, what="sort_date")

        def op(conn: sqlite3.Connection):
            row = conn.execute(
                "SELECT sort_date FROM watermarks WHERE search_id = ?", (search_id,)
            ).fetchone()
            if row is not None and new_iso <= row["sort_date"]:
                return row["sort_date"]
            conn.execute(
                """
                INSERT INTO watermarks (search_id, sort_date, updated_at)
                VALUES (?, ?, ?)
                ON CONFLICT(search_id) DO UPDATE SET
                    sort_date = excluded.sort_date,
                    updated_at = excluded.updated_at
                """,
                (search_id, new_iso, utc_now_iso()),
            )
            return new_iso

        return await self._call(op)

    async def get_watermark(self, search_id: str):
        def op(conn: sqlite3.Connection):
            row = conn.execute(
                "SELECT sort_date FROM watermarks WHERE search_id = ?", (search_id,)
            ).fetchone()
            return row["sort_date"] if row is not None else None

        return await self._call(op)

    async def get_tombstone(self, token: str):
        def op(conn: sqlite3.Connection):
            row = conn.execute(
                "SELECT * FROM tombstones WHERE token = ?", (token,)
            ).fetchone()
            return dict(row) if row is not None else None

        return await self._call(op)

    async def add_user(self, username: str, chat_id: int) -> int:
        if not isinstance(username, str) or not username.strip():
            raise StorageError("نام کاربری باید رشتهٔ غیرخالی باشد.")
        if isinstance(chat_id, bool) or not isinstance(chat_id, int):
            raise StorageError("chat_id باید عدد صحیح باشد.")
        now = utc_now_iso()

        def op(conn: sqlite3.Connection):
            cursor = conn.execute(
                """
                INSERT INTO users (username, chat_id, created_at, updated_at)
                VALUES (?, ?, ?, ?)
                """,
                (username, chat_id, now, now),
            )
            return int(cursor.lastrowid)

        try:
            return await self._call(op)
        except sqlite3.IntegrityError as exc:
            raise DuplicateUsernameError(
                f"نام کاربری «{username}» قبلاً گرفته شده است."
            ) from exc

    async def get_user(self, username: str):
        def op(conn: sqlite3.Connection):
            row = conn.execute(
                "SELECT * FROM users WHERE username = ?", (username,)
            ).fetchone()
            return dict(row) if row is not None else None

        return await self._call(op)

    async def get_user_by_chat_id(self, chat_id: int):
        def op(conn: sqlite3.Connection):
            row = conn.execute(
                "SELECT * FROM users WHERE chat_id = ?", (chat_id,)
            ).fetchone()
            return dict(row) if row is not None else None

        return await self._call(op)

    async def remove_user(self, username: str) -> bool:
        def op(conn: sqlite3.Connection):
            cursor = conn.execute(
                "DELETE FROM users WHERE username = ?", (username,)
            )
            return cursor.rowcount > 0

        return await self._call(op)

    async def create_delivery_rows(self, ad_id: int, recipients) -> int:
        rows = []
        for pair in recipients:
            if not isinstance(pair, (tuple, list)) or len(pair) != 2:
                raise StorageError(
                    "هر گیرنده باید زوج (channel, recipient) باشد."
                )
            channel, recipient = pair
            if not isinstance(channel, str) or not channel.strip():
                raise StorageError("نام کانال تحویل باید رشتهٔ غیرخالی باشد.")
            if not isinstance(recipient, str) or not recipient.strip():
                raise StorageError("نشانی گیرندهٔ تحویل باید رشتهٔ غیرخالی باشد.")
            rows.append((ad_id, channel, recipient))
        now = utc_now_iso()

        def op(conn: sqlite3.Connection):
            if conn.execute(
                "SELECT 1 FROM ads WHERE id = ?", (ad_id,)
            ).fetchone() is None:
                raise StorageError(f"آگهی با شناسهٔ {ad_id} پیدا نشد.")
            count = 0
            for _, channel, recipient in rows:
                conn.execute(
                    """
                    INSERT INTO delivery
                        (ad_id, channel, recipient, created_at, updated_at)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (ad_id, channel, recipient, now, now),
                )
                count += 1
            return count

        try:
            return await self._call(op)
        except sqlite3.IntegrityError as exc:
            raise StorageError(
                "ردیف تحویل برای همین (آگهی، کانال، گیرنده) از قبل وجود دارد."
            ) from exc

    async def get_deliveries(self, ad_id: int):
        def op(conn: sqlite3.Connection):
            rows = conn.execute(
                "SELECT * FROM delivery WHERE ad_id = ? ORDER BY id", (ad_id,)
            ).fetchall()
            return [dict(row) for row in rows]

        return await self._call(op)

    async def mark_delivery(
        self,
        delivery_id: int,
        status: str,
        *,
        error=None,
        next_attempt_at=None,
    ) -> bool:
        if status not in DELIVERY_STATUSES:
            raise StorageError(
                f"وضعیت تحویل نامعتبر است («{status}»); مقادیر مجاز: "
                + "، ".join(DELIVERY_STATUSES)
                + "."
            )
        if error is not None and not isinstance(error, str):
            raise StorageError("خطای تحویل باید رشته یا null باشد.")
        error_text = (
            None if error is None else error[:LAST_ERROR_MAX_CHARS]
        )
        next_attempt_iso = (
            None
            if next_attempt_at is None
            else canonical_utc(next_attempt_at, what="next_attempt_at")
        )

        def op(conn: sqlite3.Connection):
            cursor = conn.execute(
                """
                UPDATE delivery SET
                    status = ?,
                    attempts = attempts + 1,
                    last_error = ?,
                    last_attempt_at = ?,
                    next_attempt_at = ?,
                    updated_at = ?
                WHERE id = ?
                """,
                (
                    status,
                    error_text,
                    utc_now_iso(),
                    next_attempt_iso,
                    utc_now_iso(),
                    delivery_id,
                ),
            )
            return cursor.rowcount > 0

        return await self._call(op)

    async def purge_expired(self, purge_after_days: float, *, now=None) -> dict:
        if (
            isinstance(purge_after_days, bool)
            or not isinstance(purge_after_days, (int, float))
            or purge_after_days < 0
        ):
            raise StorageError("purge_after_days باید عدد غیرمنفی باشد.")
        moment = utc_now() if now is None else to_utc_datetime(now, what="now")
        cutoff_iso = canonical_utc(
            moment - datetime.timedelta(days=purge_after_days)
        )

        def op(conn: sqlite3.Connection):
            purged_ads = 0
            purged_deliveries = 0
            rows = conn.execute(
                "SELECT id, token, sort_date FROM ads WHERE sort_date < ?",
                (cutoff_iso,),
            ).fetchall()
            for row in rows:
                conn.execute(
                    """
                    INSERT INTO tombstones (token, last_sort_date)
                    VALUES (?, ?)
                    ON CONFLICT(token) DO UPDATE SET
                        last_sort_date = MAX(last_sort_date, excluded.last_sort_date)
                    """,
                    (row["token"], row["sort_date"]),
                )
                deleted = conn.execute(
                    "DELETE FROM delivery WHERE ad_id = ?", (row["id"],)
                )
                purged_deliveries += deleted.rowcount
                conn.execute("DELETE FROM ads WHERE id = ?", (row["id"],))
                purged_ads += 1
            return {
                "ads": purged_ads,
                "deliveries": purged_deliveries,
                "cutoff": cutoff_iso,
            }

        return await self._call(op)
