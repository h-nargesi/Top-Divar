# API غیررسمی دیوار (v8)

> مرجع نمونه‌های خام: [`fetch-sample.md`](fetch-sample.md) (گرفته‌شده با DevTools → Copy as fetch).
> این API **غیررسمی و نسخه‌دار** است و بدون اطلاع می‌تواند تغییر کند. پس از هر تغییرِ ساختار، نمونه‌ها را دوباره Capture کنید و این سند را به‌روز کنید.

## ۱. Endpointها

| Endpoint | روش | کاربرد | وضعیت |
|---|---|---|---|
| `https://api.divar.ir/v8/postlist/w/search` | POST | لیست آگهی‌ها + صفحه‌بندی + تشخیص جدید | مستند (نمونه `search page 1/2`) |
| `https://api.divar.ir/v8/posts-v2/web/{token}` | GET | جزئیات یک آگهی (متراژ، ساخت، اتاق، قیمت‌متری، طبقه، امکانات) | **منبع عملیاتی جزئیات** (ADR-0009) — نمونه `## post detail (posts-v2/web)` در `fetch-sample.md` |
| `https://divar.ir/v/{token}` | GET | صفحه HTML آگهی (SSR با `__PRELOADED_STATE__`) | **fallback** اگر JSON در دسترس نبود — نمونه `## fetch` در `fetch-sample.md` |
| `https://api.divar.ir/v8/mapview/viewport` | POST | پین‌های نقشه در ناحیه `bbox` | **رد شده** (ADR-0006) |

تصمیم (ADR-0004 + ADR-0006 + ADR-0009): پایش و تشخیص جدید با `postlist/w/search`؛ جغرافیا با **allowlist محله‌ها** روی `district_persian` پاسخ search (پس‌فیلتر سمت کلاینت — بخش ۵). فیلدهای ملک (متراژ، سال ساخت، اتاق، قیمت‌متری، طبقه، امکانات) از **جزئیات آگهی** می‌آیند چون در کارت search نیستند (بخش ۷.۳). `bbox` پیش‌فیلتر اختیاری سرور است. اگر در آینده قاعده امتیاز جغرافیایی (مثل فاصله تا مترو) لازم شد، `viewport` می‌تواند به‌عنوان Fetcher مکمل برگردد.

کارت search برای فیلدهای کاربر **کافی نیست**. API جایگزین HTML همان `posts-v2/web/{token}` است: بدنهٔ JSON با `sections[].widgets` که با `currentPost.post.sections` داخل HTML یکی است. پارسر روی ویجت کار می‌کند، نه روی DOM. API رسمی کنار (`open-api.divar.ir`، نیاز به کلید `GET_POST`) در MVP استفاده نمی‌شود.

## ۲. هدرهای درخواست

هدرهای حداقلی (هدرهای sentry/trace در نمونه‌ها نویز هستند و لازم نیست):

```
accept: application/json, text/plain, */*
content-type: application/json
referer: https://divar.ir/
user-agent: <رشته User-Agent مرورگر واقعی>
x-web-serving-mode: desktop
```

- **بدون کوکی تأیید شد**: نمونه‌های search و صفحه آگهی در مرورگر تازه بدون کوکی/لاگین Captured شده‌اند (عبارت `credentials: "include"` در snippet صرفاً پیش‌فرض کپی DevTools است). `GET posts-v2/web/{token}` هم بدون کوکی JSON برمی‌گرداند.
- نسخه `v8` را در آداپتور پین کنید؛ تغییر major یعنی هشدار.
- برای جزئیات آگهی همان هدرها کافی‌اند؛ `content-type` در GET لازم نیست.

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
| `districts` | `repeated_string` | `{"repeated_string": {"value": ["198", "399", …]}}` | **فیلتر بومی محله‌ها سمت سرور** با ID عددی. بذر نگاشت از جزئیات: یوسف‌آباد = `90`. پس از تکمیل جدول نام→ID، می‌تواند جایگزین پس‌فیلتر `district_persian` شود (ADR-0006). جدول کامل هنوز باز است (بخش ۱۱) |
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

## ۷. نگاشت فیلدهای استخراج (search + جزئیات — ADR-0007 / ADR-0009)

استخراج **دو مرحله** است. پاسخ `viewport` (بخش ۶) منبع هیچ فیلدی نیست.

