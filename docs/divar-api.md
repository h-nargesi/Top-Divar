# API غیررسمی دیوار (v8)

> مرجع نمونه‌های خام: [`fetch-sample.md`](fetch-sample.md) (گرفته‌شده با DevTools → Copy as fetch).
> این API **غیررسمی و نسخه‌دار** است و بدون اطلاع می‌تواند تغییر کند. پس از هر تغییرِ ساختار، نمونه‌ها را دوباره Capture کنید و این سند را به‌روز کنید.

## ۱. Endpointها

| Endpoint | روش | کاربرد | وضعیت |
|---|---|---|---|
| `https://api.divar.ir/v8/postlist/w/search` | POST | لیست آگهی‌ها + صفحه‌بندی — **تنها endpoint فعال** | مستند (نمونه داریم) |
| `https://api.divar.ir/v8/mapview/viewport` | POST | پین‌های نقشه در ناحیه `bbox` | **رد شده** (ADR-0006) — مختصات پین‌ها تقریبی و لازم نیست |
| جزئیات آگهی (post detail) | ؟ | فیلدهای کامل (طبقه، متن توضیحات، …) | **باز** — نیاز به نمونه |

تصمیم (ADR-0004 + ADR-0006): فقط `postlist/w/search`؛ جغرافیا با **allowlist محله‌ها** روی `district_persian` پاسخ (پس‌فیلتر سمت کلاینت — بخش ۵). `bbox` به‌عنوان پیش‌فیلتر اختیاری سرور باقی می‌ماند؛ مختصات `viewport` لازم نیست. اگر در آینده قاعده امتیاز جغرافیایی (مثل فاصله تا مترو) لازم شد، `viewport` می‌تواند به‌عنوان Fetcher مکمل برگردد.

## ۲. هدرهای درخواست

هدرهای حداقلی (هدرهای sentry/trace در نمونه‌ها نویز هستند و لازم نیست):

```
accept: application/json, text/plain, */*
content-type: application/json
referer: https://divar.ir/
user-agent: <رشته User-Agent مرورگر واقعی>
x-web-serving-mode: desktop
```

- **بدون کوکی تأیید شد**: هر دو نمونه «search page 1/2» در مرورگر تازهِ بدون کوکی/لاگین Captured شده‌اند (عبارت `credentials: "include"` در snippet صرفاً پیش‌فرض کپی DevTools است).
- نسخه `v8` را در آداپتور پین کنید؛ تغییر major یعنی هشدار.

## ۳. ساختار بدنه درخواست (search)

```jsonc
{
  "source_view": "FILTER",                       // نمونه‌های دیده‌شده: MAP_DISCOVERY_MAP / FILTER
  "city_ids": ["1"],                             // تهران
  "user_selected_location": {"places": [{"place_id": "1"}]},
  "pagination_data": { /* فقط برای صفحه ≥ ۲؛ همان pagination.data پاسخ قبلی، عیناً echo می‌شود */ },
  "search_data": {
    "form_data": {
      "data": {
        // ← فیلترها؛ دقیقاً همان کلیدهای خود دیوار (بخش ۴)
      }
    },
    "server_payload": {
      "additional_form_data": {
        "data": {"sort": {"str": {"value": "sort_date"}}}   // «جدیدترین» — تأییدشده
      }
    }
  }
}
```

- **فیلترها عیناً و بدون ترجمه از کانفیگ کاربر به `form_data.data` کپی می‌شوند** (pass-through؛ ر. ک. `configuration.md`).
- **`sort_date` تأیید شد** (نمونه districts): مقدار sort «جدیدترین» در `server_payload.additional_form_data` می‌نشیند، نه در `form_data.data` (پاسخ، آن را داخل echoی `form_data_json` ادغام می‌کند — به request اعمال نکنید).
- **صفحه‌بندی تأیید شد:** برای صفحه بعد، کل آبجکت `pagination.data` پاسخ قبلی (شامل `page`، `search_uid`، `viewed_tokens`، `filters_hash`، …) به‌عنوان `pagination_data` در بدنه درخواست بعدی برگردانده می‌شود.
- `map_state` می‌تواند خالی باشد (`{"camera_info": {"bbox": {}}}`) — bbox لازم نیست.
- **پاسخ بدون نتیجه:** اگر شرطی نتیجه نداشته باشد، `list_widgets` اصلاً نمی‌آید و `show_no_search_result_notice: true` است — خطا نیست و باید طبیعی هندل شود.
- **جغرافیا (ADR-0006):** مکانیزم اصلی، پس‌فیلتر `districts` روی `district_persian` پاسخ است (`configuration.md` بخش ۱). دیوار خودش هم کلید بومی `districts` (با ID عددی محله‌ها) دارد — بخش ۴ — که پس از تهیه جدول نگاشت نام→ID می‌تواند جای پس‌فیلتر را بگیرد. `bbox` فقط پیش‌فیلتر اختیاری سرور باقی می‌ماند.

