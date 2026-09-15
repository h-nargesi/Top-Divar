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

- نمونه‌ها با `credentials: "include"` (کوکی) ثبت شده‌اند؛ فرض اولیه: **بدون کوکی هم جواب می‌دهد** — باید تست شود (موارد باز).
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
| `recent_ads` | `str` | `{"str": {"value": "1d"}}` | «آگهی‌های اخیر» — پنجره زمانی (نمونه: ۱ روز). برای poll مکمل watermark است؛ مقادیر دیگر پنجره باید Capture شود |
| `bbox` | `repeated_float` | `[minLon, minLat, maxLon, maxLat]` | پیش‌فیلتر اختیاری سرور؛ جغرافیای اصلی با allowlist محله‌ها است (ADR-0006) |

تایپ‌های مقدار: `str`، `number_range` (min/max به‌صورت رشته)، `boolean`، `repeated_string`، `repeated_float`. هر کلید جدیدی که دیوار اضافه کند، بدون تغییر کد از کانفیگ عبور داده می‌شود.

## ۵. ساختار پاسخ `postlist/w/search`

موارد مهم (بقیه برای UI وب‌سایت است و نادیده گرفته می‌شود):

- `list_widgets[]` با `widget_type: "POST_ROW"` — به‌ازای هر آگهی:
  - `data.token` — کلید یکتای آگهی (همان `divar_token` در Storage)
  - `data.title`، `data.image_url`، `data.image_count`
  - `data.middle_description_text` — قیمت فرمت‌شده، مثلاً `"۱۲,۹۰۰,۰۰۰,۰۰۰ تومان"`
  - `data.bottom_description_text` — نام کسب‌وکار/مشاور + محله (مثل «گروه بزرگ شهرِ ملک در نارمک جنوبی») — **نشانه واسطه/آژانس**
  - `data.action.payload.web_info.district_persian` / `city_persian` — محله/شهر — **کلید فیلتر جغرافیایی** (ADR-0006). در نمونه ۲۴/۲۴ آگهی حاضر بود با مقادیر تمیز سطح محله («شهران جنوبی»، «نارمک»، …)؛ تطبیق باید **contains نرمال‌شده** باشد چون «نارمک» و «نارمک جنوبی» هر دو به‌صورت مستقل می‌آیند.
- `action_log.server_side_info.info.sort_date` — زمان ISO (UTC) مثل `"2026-09-15T13:29:15.982140Z"` — **کلید اصلی مرتب‌سازی و watermark پایش**
- `pagination`:
  - `has_next_page` — ممکن است در پاسخ بدون‌نتیجه نباشد (اختیاری تلقی شود)
  - `data.page`، `data.last_post_date`، `data.search_uid`، `data.viewed_tokens` (فشرده)، `filters_hash` — **تأییدشده**: همین آبجکت عیناً به‌عنوان `pagination_data` در درخواست صفحه بعد برمی‌گردد
- پاسخ ممکن است **خالی** باشد: بدون `list_widgets`، با `show_no_search_result_notice: true` و `last_post_date` صفر (`0001-01-01T00:00:00Z`) — طبیعی است، خطا نیست

اسکلت مینیمال `POST_ROW` (مرجع نگاشت فیلدها؛ نمونه خام در `fetch-sample.md` حذف شده):

```jsonc
{
  "widget_type": "POST_ROW",
  "data": {
    "token": "gapikIpY",
    "title": "۵۰ متر فول امکانات در نارمک *مناسب سرمایه گذاری*",
    "middle_description_text": "۱۲,۹۰۰,۰۰۰,۰۰۰ تومان",
    "bottom_description_text": "گروه بزرگ شهرِ ملک در نارمک جنوبی",
    "image_url": "…", "image_count": 1,
    "action": {"payload": {"web_info": {"district_persian": "نارمک جنوبی", "city_persian": "تهران"}}},
    "action_log": {"server_side_info": {"info": {"sort_date": "2026-09-15T13:29:15.982140Z"}}}
  }
}
```

## ۶. ساختار پاسخ `mapview/viewport` (رد شده — ADR-0006؛ صرفاً مرجع)

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

## ۷. نگاشت فیلدهای امتیازدهی (بدون درخواست اضافه)

داده کارت (هر دو endpoint) برای این فیلدهای نرمال‌شده کافی است و **در MVP نیازی به post detail نیست**:

| فیلد نرمال | منبع | استخراج |
|---|---|---|
| `price` | `subtitle1` یا `middle_description_text` | تبدیل ارقام فارسی، حذف `,` |
| `price_per_square` | `subtitle2` یا `price_fields` | همان بالا |
| `size` | `chips[0]` مثل «۵۶ متر» | پارس عدد |
| `rooms` | `chips[1]` مثل «۱ اتاق» | عدد |
| `building_age` | `chips[2]` مثل «۱۱ سال» | عدد |
| `has_parking` | chip با آیکن `parking.png` | بولی |
| `has_elevator` | chip با آیکن `elevator.png` | بولی |
| `has_warehouse` | chip با آیکن `warehouse.png` (احتمالی) | بولی — **تأیید نشده** (در نمونه، فیلتر warehouse=true بود) |
| `rebuilt` | از وجود فیلتر در جستجو یا post detail | در MVP فقط اگر فیلتر شده باشد |
| `is_dealer` (مشتق) | `bottom_description_text` (نام مشاور/آژانس) | heuristic؛ **نیاز به نمونه‌های بیشتر** |
| `district` | `district_persian` | متنی |
| `sort_date` | `action_log…info.sort_date` | ISO UTC |
| `token` | `token` | کلید یکتا |

