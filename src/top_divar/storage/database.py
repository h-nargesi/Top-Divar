import sqlite3
from pathlib import Path

from top_divar.storage.errors import StorageError

DEFAULT_DB_PATH = Path("data") / "top_divar.sqlite3"
BUSY_TIMEOUT_MS = 5_000

MIGRATIONS: list = [
    (
        1,
        [
            """
            CREATE TABLE ads (
                id INTEGER PRIMARY KEY,
                token TEXT NOT NULL,
                title TEXT,
                price INTEGER,
                price_per_square INTEGER,
                size INTEGER,
                rooms INTEGER,
                construction_year INTEGER,
                building_age INTEGER,
                floor INTEGER,
                total_floors INTEGER,
                has_parking INTEGER,
                has_elevator INTEGER,
                has_warehouse INTEGER,
                district TEXT,
                city TEXT,
                is_promoted INTEGER NOT NULL DEFAULT 0,
                image_count INTEGER,
                sort_date TEXT NOT NULL,
                published_at TEXT,
                last_bumped_at TEXT,
                last_updated_at TEXT,
                raw_json TEXT,
                scoring_state TEXT NOT NULL DEFAULT 'pending'
                    CHECK (scoring_state IN ('pending', 'scored')),
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            """,
            "CREATE UNIQUE INDEX idx_ads_token ON ads (token)",
            "CREATE INDEX idx_ads_sort_date ON ads (sort_date)",
            """
            CREATE TABLE tombstones (
                token TEXT PRIMARY KEY,
                last_sort_date TEXT NOT NULL
            )
            """,
            """
            CREATE TABLE watermarks (
                search_id TEXT PRIMARY KEY,
                sort_date TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            """,
            """
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL COLLATE NOCASE,
                chat_id INTEGER NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            """,
            "CREATE UNIQUE INDEX idx_users_username ON users (username)",
            "CREATE INDEX idx_users_chat_id ON users (chat_id)",
            """
            CREATE TABLE delivery (
                id INTEGER PRIMARY KEY,
                ad_id INTEGER NOT NULL REFERENCES ads (id) ON DELETE CASCADE,
                channel TEXT NOT NULL,
                recipient TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'pending'
                    CHECK (status IN ('pending', 'sent', 'dead')),
                attempts INTEGER NOT NULL DEFAULT 0,
                last_error TEXT,
                last_attempt_at TEXT,
                next_attempt_at TEXT,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            """,
            """
            CREATE UNIQUE INDEX idx_delivery_ad_channel_recipient
                ON delivery (ad_id, channel, recipient)
            """,
            "CREATE INDEX idx_delivery_status ON delivery (status)",
        ],
    ),
    (
        2,
        [
            """
            CREATE TABLE matched_searches (
                id INTEGER PRIMARY KEY,
                ad_id INTEGER NOT NULL REFERENCES ads (id) ON DELETE CASCADE,
                search_id TEXT NOT NULL,
                first_seen_at TEXT NOT NULL,
                UNIQUE (ad_id, search_id)
            )
            """,
            "CREATE INDEX idx_matched_searches_search ON matched_searches (search_id)",
        ],
    ),
]


def connect(db_path) -> sqlite3.Connection:
    path = Path(db_path)
    if str(path.parent) not in ("", "."):
        path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(
        str(path),
        timeout=BUSY_TIMEOUT_MS / 1000.0,
        check_same_thread=False,
    )
    conn.row_factory = sqlite3.Row
    conn.execute(f"PRAGMA busy_timeout = {BUSY_TIMEOUT_MS}")
    conn.execute("PRAGMA journal_mode = WAL")
    conn.execute("PRAGMA synchronous = NORMAL")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def schema_version(conn: sqlite3.Connection) -> int:
    return int(conn.execute("PRAGMA user_version").fetchone()[0])


def latest_version() -> int:
    return MIGRATIONS[-1][0] if MIGRATIONS else 0


def migrate(conn: sqlite3.Connection) -> int:
    current = schema_version(conn)
    if current > latest_version():
        raise StorageError(
            f"نسخهٔ پایگاه داده ({current}) از نسخهٔ کد ({latest_version()}) جدیدتر است؛"
            " برنامه را به‌روز کنید."
        )
    for version, statements in MIGRATIONS:
        if version <= current:
            continue
        try:
            with conn:
                for statement in statements:
                    conn.execute(statement)
                conn.execute(f"PRAGMA user_version = {version}")
        except sqlite3.Error as exc:
            raise StorageError(
                f"مهاجرت پایگاه داده به نسخهٔ {version} شکست خورد: {exc}"
            ) from exc
    return schema_version(conn)