## ۴. کلیدهای تأییدشده فیلترها (`form_data.data`)

از نمونه واقعی `apartment-sell` (خرید آپارتمان):

| کلید | تایپ ساختار | نمونه | نکته |
|---|---|---|---|
| `category` | `str` | `{"str": {"value": "apartment-sell"}}` | دسته خرید آپارتمان |
| `price` | `number_range` | `{"number_range": {"minimum": "10000000000", "maximum": "15000000000"}}` | قیمت کل، **تومان مطلق**؛ مقادیر رشته‌اند |
| `price_per_square` | `number_range` | `min: "256000000", max: "300000000"` | قیمت هر متر |
| `size` | `number_range` | `min: "40", max: "60"` | متراژ |
| `rooms` | `repeated_string` | `{"repeated_string": {"value": ["یک"]}}` | **کلمات فارسی**: یک/دو/سه/چهار… |
| `building-age` | `number_range` | `min: "10", max: "15"` | عمر بنا به سال |
| `floor` | `number_range` | `min: "-1", max: "8"` | `-1` = زیر همکف، `0` = همکف |
| `elevator` | `boolean` | `{"boolean": {"value": true}}` | آسانسور |
| `parking` | `boolean` | `true` | پارکینگ |
| `warehouse` | `boolean` | `true` | انبار |
| `rebuilt` | `boolean` | `true` | بازسازی‌شده |
| `districts` | `repeated_string` | `{"repeated_string": {"value": ["198", "399", …]}}` | **فیلتر بومی محله‌ها سمت سرور** با ID عددی (نمونه districts). فعلاً IDها مات‌اند؛ پس از تهیه جدول نام→ID، جایگزین پس‌فیلتر `district_persian` می‌شود (ADR-0006) |
| `recent_ads` | `str` | `{"str": {"value": "1d"}}` | فقط آگهی‌های ~۲۴ ساعت اخیر — **معنی تأیید شد**؛ مکمل watermark برای سبک‌شدن پاسخ (پایش اصلی همچنان watermark است) |
| `bbox` | `repeated_float` | `[minLon, minLat, maxLon, maxLat]` | پیش‌فیلتر اختیاری سرور؛ جغرافیای اصلی با allowlist محله‌ها است (ADR-0006) |

تایپ‌های مقدار: `str`، `number_range` (min/max به‌صورت رشته)، `boolean`، `repeated_string`، `repeated_float`. هر کلید جدیدی که دیوار اضافه کند، بدون تغییر کد از کانفیگ عبور داده می‌شود.

## ۵. ساختار پاسخ `postlist/w/search`

موارد مهم (بقیه برای UI وب‌سایت است و نادیده گرفته می‌شود):

