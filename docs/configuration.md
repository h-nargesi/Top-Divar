# کانفیگ (Configuration)

> قالب پیشنهادی: **YAML** در `config.yaml` (نسخه‌بندی‌شده در git). همه مقادیر حساس فقط از `.env` (که gitignore است).
> فیلترهای دیوار **عیناً و بدون ترجمه** وارد کانفیگ می‌شوند — مرجع کلیدها: [`divar-api.md`](divar-api.md) بخش ۴.

## ۱. جستجوها (`searches`)

```yaml
searches:
  - id: tehran-apt-40-60          # شناسه یکتا (انگلیسی)
    enabled: true
    interval: 5m                  # بازه poll (حداقل 5m)
    city_ids: ["1"]               # تهران
    place_ids: ["1"]              # user_selected_location (اختیاری)
    sort: sort_date               # «جدیدترین» — تأییدشده (نمونه districts)؛ از طریق server_payload ارسال می‌شود

    # ← دقیقاً همان form_data دیوار؛ pass-through، بدون هیچ ترجمه‌ای
    form_data:
      category: {str: {value: apartment-sell}}
      price: {number_range: {minimum: "10000000000", maximum: "15000000000"}}
      price_per_square: {number_range: {minimum: "256000000", maximum: "300000000"}}
      size: {number_range: {minimum: "40", maximum: "60"}}
      rooms: {repeated_string: {value: ["یک", "دو"]}}
      building-age: {number_range: {minimum: "10", maximum: "15"}}
      floor: {number_range: {minimum: "0", maximum: "8"}}
      elevator: {boolean: {value: true}}
      parking: {boolean: {value: true}}
      warehouse: {boolean: {value: true}}
      rebuilt: {boolean: {value: true}}
    # جغرافیا = allowlist محله‌ها (پس‌فیلتر روی district_persian پاسخ — ADR-0006)
    districts: [شهران, پونک]       # تطبیق contains نرمال‌شده: «شهران» ← «شهران جنوبی/شمالی»
    allow_unknown_district: false  # آگهیِ بدون محله: رد شود (پیش‌فرض)
    # bbox: {repeated_float: {value: [51.239, 35.681, 51.538, 35.771]}}   # اختیاری — پیش‌فیلتر سرور دیوار (pass-through)

    scoring_ref: default          # ارجاع به بلوک scoring (پیش‌فرض: default)
```

قواعد:

- **Pass-through:** `form_data` بایت‌به‌بایت به `search_data.form_data.data` بدنه درخواست تبدیل می‌شود؛ فیلتر جدید دیوار بدون تغییر کد پشتیبانی می‌شود.
- راهنمای پر کردن: در دیوار فیلترها را اعمال کنید → DevTools → درخواست `postlist/w/search` → بدنه → `search_data.form_data.data` → کپی در کانفیگ.
- مقادیر `number_range` در نمونه‌های دیوار رشته‌اند؛ هر دو شکل رشته و عدد پذیرفته می‌شود.
- **جغرافیا با `districts` (ADR-0006):** پس‌فیلتر سمت ما روی `district_persian` پاسخ. تطبیق **contains** روی متن نرمال‌شده است (تبدیل ي/ك عربی به ی/ک فارسی، یکسان‌سازی نیم‌فاصله با فاصله، حذف فاصله‌های اضافی) — پس «نارمک» هر دو «نارمک» و «نارمک جنوبی» را می‌گیرد. آگهی خارج از لیست به‌عنوان **seen** ثبت می‌شود (تا در poll بعدی دوباره پردازش نشود) ولی امتیازدهی/نوتیف نمی‌گیرد.
- `bbox` (اختیاری): اگر گذاشته شود عیناً به سرور دیوار می‌رود (پیش‌فیلتر جغرافیایی سرور) — مفید وقتی ناحیه‌ای بزرگ‌تر از چند محله مدنظر است؛ همیشه همراه `districts` استفاده شود چون مستطیل، محله‌های مجاور را هم می‌گیرد.
- **تداخل با کلید بومی `districts` دیوار:** دیوار خودش فیلتر `districts` با ID عددی محله‌ها دارد (داخل `form_data` — pass-through می‌شود). اگر کاربر آن را مستقیم در `form_data` گذاشت **و** `districts` (نام) در سطح جستجو هم بود → خطای اعتبارسنجی (ابهام). یکی از دو مسیر: نام‌ها در سطح جستجو (پس‌فیلتر، خوانا) یا IDها در `form_data` (سرور، دقیق).
- `recent_ads` (اختیاری، مثل `{"str": {"value": "1d"}}`): پنجره «آگهی‌های اخیر» — مکمل watermark برای سبک‌شدن پاسخ؛ به‌تنهایی کافی نیست (اگر poll طولانی متوقف شود، پنجره ممکن است پرت شود).
- **مسیر ارتقا:** پس از تهیه جدول نگاشت نام محله → district ID، مقادیر `districts` به کلید بومی دیوار ترجمه می‌شوند — کانفیگ کاربر بدون تغییر می‌ماند، فقط سرریز نتایج حذف می‌شود.
- اعتبارسنجی در startup: کلیدهای ناشناخته فقط **هشدار** می‌دهند (نه خطا)، تا فیلترهای جدید دیوار مسدود نشوند؛ کلیدهای معتبرِ غلط‌مقدار (مثلاً `number_range` بدون min/max) خطا می‌دهند.