1. **کارت search** (`POST_ROW`) — تشخیص جدید، جغرافیا، قیمت کل نمایشی، عنوان.
2. **جزئیات آگهی** (`GET posts-v2/web/{token}`، fallback: HTML) — متراژ، سال ساخت، اتاق، قیمت‌متری، طبقه، امکانات.

پارسر جزئیات روی ویجت‌های `LIST_DATA` با **عنوان فارسی** کار می‌کند (کلید انگلیسی ثابت نیست). شکل JSON و شکل SSR HTML هر دو پذیرفته می‌شوند (بخش ۱۲).

### ۷.۱. فیلدهای نرمال‌شده از کارت search

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

### ۷.۳. فیلدهایی که در search نیستند → جزئیات آگهی

با نمونه کامل دوصفحه‌ای search **قطعاً در کارت `POST_ROW` نیستند**. هر چیزی شبیه آن‌ها داخل `extra_data.jli` فقط echoی فیلتر جستجوست — استخراج per-ad از آنجا ممنوع است.

مسیر بازیابی: `GET /v8/posts-v2/web/{token}` (یا HTML معادل). قواعد امتیاز روی این فیلدها پس از نرمال‌سازی مجازند.

### ۷.۴. فیلدهای نرمال‌شده از جزئیات آگهی (نمونه `gap5-Twe`)

منبع اصلی: بخش `LIST_DATA` — ویجت‌ها با `data.title` فارسی. JSON-LD / `seo.post_seo_schema` فقط fallback است (قیمت، طبقه، سال ساخت و امکانات را ندارد).

| فیلد نرمال | ویجت / مسیر | مقدار نمونه | استخراج |
|---|---|---|---|
| `size` | `GROUP_INFO_ROW` آیتم `متراژ` | `"۹۷"` | عدد |
| `construction_year` | همان، آیتم `ساخت` | `"۱۴۰۳"` | سال شمسی |
| `building_age` | مشتق | `۲` (اگر سال جاری ۱۴۰۵ باشد) | `سال_شمسی_جاری − construction_year` (بخش ۸.۴) |
| `rooms` | همان، آیتم `اتاق` | `"۲"` | عدد صحیح (بخش ۸.۵) |
| `price` | `UNEXPANDABLE_ROW` عنوان `قیمت کل` | `"‏۴۸,۵۰۰,۰۰۰,۰۰۰ تومان"` | تومان؛ سپس آشتی با متری×متراژ (بخش ۸.۶) |
| `price_per_square` | `UNEXPANDABLE_ROW` عنوان `قیمت هر متر` | `"‏۵۰۰,۰۰۰,۰۰۰ تومان"` | تومان بر متر |
| `floor` | `UNEXPANDABLE_ROW` عنوان `طبقه` | `"۵"` یا `"۳ از ۸"` | عدد طبقه؛ `total_floors` اختیاری (بخش ۸.۳) |
| `has_elevator` | `GROUP_FEATURE_ROW` آیتم `آسانسور` | `available: true` | بولی (بخش ۸.۷) |
| `has_parking` | همان، `پارکینگ` | `available: true` | بولی |
| `has_warehouse` | همان، `انباری` | `available: true` | بولی |
| `district` | `seo.web_info.district_persian` | `یوسف‌آباد` | اگر با کارت search فرق داشت، مقدار جزئیات ارجح است |
| `city` | `seo.web_info.city_persian` | `تهران` | متن |
| `token` | `share.web_url` / `webengage.token` | `gap5-Twe` | باید با token جستجو یکی باشد |

`webengage.price` (در نمونه `48499998720`) منبع قیمت **نیست** — ضرب تقریبی متری×متراژ با خطای ممیز است (بخش ۸.۶).

توضیحات متنی (`DESCRIPTION_ROW`) و سند و نقشه در MVP امتیاز نمی‌گیرند؛ در `raw_json` ذخیره می‌شوند.

## ۸. قواعد نرمال‌سازی

### ۸.۱. متن و ارقام

1. ارقام فارسی/عربی → لاتین (`۰-۹`، `٠-٩`)؛ حذف جداکننده‌های `,` و `٬`؛ ممیز `٫` → `.`
2. علامت‌های نامرئی قیمت را دور بریزید: `\u200f` (RLM) و `\u200e` (LRM) در ابتدای «قیمت کل / قیمت هر متر».
3. قیمت «توافقی» → مقدار `null` **صریح**؛ متن خالی/فیلد نداشتن → فیلد **غایب**. تفاوت semantics: `configuration.md` بخش ۲.
4. دسته‌های اجاره‌ای (رهن/اجاره): **پشتیبانی نمی‌شوند** (تصمیم محصول — خارج از دامنه)؛ ابزار فقط برای دسته‌های فروش طراحی شده است.
5. `sort_date` همیشه UTC ذخیره شود؛ نمایش شمسی فقط در لایه پیام.