- `list_widgets[]` ممکن است علاوه بر `POST_ROW` ردیف‌های غیرآگهی هم داشته باشد (`DIVIDER_ROW` و… — دیده‌شده در صفحه ۲ نمونه) → پارسر فقط `widget_type == "POST_ROW"` را پردازش می‌کند
- به‌ازای هر آگهی (`POST_ROW`) — **فیلدست کامل با نمونه دوصفحه‌ای بدون کوکی تأیید شد**:
  - `data.token` — کلید یکتای آگهی (همان `divar_token` در Storage)
  - `data.title`، `data.image_url`، `data.image_count`
  - `data.middle_description_text` — قیمت مطلقِ فرمت‌شده با ارقام فارسی، مثل `"۳۵,۰۰۰,۰۰۰,۰۰۰ تومان"`
  - `data.bottom_description_text` — **دو شکل تأییدشده**: «⟨نام مشاور/آژانس⟩ در ⟨محله⟩» (مثل «آژانس ملکاتو در سعادت‌آباد») یا «⟨زمان نسبی⟩ در ⟨محله⟩» برای آگهی شخصی (مثل «۹ ساعت پیش در آبشار تهران (دریاچه)») — مبنای heuristic آیندهٔ `is_dealer` (فعلاً خارج از دامنه)
  - `data.red_text` — اختیاری؛ `"نردبان شده"` (آگهی promoted) → فیلد اطلاعاتی `is_promoted`
  - `data.image_top_left_tag` — تعداد عکس/ویدیو (آیکن CAMERA/VIDEOCAM) — با `image_count` هم‌پوشان است
  - `data.action.payload.web_info.district_persian` / `city_persian` — محله/شهر — **کلید فیلتر جغرافیایی** (ADR-0006)؛ تطبیق باید **contains نرمال‌شده** باشد چون «نارمک» و «نارمک جنوبی» هر دو به‌صورت مستقل می‌آیند
  - `action_log.server_side_info.info.sort_date` — زمان ISO (UTC) مثل `"2026-09-15T14:29:17.323148Z"` — **کلید اصلی مرتب‌سازی و watermark پایش**
  - ⚠️ `action_log…info.extra_data` (`jli`، `form_data_json` و…) فقط **echoی فیلترهای جستجو** است، نه داده هر آگهی — از آن فیلد per-ad استخراج نکنید (تله اصلی پیاده‌سازی)
- سطح پاسخ: `action_log…info.posts_metadata[]` — نگاشت فشرده token → `sort_date` (epoch میکروثانیه به‌صورت رشته) + `freshness` — منبع راستی‌آزمایی `sort_date`
- `pagination`:
  - `has_next_page` — **در صفحه آخر نمی‌آید** (تأییدشده در صفحه ۲ نمونه) → غیبت آن = شرط توقف صفحه‌بندی
  - `is_first_page` (فقط صفحه ۱)
  - `data.page`، `data.last_post_date`، `data.search_uid`، `data.viewed_tokens` (فشرده)، `filters_hash` — **تأییدشده**: همین آبجکت عیناً به‌عنوان `pagination_data` در درخواست صفحه بعد برمی‌گردد (صفحه ۲ نمونه)
- پاسخ ممکن است **خالی** باشد: بدون `list_widgets`، با `show_no_search_result_notice: true` و `last_post_date` صفر (`0001-01-01T00:00:00Z`) — طبیعی است، خطا نیست (صفحه ۲ِ همان نمونه دقیقاً این حالت را نشان می‌دهد)

اسکلت `POST_ROW` (تأییدشده؛ فیلدهای صرفاً UI مثل `long_press_action`، `image_top_left_tag`، `layout_type` حذف شده‌اند):

```jsonc
{
  "widget_type": "POST_ROW",
  "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "token": "gapa1FMk",
    "title": "۸۰ متر/۲ خواب/بازسازی شده/صرافهای شمالی",
    "middle_description_text": "۳۵,۰۰۰,۰۰۰,۰۰۰ تومان",
    "bottom_description_text": "مشاور املاک در سعادت‌آباد",   // یا: «۹ ساعت پیش در آبشار تهران (دریاچه)»
    "red_text": "نردبان شده",                                  // اختیاری
    "image_url": "…", "image_count": 8,
    "action": {"payload": {"token": "gapa1FMk", "web_info": {"district_persian": "سعادت‌آباد", "city_persian": "تهران"}}}
  },
  "action_log": {"server_side_info": {"info": {
    "post_token": "gapa1FMk",
    "sort_date": "2026-09-15T14:29:17.323148Z",
    "extra_data": { /* فقط echoی فیلترهای جستجو — نادیده گرفته شود */ }
  }}}
}
```

## ۶. ساختار پاسخ `mapview/viewport` (رد شده — ADR-0006؛ صرفاً مرجع)

