"""لایهٔ دیوار (مرحلهٔ ۳): واکشی، پارس و نرمال‌سازی."""

from top_divar.divar.errors import (
    DivarError,
    DivarHTTPError,
    DivarSchemaError,
    DivarUnavailableError,
)
from top_divar.divar.fetcher import DivarFetcher, build_search_body
from top_divar.divar.ingest import IngestResult, build_ad_record, ingest_search_page
from top_divar.divar.models import AdCard, PostDetail, SearchPage
from top_divar.divar.queue import DivarRequestQueue

__all__ = [
    "AdCard",
    "DivarError",
    "DivarFetcher",
    "DivarHTTPError",
    "DivarRequestQueue",
    "DivarSchemaError",
    "DivarUnavailableError",
    "IngestResult",
    "PostDetail",
    "SearchPage",
    "build_ad_record",
    "build_search_body",
    "ingest_search_page",
]