## ۲. امتیازدهی (`scoring`)

موتور امتیازدهی روی **فیلدهای نرمال‌شده** جدول بخش ۷ `divar-api.md` کار می‌کند (`price`، `price_per_square`، `size`، `rooms`، `building_age`، `has_parking`، `has_elevator`، `is_dealer`، …).

```yaml
scoring:
  default:                        # بلوک پیش‌فرض؛ جستجوها می‌توانند بلوک خودشان را داشته باشند
    min_score: 60                 # ← فقط امتیاز >= این مقدار نوتیف می‌گیرد
    on_missing_field: skip        # skip (پیش‌فرض) | zero
    rules:
      # قاعده ساده: مقایسه + امتیاز ثابت
      - {field: rooms, op: ">=", value: 2, points: 10}
      - {field: has_elevator, op: "==", value: true, points: 5}
      - {field: has_parking, op: "==", value: true, points: 5}
      - {field: building_age, op: "<=", value: 12, points: 10}

      # قاعده پله‌ای: اولین شرط برقرار اعمال می‌شود
      - field: price_per_square
        tiers:
          - {op: "<=", value: 260000000, points: 30}
          - {op: "<=", value: 280000000, points: 15}
          - {op: "<=", value: 300000000, points: 5}

      # جریمه (امتیاز منفی)
      - {field: is_dealer, op: "==", value: true, points: -20}
      - {field: price, op: "==", value: null, points: -10}   # توافقی
```

قواعد موتور:

- عملگرها: `==`، `!=`، `<`، `<=`، `>`، `>=`، `in` (عضویت در لیست).
- `points` می‌تواند منفی باشد (جریمه). امتیاز نهایی = جمع امتیاز همه قواعد برقرار (در tiers فقط پله اول).
- فیلد ناموجود/`null` → کل قاعده `skip` می‌شود (پیش‌فرض) — قیمت «توافقی» آگهی را بی‌دلیل حذف نمی‌کند.
- `score >= min_score` → نوتیف؛ **پیام شامل امتیاز کل و شکست آن است** تا کالیبره‌کردن قواعد ممکن باشد.
- قواعد نسبی (مقایسه با میانگین محله/دسته — «چند بودن») → فاز بعد (backlog)؛ طراحی `value` برای عبارت‌هایی مثل `below_neighborhood_avg: 20%` باز نگه داشته می‌شود.

## ۳. اطلاع‌رسانی (`notify`)

```yaml
notify:
  channels: [telegram]            # ترتیب = اولویت fallback
  telegram:
    chat_id: "123456789"
    # توکن بات فقط از .env → TELEGRAM_BOT_TOKEN
  message:
    fields: [title, price, price_per_square, size, rooms, building_age, district, score, score_breakdown, link]
    link_template: "https://divar.ir/v/{token}"
```

## ۴. پایش و نرخ درخواست (`polling`)

```yaml
polling:
  min_request_interval: 30s       # حداقل فاصله بین هر دو درخواست به دیوار (سراسری)
  default_interval: 5m            # پیش‌فرض جستجوها
  jitter: ±30s
  backoff: exponential            # روی 429/5xx
  max_consecutive_errors: 5       # بعد از آن، توقف موقت + لاگ
```

## ۵. متغیرهای محیطی (`.env`)

```
TELEGRAM_BOT_TOKEN=...            # هرگز commit نمی‌شود
# HTTPS_PROXY=...                 # اگر سرویس داخل ایران است (ADR-0002)
```

## ۶. اعتبارسنجی startup

1. ساختار YAML (schema validation).
2. `id` یکتا؛ `interval >= polling.default_interval` حداقل مجاز.
3. فیلدهای قواعد امتیازدهی ⊆ فیلدهای نرمال‌شده شناخته‌شده (خطا).
4. کلیدهای `form_data` ناشناخته → هشدار (نه خطا).
5. وجود `.env` و مقادیر لازم برای کانال‌های فعال.