> این پاسخ **منبع هیچ فیلد استخراجی نیست** (ADR-0007)؛ فقط برای روزی که قاعده امتیاز جغرافیایی مبتنی بر مختصات لازم شود نگه داشته شده است.

- `posts[]` — به‌ازای هر آگهی:
  - `map_post_card.token`، `title`، `price_fields[]` («قیمت:» و «متری:» به فارسی)، `chips[]`، `images[]`
  - `map_pin_feature.properties`:
    - `subtitle1` — قیمت دقیق با ارقام فارسی و جداکننده: `"۱۴,۶۰۰,۰۰۰,۰۰۰ تومان"`
    - `subtitle2` — `"متری: ۲۶۰,۷۱۴,۲۸۵ تومان"` (دقیق)
    - `subtitle3` — زمان نسبی مثل `"دیروز، شخصی"` یا `"۳ هفته پیش"`
    - `lat/lon` (تقریبی)، `location_type` (`A`/`E`)، `chat_enabled`، `is_verified`
  - `action_log...info.sort_date` — مانند search
- **صفحه‌بندی ندارد**؛ نتیجه محدود به `bbox`/زوم دوربین است.
- `chips[]`: سه آیتم متنی اول «متراژ / اتاق / سن» هستند؛ آیتم‌های بعدی آیکن‌اند (`parking.png`، `elevator.png`، …) — یعنی امکانات ملک از نام فایل آیکن استخراج می‌شود.

## ۷. نگاشت فیلدهای استخراج (فقط از کارت `search` — ADR-0007)

مبنای استخراج **فقط** فیلدهای تأییدشده اسکلت `POST_ROW` (بخش ۵) است. پاسخ `viewport` (بخش ۶) منبع هیچ فیلدی نیست — ارجاع‌های قبلی به `subtitle1/2` و `chips` متعلق به viewportِ ردشده بودند و حذف شدند.

### ۷.۱. فیلدهای نرمال‌شده MVP (از کارت search)

| فیلد نرمال | منبع در `POST_ROW` | استخراج |
|---|---|---|
| `token` | `data.token` | عیناً (کلید یکتا) |
| `title` | `data.title` | متن خام (نرمال‌سازی ی/ك و نیم‌فاصله برای تطبیق) |
| `price` | `data.middle_description_text` مثل «۱۲,۹۰۰,۰۰۰,۰۰۰ تومان» | تبدیل ارقام فارسی/عربی، حذف `,`/`٬`؛ «توافقی» → `null` صریح (بخش ۸) |
| `is_promoted` | `data.red_text == "نردبان شده"` | بولی (اطلاعاتی) — آگهی promoted |
| `district` | `…web_info.district_persian` | متن + نرمال‌سازی |
| `city` | `…web_info.city_persian` | متن |
| `image_count` | `data.image_count` | عدد |
| `sort_date` | `action_log…info.sort_date` | ISO UTC |

`bottom_description_text` به‌عنوان داده خام در `raw_json` (ADR-0001) ذخیره می‌شود؛ heuristic `is_dealer` در فاز بعد روی الگوی دوگانه آن (بخش ۵) کار خواهد کرد — فعلاً خارج از دامنه است.

### ۷.۲. فیلد بافتاری از فیلتر جستجو (نه از داده آگهی)

| فیلد | منبع | semantics |
|---|---|---|
| `rebuilt` | وجود `rebuilt=true` در `form_data` جستجو | `true` برای همه آگهی‌های آن جستجو (تضمین فیلتر سرور)؛ در غیر این صورت **غایب** → قاعده skip. چون در سطح جستجو ثابت است، امتیازدادن به آن بی‌معناست — فقط اطلاعاتی |

### ۷.۳. فیلدهای خارج از دسترس search → فقط post detail

`price_per_square`، `size`، `rooms`، `building_age`، `has_parking`، `has_elevator`، `has_warehouse`، `floor`: با نمونه کامل دوصفحه‌ای (بدون کوکی) **قطعاً در کارت search وجود ندارند** — هر چیزی شبیه آن‌ها در پاسخ صرفاً echoی فیلترهای جستجوست (`extra_data.jli` — بخش ۵). تنها مسیر بازیابی: **post detail** (فاز بعد — طبقه، سند، متن کامل توضیحات و…). تا آن زمان، قواعد امتیاز روی این فیلدها در startup خطا می‌دهند (فیلد ناشناخته — `configuration.md` بخش ۶).