فیلدهایی که فقط از post detail می‌آیند (طبقه، تعداد واحد، جهت، متن کامل توضیحات برای کلمات ممنوعه) → فاز بعد.

## ۸. قواعد نرمال‌سازی

1. ارقام فارسی/عربی → لاتین (`۰-۹`، `٠-٩`)؛ حذف جداکننده‌های `,` و `٬`؛ ممیز `٫` → `.`
2. واحدهای «میلیون»/«میلیارد» در متن‌های خلاصه → ضرب در ۱e۶/۱e۹ (مقادیر `subtitle1/2` از قبل مطلق‌اند).
3. `rooms` متنی: یک=۱، دو=۲، سه=۳، چهار=۴، پنج=۵ (فیلتر و chip هر دو ممکن است متنی باشند).
4. `floor`: `-1`=زیر همکف، `0`=همکف.
5. قیمت «توافقی» یا خالی → `null` → قواعد وابسته `skip` می‌شوند (سیاست `on_missing_field`).
6. `sort_date` همیشه UTC ذخیره شود؛ نمایش شمسی فقط در لایه پیام.

## ۹. استراتژی پایش و تشخیص جدید

1. هر poll: درخواست **صفحه اول** با `sort=جدیدترین`.
2. پیمایش نتایج تا رسیدن به `sort_date` رکورد آخرین poll موفق قبلی (watermark) — بعد از آن، بقیه تکراری‌اند.
3. کلید یکتا: `token` (ایندکس یونیک در SQLite طبق ADR-0001)؛ `sort_date` برای watermark و مرتب‌سازی.
4. پس‌فیلتر جغرافیایی: `district_persian` ∉ `districts` (تطبیق contains نرمال‌شده) یا محله خالی و `allow_unknown_district: false` → آگهی **seen ثبت می‌شود** ولی امتیازدهی/نوتیف نمی‌گیرد (ثبت seen ضروری است چون سرور آن را دوباره برمی‌گرداند).
5. آگهی مانده → نرمال‌سازی → امتیازدهی → در صورت عبور از `min_score` نوتیف.

## ۱۰. نرخ درخواست و پایداری

- Concurrency = ۱ (بدون درخواست موازی — مطابق AGENTS.md).
- حداقل فاصله بین دو درخواست به دیوار: پیش‌فرض `30s`؛ بازه poll هر جستجو: حداقل `5m` + jitter تصادفی.
- Backoff نمایی روی 429/5xx؛ بعد از N خطای متوالی، توقف موقت پایش + لاگ.
- HTTP 403/جواب غیر JSON → احتمال WAF/تغییر ساختار → هشدار در لاگ.
- **تست snapshot:** پاسخ‌های نمونه `fetch-sample.md` را به‌عنوان fixture نگه دارید؛ اگر دیوار اسکیما را عوض کرد، تست‌ها زودتر از محیط عملیاتی فاش می‌کنند.
- آداپتور `DivarFetcher` تنها نقطه تماس با این API است (بازتعریف‌پذیر طبق معماری).

## ۱۱. موارد باز (نیاز به Capture/تست)

- [ ] **post detail** — باز کردن یک آگهی در مرورگر و گرفتن درخواست جزئیات (برای طبقه، توضیحات، سند و…)
- [x] ~~مقدار `sort` برای «جدیدترین»~~ — تأییدشده: `sort_date` (نمونه districts)
- [x] ~~بدنه درخواست صفحه ۲~~ — تأییدشده: echoی `pagination.data` پاسخ قبلی (نمونه districts)
- [ ] **جدول نگاشت نام محله → `districts` ID** (برای ارتقای ADR-0006 به فیلتر بومی سرور؛ IDهای دیده‌شده: 198, 399, 40, 654, 75, 907, 929, 992) + نگاشت شهر → `city_id` (تهران=`1`)
- [ ] مقادیر دیگر پنجره `recent_ads` (نمونه فقط `1d`)
- [ ] (اختیاری — فقط اگر `bbox` استفاده شود) تست `bbox` به‌تنهایی بدون `map_state.camera_info`
- [ ] تست درخواست بدون کوکی/احراز هویت
- [ ] رفتار دقیق rate limit (کد وضعیت، هدرهای Retry-After)
- [ ] تأیید آیکن `warehouse.png` و قاعده قطعی `is_dealer` با نمونه‌های متنوع
- [ ] یک نمونه `POST_ROW` کامل دوباره به `fetch-sample.md` اضافه شود (نمونه قبلی حذف شده؛ اسکلت در بخش ۵ همین سند هست)