### ۸.۲. قیمت از کارت search (قبل از جزئیات)

`middle_description_text` مطلق و جداکننده‌دار است («۱۲,۹۰۰,۰۰۰,۰۰۰ تومان»). اگر در نمونه‌های بعدی متن خلاصه با «میلیون/میلیارد» دیده شد → ضرب در ۱e۶/۱e۹. پس از دریافت جزئیات، `price` از «قیمت کل» جزئیات ارجح است و با بخش ۸.۶ آشتی داده می‌شود.

### ۸.۳. طبقه — هر دو شکل

مقدار ویجت `طبقه` ممکن است فقط شماره باشد یا «N از M». هر دو پذیرفته می‌شوند:

| متن (پس از نرمال ارقام) | `floor` | `total_floors` |
|---|---|---|
| `5` / `۵` | `5` | غایب |
| `3 از 8` / `۳از۸` / `3از 8` | `3` | `8` |
| `همکف` | `0` | غایب |
| `زیرهمکف` / `زیر همکف` / `-1` | `-1` | غایب |

فیلتر search همچنان `number_range` با `-1`=زیرهمکف و `0`=همکف است؛ این پارس فقط برای مقدار هر آگهی است. شکل «N از M» در نمونه فعلی نیست ولی پارسر باید آن را از روز اول قبول کند.

### ۸.۴. سال ساخت و عمر بنا

دیوار در جزئیات برچسب **«ساخت»** می‌دهد (سال شمسی)، نه عمر. فیلتر search همچنان `building-age` (عمر به سال) است.

- `construction_year` = عدد سال شمسی از آیتم «ساخت»
- `building_age` = **سال شمسی جاری − `construction_year`** (دقت سال، نه ماه)
- سال جاری از تاریخ سیستم به تقویم شمسی تبدیل می‌شود (کتابخانه تبدیل؛ مرز سال = ۱ فروردین)
- اگر نتیجه منفی بود (داده خراب) → `0` + هشدار لاگ
- اگر «ساخت» غایب بود → هر دو فیلد غایبند

نمونه: ساخت `۱۴۰۳` در شهریور ۱۴۰۵ → عمر `۲`. با متن توضیحات همان آگهی («دو ساله») سازگار است.

### ۸.۵. تعداد اتاق — منبع ارجح

خروجی همیشه عدد صحیح `rooms` است. ترتیب منبع:

1. **اصل:** آیتم `اتاق` در `GROUP_INFO_ROW` (در نمونه `"۲"`)
2. اگر رقم فارسی/لاتین بود → همان عدد
3. اگر کلمه بود → نگاشت فیلتر دیوار: `یک`=۱، `دو`=۲، `سه`=۳، `چهار`=۴، `پنج`=۵ (و «پنج یا بیشتر» اگر دیده شد =۵)
4. **fallback:** `seo.post_seo_schema.numberOfRooms` (در نمونه `"دو"`) با همان نگاشت
5. عنوان آگهی پارس نمی‌شود وقتی یکی از منابع بالا موجود باشد

### ۸.۶. آشتی قیمت کل / قیمت هر متر / متراژ

سه مقدار نمایشی با هم مرتبط‌اند. در نمونه `gap5-Twe`:

- قیمت کل نمایشی = ۴۸٬۵۰۰٬۰۰۰٬۰۰۰
- قیمت هر متر نمایشی = ۵۰۰٬۰۰۰٬۰۰۰
- متراژ = ۹۷
- ۵۰۰٬۰۰۰٬۰۰۰ × ۹۷ = ۴۸٬۵۰۰٬۰۰۰٬۰۰۰ (دقیق)
- `webengage.price` = ۴۸٬۴۹۹٬۹۹۸٬۷۲۰ → ضرب ممیزی؛ **استفاده نشود** وقتی متن نمایشی هست

الگوریتم:

1. `price` و `price_per_square` را از متن «قیمت کل» و «قیمت هر متر» پارس کن (تومان صحیح).
2. `webengage.price` فقط اگر هر دو متن غایب بودند، به‌عنوان آخرین راه، آن هم پس از گرد کردن به میلیون تومان.
3. اگر هر سه (`price`، `pps`، `size`) موجود باشند:
   - `product = pps × size`
   - اگر `|price − product| / max(price, product) ≤ 0.001` **یا** اختلاف مطلق ≤ ۱٬۰۰۰٬۰۰۰ تومان → سازگارند؛ مقادیر نمایشی را نگه دار (در نمونه دقیقاً برابرند).
   - اگر اختلاف بزرگ‌تر بود → هر دو مقدار نمایشی بمانند + هشدار لاگ؛ برای امتیاز کمیابی از `price_per_square` نمایشی استفاده شود نه `price / size`.
4. اگر `price` غایب و `pps` و `size` موجود → `price = pps × size`.
5. اگر `pps` غایب و `price` و `size` موجود → `pps = round(price / size)`.
6. قیمت توافقی (`null`) در این آشتی شرکت نمی‌کند.

### ۸.۷. امکانات (آسانسور / پارکینگ / انباری)

از `GROUP_FEATURE_ROW.items[]` با عنوان فارسی. **هر دو حالت نبودن پشتیبانی می‌شود:**

| وضعیت آیتم | مقدار نرمال |
|---|---|
| موجود و `available: true` | `true` |
| موجود و `available: false` | `false` |
| موجود و کلید `available` نیست | `true` (برچسب آمده یعنی دارد) |
| آیتم در لیست نیست | `false` |

نگاشت عنوان: `آسانسور`→`has_elevator`، `پارکینگ`→`has_parking`، `انباری`→`has_warehouse`.  
مودال «سایر ویژگی‌ها» (`FEATURE_ROW` با `disabled`) منبع ثانویه است؛ اگر `GROUP_FEATURE_ROW` همان عنوان را داشت، آن ارجح است (`disabled: true` → `false`).

## ۹. استراتژی پایش و تشخیص جدید

1. هر poll: درخواست **صفحه اول** با `sort=جدیدترین`.
2. **مرز watermark:** صفحه‌بندی ادامه می‌یابد تا صفحه‌ای که جدیدترین آیتم آن `sort_date < watermark` باشد (آیتم‌های هم‌زمان با watermark همچنان پردازش می‌شوند). تشخیص تکراریِ نهایی همیشه با `token` است — watermark فقط هزینه صفحه‌بندی را محدود می‌کند. شرط توقف دیگر: نبودِ `pagination.has_next_page` (صفحه آخر — تأییدشده، بخش ۵).
3. کلید یکتا: `token` (ایندکس یونیک در SQLite طبق ADR-0001، **سراسری بین جستجوها**)؛ `sort_date` برای watermark و مرتب‌سازی.
4. **سقف صفحات هر poll:** `polling.max_pages_per_poll` (پیش‌فرض ۵)؛ اگر watermark تا سقف پیدا نشد → هشدار لاگ (احتمال از دست رفتن آگهی — فیلتر `recent_ads` آسیب را محدود می‌کند).
5. **poll اول هر جستجو (بدون watermark):** فقط baseline — ثبت seen صفحه اول، ست‌کردن watermark، **بدون نوتیف و بدون درخواست جزئیات** (صرفه‌جویی نرخ؛ جلوگیری از اسپم آگهی‌های قدیمی).
6. پس‌فیلتر جغرافیایی روی کارت search: `district_persian` ∉ `districts` (contains نرمال‌شده) یا محله خالی و `allow_unknown_district: false` → آگهی **seen ثبت می‌شود** ولی جزئیات/امتیاز/نوتیف نمی‌گیرد (ثبت seen ضروری است چون سرور آن را دوباره برمی‌گرداند).
7. **جزئیات (ADR-0009):** برای آگهی **جدید** که از جغرافیا عبور کرده → `GET /v8/posts-v2/web/{token}` (شکست → fallback HTML `https://divar.ir/v/{token}`). این درخواست هم مشمول `min_request_interval` است.
8. نرمال‌سازی (بخش ۸) → امتیازدهی → در صورت عبور از `min_score` نوتیف.
9. **bump/ویرایش:** token موجود با `sort_date` جدیدتر → دوباره جزئیات گرفته می‌شود تا قیمت/فیلدها به‌روز شوند؛ نوتیف مجدد فقط اگر `notify_on_bump: true` (پیش‌فرض `false`).
10. **آگهی مشترک بین چند جستجو (ADR-0007):** اولین جستجویی که token را می‌بیند صاحب نوتیف است (پیام برچسب همان جستجو)؛ جستجوهای بعدی فقط `matched_searches` را تکمیل می‌کنند — بدون نوتیف جدید و بدون درخواست جزئیات تکراری.