## ۸. قواعد نرمال‌سازی

1. ارقام فارسی/عربی → لاتین (`۰-۹`، `٠-٩`)؛ حذف جداکننده‌های `,` و `٬`؛ ممیز `٫` → `.`
2. `middle_description_text` کارت search مطلق و جداکننده‌دار است («۱۲,۹۰۰,۰۰۰,۰۰۰ تومان»); اگر در نمونه‌های بعدی متن خلاصه با «میلیون/میلیارد» دیده شد → ضرب در ۱e۶/۱e۹.
3. قیمت «توافقی» → مقدار `null` **صریح**؛ متن خالی/فیلد نداشتن → فیلد **غایب**. تفاوت semantics در امتیازدهی: `configuration.md` بخش ۲.
4. `rooms` متنی (یک=۱ … پنج=۵) فقط در فیلتر جستجو معنا دارد؛ از کارت search استخراج نمی‌شود (بخش ۷.۳).
5. `floor` فقط کلید فیلتر است (`-1`=زیر همکف، `0`=همکف)؛ از کارت search استخراج نمی‌شود.
6. دسته‌های اجاره‌ای (رهن/اجاره): **پشتیبانی نمی‌شوند** (تصمیم محصول — خارج از دامنه)؛ ابزار فقط برای دسته‌های فروش طراحی شده است.
7. `sort_date` همیشه UTC ذخیره شود؛ نمایش شمسی فقط در لایه پیام.

## ۹. استراتژی پایش و تشخیص جدید

1. هر poll: درخواست **صفحه اول** با `sort=جدیدترین`.
2. **مرز watermark:** صفحه‌بندی ادامه می‌یابد تا صفحه‌ای که جدیدترین آیتم آن `sort_date < watermark` باشد (آیتم‌های هم‌زمان با watermark همچنان پردازش می‌شوند). تشخیص تکراریِ نهایی همیشه با `token` است — watermark فقط هزینه صفحه‌بندی را محدود می‌کند. شرط توقف دیگر: نبودِ `pagination.has_next_page` (صفحه آخر — تأییدشده، بخش ۵).
3. کلید یکتا: `token` (ایندکس یونیک در SQLite طبق ADR-0001، **سراسری بین جستجوها**)؛ `sort_date` برای watermark و مرتب‌سازی.
4. **سقف صفحات هر poll:** `polling.max_pages_per_poll` (پیش‌فرض ۵)؛ اگر watermark تا سقف پیدا نشد → هشدار لاگ (احتمال از دست رفتن آگهی — فیلتر `recent_ads` آسیب را محدود می‌کند).
5. **poll اول هر جستجو (بدون watermark):** فقط baseline — ثبت seen صفحه اول، ست‌کردن watermark، **بدون نوتیف** (جلوگیری از اسپم آگهی‌های قدیمی).
6. **bump/ویرایش:** token موجود با `sort_date` جدیدتر → به‌روزرسانی رکورد و ثبت رویداد؛ نوتیف مجدد فقط اگر `notify_on_bump: true` (پیش‌فرض `false`).
7. **آگهی مشترک بین چند جستجو (ADR-0007):** اولین جستجویی که token را می‌بیند صاحب نوتیف است (پیام برچسب همان جستجو)؛ جستجوهای بعدی فقط `matched_searches` را تکمیل می‌کنند — بدون نوتیف جدید.
8. پس‌فیلتر جغرافیایی: `district_persian` ∉ `districts` (تطبیق contains نرمال‌شده) یا محله خالی و `allow_unknown_district: false` → آگهی **seen ثبت می‌شود** ولی امتیازدهی/نوتیف نمی‌گیرد (ثبت seen ضروری است چون سرور آن را دوباره برمی‌گرداند).
9. آگهی مانده → نرمال‌سازی → امتیازدهی → در صورت عبور از `min_score` نوتیف.

## ۱۰. نرخ درخواست و پایداری

