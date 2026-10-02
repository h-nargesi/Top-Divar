"""تست قالب پیام اطلاع‌رسانی (مرحلهٔ ۶) — configuration.md بخش ۳.۲ تا ۳.۴."""

import json

from top_divar.notify.message import (
    TELEGRAM_MAX_CHARS,
    breakdown_text,
    build_email_body,
    build_email_subject,
    build_telegram_message,
    escape_html,
    format_jalali_moment,
    post_link,
)

AD = {
    "token": "gapa1FMk",
    "title": "آپارتمان ۵۵ متری پونک",
    "price": 12_900_000_000,
    "price_per_square": 234_500_000,
    "size": 55,
    "rooms": 2,
    "construction_year": 1403,
    "building_age": 2,
    "floor": 3,
    "total_floors": 8,
    "has_parking": True,
    "has_elevator": True,
    "has_warehouse": True,
    "district": "پونک",
    "city": "تهران",
    "published_at": "2026-09-13T13:49:00+00:00",
    "raw_json": json.dumps({"search_card": {}}, ensure_ascii=False),
    "score": 65,
    "score_breakdown": json.dumps(
        [
            {"label": "قیمت≤۱۳.۵B", "points": 15},
            {"label": "قیمت‌متری≤۲۸۰M", "points": 20},
            {"label": "عمر≤۵", "points": 15},
            {"label": "اتاق≥۲", "points": 5},
            {"label": "پارکینگ", "points": 5},
            {"label": "آسانسور", "points": 5},
        ],
        ensure_ascii=False,
    ),
}


def test_full_message_layout_matches_approved_sample():
    message = build_telegram_message(AD, "آپارتمان تهران")
    lines = message.split("\n")
    assert lines[0] == "<b>آپارتمان ۵۵ متری پونک — آپارتمان تهران</b>"
    assert lines[1] == "قیمت: ۱۲,۹۰۰,۰۰۰,۰۰۰ تومان"
    assert lines[2] == "قیمت هر متر: ۲۳۴,۵۰۰,۰۰۰ تومان"
    assert lines[3] == "متراژ: ۵۵"
    assert lines[4] == "اتاق: ۲"
    assert lines[5] == "ساخت: ۱۴۰۳ (عمر ۲ سال)"
    assert lines[6] == "طبقه: ۳ از ۸"
    assert lines[7] == "امکانات: پارکینگ · آسانسور · انباری"
    assert lines[8] == "محله: پونک"
    assert lines[9] == "شهر: تهران"
    assert lines[10] == "انتشار: ۲۲ شهریور ۱۴۰۵، ۱۷:۱۹"
    assert lines[11].startswith("امتیاز: ۶۵ — قیمت≤۱۳.۵B: ۱۵ · ")
    assert lines[12] == "https://divar.ir/v/gapa1FMk"


def test_single_message_with_only_header_score_and_link():
    ad = {"token": "t1", "title": "خونه", "score": 10}
    message = build_telegram_message(ad, "s")
    assert message.split("\n") == [
        "<b>خونه — s</b>",
        "امتیاز: ۱۰",
        "https://divar.ir/v/t1",
    ]


def test_missing_fields_are_omitted():
    ad = {
        "token": "t2",
        "title": "آپارتمان بدون جزئیات",
        "price_per_square": None,
        "size": None,
        "published_at": None,
        "score": 5,
    }
    message = build_telegram_message(ad, None)
    assert "قیمت" not in message
    assert "انتشار" not in message
    assert "متراژ" not in message
    assert message.split("\n")[0] == "<b>آپارتمان بدون جزئیات</b>"


def test_variable_texts_are_html_escaped():
    ad = {
        "token": "t3",
        "title": "فروش <خونه> & باغ",
        "district": "سعادت<آباد",
        "score": 1,
        "score_breakdown": json.dumps(
            [{"label": "محله ∈ {سعادت<آباد}", "points": 1}], ensure_ascii=False
        ),
    }
    message = build_telegram_message(ad, "جستجو & فیلتر")
    assert "<b>فروش &lt;خونه&gt; &amp; باغ — جستجو &amp; فیلتر</b>" in message
    assert "محله: سعادت&lt;آباد" in message
    assert "سعادت&lt;آباد" in message.split("\n")[-2]
    # تگ HTML فقط از قالب خود پیام می‌آید
    assert "<b>" in message and "<خونه>" not in message


def test_agreed_price_shown_as_tavafoghi():
    ad = {
        "token": "t4",
        "title": "آپارتمان",
        "price": None,
        "raw_json": json.dumps({"price_agreed": True}, ensure_ascii=False),
        "score": 0,
    }
    message = build_telegram_message(ad, "s")
    assert "قیمت: توافقی" in message


def test_floor_variants_and_partial_amenities():
    base = dict(AD)
    base.update({"floor": 2, "total_floors": None, "has_warehouse": False, "has_parking": None})
    message = build_telegram_message(base, "l")
    assert "طبقه: ۲" in message
    assert "امکانات: آسانسور" in message
    assert "از ۸" not in message
    assert "پارکینگ · " not in message