## ۱۰. نرخ درخواست و پایداری

- Concurrency = ۱ (بدون درخواست موازی — مطابق AGENTS.md).
- حداقل فاصله بین **هر دو** درخواست به دیوار (search **یا** جزئیات): پیش‌فرض `30s`؛ بازه poll هر جستجو: حداقل `5m` + jitter تصادفی.
- چند آگهی جدید در یک poll یعنی چند GET جزئیات پشت‌سرهم؛ با فاصله ۳۰ثانیه در بودجهٔ زمانی همان poll جا می‌شوند یا به نوبت بعد می‌روند — صف سریال، نه موازی.
- Backoff نمایی روی 429/5xx؛ بعد از N خطای متوالی، توقف موقت پایش + لاگ.
- **کشف رفتار rate limit از لاگ اجرا:** هر پاسخ 429/5xx همراه کد وضعیت و هدرهای مرتبط (`Retry-After` و…) لاگ می‌شود تا رفتار واقعی دیوار در حین اجرا مستند و در بخش ۱۱ ثبت شود.
- HTTP 403 / جواب غیر JSON روی search → احتمال WAF/تغییر ساختار → هشدار در لاگ.
- HTTP 403 / HTML به‌جای JSON روی `posts-v2/web` → تلاش fallback HTML؛ اگر آن هم ویجت نداشت → هشدار + فیلدهای جزئیات غایب (قواعد مربوط `skip`).
- **تست snapshot:** پاسخ‌های نمونه `fetch-sample.md` (search + `posts-v2/web` + صفحه HTML) را به‌عنوان fixture نگه دارید؛ اگر دیوار اسکیما را عوض کرد، تست‌ها زودتر از محیط عملیاتی فاش می‌کنند.
- آداپتور `DivarFetcher` تنها نقطه تماس است: `search()` و `get_post(token)`.

## ۱۱. موارد باز (نیاز به Capture/تست)

- [x] ~~جزئیات آگهی (post detail)~~ — JSON نمونه `GET /v8/posts-v2/web/gap5-Twe` در `fetch-sample.md` بخش `## post detail (posts-v2/web)`؛ HTML معادل در بخش `## fetch` — ADR-0009
- [x] ~~مقدار `sort` برای «جدیدترین»~~ — تأییدشده: `sort_date`
- [x] ~~بدنه درخواست صفحه ۲~~ — تأییدشده: echoی عین `pagination.data` پاسخ قبلی (نمونه page 2؛ صفحه آخر هم `has_next_page` ندارد)
- [x] ~~تست بدون کوکی~~ — تأییدشده: نمونه‌های search و صفحه آگهی بدون کوکی/لاگین
- [x] ~~نمونه کامل `POST_ROW`~~ — تأییدشده؛ فیلدهای بخش ۷.۳ در کارت search **نیستند**
- [x] ~~معنی `recent_ads: "1d"`~~ — فقط آگهی‌های ~۲۴ ساعت اخیر؛ برای MVP کافی است (پایش اصلی با watermark)
- [x] ~~`is_dealer` در MVP~~ — خارج از دامنه (تصمیم محصول)؛ الگوی دوگانه `bottom_description_text` در بخش ۵ برای فاز بعد مستند شد
- [x] ~~دسته اجاره‌ای~~ — خارج از دامنه (تصمیم محصول)
- [ ] **رفتار rate limit** — در حین اجرا از لاگ: هر 429/5xx با هدرهای `Retry-After` ثبت و در اینجا مستند می‌شود (بخش ۱۰)
- [ ] **رفتار bump/ویرایش** — دو راه کشف: (۱) پس از پیاده‌سازی، Detector هر token شناخته‌شده با `sort_date` جدیدتر را لاگ می‌کند (داده تجمعی از اجرا)؛ (۲) آزمایش دستی: آگهی آزمایشی خودتان را با جستجوی منطبق پیدا و `sort_date` آن را ثبت کنید، آگهی را ویرایش/نردبان کنید و دوباره بگیرید و مقایسه کنید
- [ ] **جدول نگاشت نام محله → `districts` ID** — بذر: یوسف‌آباد = `90`. فعلاً بقیه IDها را کاربر مستقیم در `form_data.districts` می‌گذارد (فیلتر دقیق سرور؛ Capture از DevTools)؛ جدول کامل فاز بعد + نگاشت شهر → `city_id` (تهران=`1`)
- [ ] نمونه آگهی **بدون** پارکینگ/آسانسور/انباری (`available: false` یا آیتم غایب) برای تثبیت بخش ۸.۷
- [ ] نمونه طبقه به شکل «N از M»
- [ ] (اختیاری — فقط اگر `bbox` استفاده شود) تست `bbox` به‌تنهایی بدون `map_state.camera_info`