- Concurrency = ۱ (بدون درخواست موازی — مطابق AGENTS.md).
- حداقل فاصله بین دو درخواست به دیوار: پیش‌فرض `30s`؛ بازه poll هر جستجو: حداقل `5m` + jitter تصادفی.
- Backoff نمایی روی 429/5xx؛ بعد از N خطای متوالی، توقف موقت پایش + لاگ.
- **کشف رفتار rate limit از لاگ اجرا:** هر پاسخ 429/5xx همراه کد وضعیت و هدرهای مرتبط (`Retry-After` و…) لاگ می‌شود تا رفتار واقعی دیوار در حین اجرا مستند و در بخش ۱۱ ثبت شود.
- HTTP 403/جواب غیر JSON → احتمال WAF/تغییر ساختار → هشدار در لاگ.
- **تست snapshot:** پاسخ‌های نمونه `fetch-sample.md` را به‌عنوان fixture نگه دارید؛ اگر دیوار اسکیما را عوض کرد، تست‌ها زودتر از محیط عملیاتی فاش می‌کنند.
- آداپتور `DivarFetcher` تنها نقطه تماس با این API است (بازتعریف‌پذیر طبق معماری).

## ۱۱. موارد باز (نیاز به Capture/تست)

- [ ] **post detail** — راهنمای Capture: در مرورگر تازهِ بدون کوکی یک آگهی را از نتایج باز کنید؛ DevTools → Network → فیلتر Fetch/XHR روی دامنه `api.divar.ir`؛ درخواستی که JSON جزئیات آگهی را برمی‌گرداند (URL معمولاً حاوی token آگهی است) → راست‌کلیک → Copy as fetch → به `fetch-sample.md` اضافه شود (برای طبقه، توضیحات، سند و…)
- [x] ~~مقدار `sort` برای «جدیدترین»~~ — تأییدشده: `sort_date`
- [x] ~~بدنه درخواست صفحه ۲~~ — تأییدشده: echoی عین `pagination.data` پاسخ قبلی (نمونه page 2؛ صفحه آخر هم `has_next_page` ندارد)
- [x] ~~تست بدون کوکی~~ — تأییدشده: هر دو نمونه جدید در مرورگر تازهِ بدون کوکی/لاگین گرفته شده‌اند
- [x] ~~نمونه کامل `POST_ROW`~~ — تأییدشده (صفحات ۱ و ۲)؛ نتیجه: فیلدهای بخش ۷.۳ در کارت search **نیستند** → مسیر بازیابی فقط post detail
- [x] ~~معنی `recent_ads: "1d"`~~ — فقط آگهی‌های ~۲۴ ساعت اخیر؛ برای MVP کافی است (پایش اصلی با watermark)
- [x] ~~`is_dealer` در MVP~~ — خارج از دامنه (تصمیم محصول)؛ الگوی دوگانه `bottom_description_text` در بخش ۵ برای فاز بعد مستند شد
- [x] ~~دسته اجاره‌ای~~ — خارج از دامنه (تصمیم محصول)
- [ ] **رفتار rate limit** — در حین اجرا از لاگ: هر 429/5xx با هدرهای `Retry-After` ثبت و در اینجا مستند می‌شود (بخش ۱۰)
- [ ] **رفتار bump/ویرایش** — دو راه کشف: (۱) پس از پیاده‌سازی، Detector هر token شناخته‌شده با `sort_date` جدیدتر را لاگ می‌کند (داده تجمعی از اجرا)؛ (۲) آزمایش دستی: آگهی آزمایشی خودتان را با جستجوی منطبق پیدا و `sort_date` آن را ثبت کنید، آگهی را ویرایش/نردبان کنید و دوباره بگیرید و مقایسه کنید
- [ ] **جدول نگاشت نام محله → `districts` ID** — فعلاً IDها را کاربر مستقیم در `form_data.districts` تنظیمات می‌گذارد (فیلتر دقیق سرور؛ Capture از DevTools)؛ جدول نگاشت در فازهای بعدی تکمیل می‌شود + نگاشت شهر → `city_id` (تهران=`1`)
- [ ] (اختیاری — فقط اگر `bbox` استفاده شود) تست `bbox` به‌تنهایی بدون `map_state.camera_info`
