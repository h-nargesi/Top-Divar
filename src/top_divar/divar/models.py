"""مدل‌های دادهٔ لایهٔ دیوار (مرحلهٔ ۳).

فیلدها مطابق نگاشت divar-api.md بخش ۷ است:
- AdCard — فیلدهای نرمال‌شدهٔ کارت search (بخش ۷.۱)
- PostDetail — فیلدهای نرمال‌شدهٔ جزئیات آگهی (بخش ۷.۴)
- SearchPage — صفحهٔ search + صفحه‌بندی (بخش ۵)
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AdCard:
    token: str
    title: Optional[str] = None
    price: Optional[int] = None
    price_agreed: bool = False          # «توافقی» → null صریح (بخش ۸.۱.۳)
    is_promoted: bool = False           # red_text == «نردبان شده»
    district: Optional[str] = None
    city: Optional[str] = None
    image_count: Optional[int] = None
    sort_date: Optional[str] = None     # ISO UTC
    raw: dict = field(default_factory=dict, repr=False)


@dataclass
class PostDetail:
    token: Optional[str] = None
    size: Optional[int] = None
    construction_year: Optional[int] = None
    building_age: Optional[int] = None
    rooms: Optional[int] = None
    price: Optional[int] = None
    price_agreed: bool = False
    price_per_square: Optional[int] = None
    floor: Optional[int] = None
    total_floors: Optional[int] = None
    has_elevator: Optional[bool] = None
    has_parking: Optional[bool] = None
    has_warehouse: Optional[bool] = None
    district: Optional[str] = None
    city: Optional[str] = None
    published_at: Optional[str] = None
    last_bumped_at: Optional[str] = None
    last_updated_at: Optional[str] = None
    raw: dict = field(default_factory=dict, repr=False)


@dataclass
class SearchPage:
    cards: list = field(default_factory=list)
    has_next_page: bool = False
    pagination_data: Optional[dict] = None   # عیناً echo به درخواست صفحه بعد
    no_result: bool = False
    raw: dict = field(default_factory=dict, repr=False)