def test_age_only_line():
    ad = {"token": "t5", "title": "x", "building_age": 12, "score": 0}
    message = build_telegram_message(ad, "l")
    assert "عمر: ۱۲ سال" in message
    assert "ساخت:" not in message


def test_truncation_single_message_preserves_header_score_link():
    ad = dict(AD)
    ad["title"] = "عنوان " * 30  # بلند ولی قابل‌جای‌دادن
    long_breakdown = [
        {"label": f"قاعدهٔ شمارهٔ {i} با متن بلند برای پرکردن پیام", "points": i}
        for i in range(120)
    ]
    ad["score_breakdown"] = json.dumps(long_breakdown, ensure_ascii=False)
    message = build_telegram_message(ad, "برچسب بلند جستجو")
    assert len(message) <= TELEGRAM_MAX_CHARS
    assert message.count("\n") >= 2
    lines = message.split("\n")
    assert lines[0].startswith("<b>") and lines[0].endswith("</b>")
    assert lines[-1] == post_link(ad)
    assert "امتیاز: " in message


def test_truncation_drops_middle_fields_before_breakdown():
    ad = dict(AD)
    ad["title"] = "ط" * 4026  # همهٔ فیلدها باید قربانی شوند؛ شکست امتیاز جا می‌ماند
    ad["score_breakdown"] = json.dumps(
        [{"label": "قیمت≤۱۳.۵B", "points": 15}], ensure_ascii=False
    )
    message = build_telegram_message(ad, "l")
    assert len(message) <= TELEGRAM_MAX_CHARS
    # فیلدهای میانی از قدیمی‌ترین اولویت نمایش قربانی شدند (اینجا: همه)
    assert "قیمت: ۱۲,۹۰۰" not in message
    assert "قیمت هر متر" not in message
    assert "متراژ: ۵۵" not in message
    assert "اتاق: ۲" not in message
    assert "انتشار:" not in message
    # شکست امتیاز و خط اول و لینک ماندند
    assert message.split("\n")[0].startswith("<b>ط")
    assert "امتیاز: ۶۵ — قیمت≤۱۳.۵B: ۱۵" in message
    assert message.endswith("https://divar.ir/v/gapa1FMk")


def test_truncation_cuts_breakdown_from_middle_with_marker():
    ad = dict(AD)
    ad["title"] = "ط" * 2500
    ad["score_breakdown"] = json.dumps(
        [{"label": "ل" * 900, "points": 1}, {"label": "ب" * 900, "points": 2}],
        ensure_ascii=False,
    )
    message = build_telegram_message(ad, "l")
    assert len(message) <= TELEGRAM_MAX_CHARS
    score_line = message.split("\n")[-2]
    assert score_line.startswith("امتیاز: ۶۵ — ")
    assert "…" in score_line  # نشانگر برش از میانه
    assert score_line.endswith("…ببببب: ۲") or "ب" * 10 in score_line


def test_truncation_last_resort_keeps_score_number_only():
    ad = dict(AD)
    ad["title"] = "ط" * 4000
    ad["score_breakdown"] = json.dumps(
        [{"label": "ق" * 3000, "points": 1}], ensure_ascii=False
    )
    message = build_telegram_message(ad, "ل" * 100)
    assert len(message) <= TELEGRAM_MAX_CHARS
    lines = message.split("\n")
    assert lines[-1] == post_link(ad)
    assert lines[-2] == "امتیاز: ۶۵" or lines[-2].startswith("امتیاز: ۶۵ —")
    assert lines[0].startswith("<b>")


def test_breakdown_text_format():
    payload = json.dumps(
        [{"label": "پارکینگ", "points": 5}, {"label": "عمر≤۵", "points": 15}],
        ensure_ascii=False,
    )
    assert breakdown_text(payload) == "پارکینگ: ۵ · عمر≤۵: ۱۵"
    assert breakdown_text(None) == ""
    assert breakdown_text("not json") == ""
    assert breakdown_text(json.dumps({"label": "x", "points": 1})) == ""


def test_escape_html():
    assert escape_html("a&b<c>d") == "a&amp;b&lt;c&gt;d"


def test_jalali_moment_format():
    assert format_jalali_moment("2026-09-13T13:49:00+00:00") == "۲۲ شهریور ۱۴۰۵، ۱۷:۱۹"
    assert format_jalali_moment("2026-01-01T20:31:00Z") == "۱۲ دی ۱۴۰۴، ۰۰:۰۱"


def test_email_subject_approved_format():
    assert build_email_subject(AD) == "Top Divar — آپارتمان ۵۵ متری پونک (امتیاز ۶۵)"


def test_email_body_plain_text_same_fields():
    body = build_email_body(AD, "آپارتمان تهران")
    assert "<b>" not in body
    assert body.split("\n")[0] == "آپارتمان ۵۵ متری پونک — آپارتمان تهران"
    assert "قیمت: ۱۲,۹۰۰,۰۰۰,۰۰۰ تومان" in body
    assert "انتشار: ۲۲ شهریور ۱۴۰۵، ۱۷:۱۹" in body
    assert body.split("\n")[-1] == "https://divar.ir/v/gapa1FMk"