## ۱۲. ساختار جزئیات آگهی (`posts-v2/web` و HTML معادل)

### ۱۲.۱. منبع عملیاتی در برابر fallback

| منبع | شکل | کی |
|---|---|---|
| `GET https://api.divar.ir/v8/posts-v2/web/{token}` | JSON: `sections[]` با `section_name` + `widgets[]` | **اصل** — نمونه خام: `fetch-sample.md` بخش `## post detail (posts-v2/web)` |
| `GET https://divar.ir/v/{token}` | HTML SSR → `window.__PRELOADED_STATE__.currentPost.post` | fallback؛ نمونه خام: `fetch-sample.md` بخش `## fetch` |

کارت search فیلدهای کاربر را ندارد؛ این JSON جایگزین HTML است. API رسمی کنار (`open-api.divar.ir/v1/open-platform/finder/post/{token}`) کلید `GET_POST` می‌خواهد و در MVP نیست.

پارس **جدول HTML / کلاس CSS نیست**. هر دو منبع به لیست `{widget_type, data}` نرمال می‌شوند، بعد با عنوان فارسی استخراج می‌شوند.

### ۱۲.۲. دو شکل ورودی — هر دو را قبول کن

**JSON API** (آرایهٔ بخش‌ها):

```jsonc
{
  "sections": [
    {
      "section_name": "LIST_DATA",
      "widgets": [
        { "widget_type": "GROUP_INFO_ROW", "data": { /* … */ } }
      ]
    }
  ],
  "seo": { "web_info": { "district_persian": "یوسف‌آباد", "city_persian": "تهران" } },
  "share": { "web_url": "https://divar.ir/v/gap5-Twe" },
  "webengage": { "token": "gap5-Twe", "price": 48499998720 }  // قیمت را از اینجا نخوان
}
```

**HTML SSR** (آبجکت کلیددار + غلاف `dto`):

```jsonc
currentPost.post.sections.LIST_DATA[].dto  // { widget_type, data }
currentPost.post.seo.webInfo               // district_persian, city_persian
```

نرمال‌سازی شکل: اگر `sections` آرایه بود از `section_name == "LIST_DATA"` و `widgets` بخوان؛ اگر آبجکت بود از `sections.LIST_DATA` و برای هر آیتم `dto ?? خود آیتم` را بردار.

### ۱۲.۳. اسکلت `LIST_DATA` (تأییدشده با `gap5-Twe`)

```jsonc
{
  "widget_type": "GROUP_INFO_ROW",
  "data": {
    "items": [
      { "title": "متراژ", "value": "۹۷" },
      { "title": "ساخت", "value": "۱۴۰۳" },
      { "title": "اتاق", "value": "۲" }
    ]
  }
}
// سپس چند UNEXPANDABLE_ROW:
//   "تصویر‌ها برای همین ملک است؟" / "خیر"   — اطلاعاتی، امتیاز ندارد
//   "قیمت کل" / "‏۴۸,۵۰۰,۰۰۰,۰۰۰ تومان"
//   "قیمت هر متر" / "‏۵۰۰,۰۰۰,۰۰۰ تومان"
//   "طبقه" / "۵"
{
  "widget_type": "GROUP_FEATURE_ROW",
  "data": {
    "items": [
      { "title": "آسانسور", "available": true },
      { "title": "پارکینگ", "available": true },
      { "title": "انباری", "available": true }
    ]
  }
}
```

`seo.post_seo_schema` (و JSON-LD صفحه) فقط `floorSize`، `numberOfRooms` و محله را دارد — قیمت، طبقه، سال ساخت و امکانات را ندارد؛ fallback محدود بخش ۸.۵ / `size`.

### ۱۲.۴. هدرهای GET جزئیات

همان مجموعهٔ حداقلی بخش ۲، به‌اضافه `referer: https://divar.ir/` و `accept: application/json`. بدون کوکی تأیید شد.
