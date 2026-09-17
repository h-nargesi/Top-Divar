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

    scoring_ref: default          # ارجاع به بلوک scoring (پیش‌فرض: default)
```

قواعد:

- **Pass-through:** `form_data` بایت‌به‌بایت به `search_data.form_data.data` بدنه درخواست تبدیل می‌شود؛ فیلتر جدید دیوار بدون تغییر کد پشتیبانی می‌شود.
- راهنمای پر کردن: در دیوار فیلترها را اعمال کنید → DevTools → درخواست `postlist/w/search` → بدنه → `search_data.form_data.data` → کپی در کانفیگ.
- مقادیر `number_range` در نمونه‌های دیوار رشته‌اند؛ هر دو شکل رشته و عدد پذیرفته می‌شود.
- **جغرافیا با `districts` (ADR-0006):** پس‌فیلتر سمت ما روی `district_persian` پاسخ. تطبیق **contains** روی متن نرمال‌شده است (تبدیل ي/ك عربی به ی/ک فارسی، یکسان‌سازی نیم‌فاصله با فاصله، حذف فاصله‌های اضافی) — پس «نارمک» هر دو «نارمک» و «نارمک جنوبی» را می‌گیرد. آگهی خارج از لیست به‌عنوان **seen** ثبت می‌شود (تا در poll بعدی دوباره پردازش نشود) ولی امتیازدهی/نوتیف نمی‌گیرد.
- **تداخل با کلید بومی `districts` دیوار:** دیوار خودش فیلتر `districts` با ID عددی محله‌ها دارد (داخل `form_data` — pass-through می‌شود). اگر **کاربر خودش** IDها را مستقیم در `form_data.districts` بگذارد **و** هم‌زمان `districts` (نام) در سطح جستجو هم باشد → خطای اعتبارسنجی (ابهام). (تزریق خودکار IDها از جدول نگاشت — بند بعد — تداخل نیست.)
- `recent_ads` (اختیاری، مثل `{"str": {"value": "1d"}}`): پنجره «آگهی‌های اخیر» — مکمل watermark برای سبک‌شدن پاسخ؛ به‌تنهایی کافی نیست (اگر poll طولانی متوقف شود، پنجره ممکن است پرت شود).
- **جدول نگاشت نام محله → district ID (خودکار + دستی — ADR-0006):** IDها را کاربر می‌تواند مستقیم در `form_data.districts` بگذارد (Capture از DevTools — فیلتر دقیق سمت سرور) یا با دستور CLI `district add` وارد کند؛ به‌علاوه هر `get_post` موفق، نگاشت `district_persian → ID` را خودکار از `seo.bread_crumb` در جدول SQLite `district_id_map` ثبت می‌کند (تقدم `manual` > `auto`؛ بذرها: یوسف‌آباد = `90`، هروی = `1024`؛ جزئیات برداشت: `divar-api.md` بخش ۱۲.۵). در ساخت بدنهٔ درخواست، نام‌های `districts` که نگاشت دارند به `form_data.districts` تزریق (merge) می‌شوند و بقیه نام‌ها با پس‌فیلتر `district_persian` می‌مانند؛ کانفیگ نام‌محور بدون تغییر است.
- اعتبارسنجی در startup: کلیدهای ناشناخته فقط **هشدار** می‌دهند (نه خطا)، تا فیلترهای جدید دیوار مسدود نشوند؛ کلیدهای معتبرِ غلط‌مقدار (مثلاً `number_range` بدون min/max) خطا می‌دهند.

## ۲. امتیازدهی (`scoring`)

موتور امتیازدهی روی **فیلدهای نرمال‌شده جدول بخش ۷ `divar-api.md`** کار می‌کند — کارت search به‌علاوه جزئیات آگهی (ADR-0009): `price`، `price_per_square`، `size`، `rooms`، `construction_year`، `building_age`، `floor`، `has_parking`، `has_elevator`، `has_warehouse`، `district`، `city`، `title`، `is_promoted`.

```yaml
scoring:
  default:                        # بلوک پیش‌فرض؛ جستجوها می‌توانند بلوک خودشان را داشته باشند
    min_score: 60                 # ← فقط امتیاز >= این مقدار نوتیف می‌گیرد
    on_missing_field: skip        # skip (پیش‌فرض) | zero
    rules:
      # قاعده پله‌ای روی قیمت کل
      - field: price
        tiers:
          - {op: "<=", value: 12000000000, points: 30}
          - {op: "<=", value: 13500000000, points: 15}
          - {op: "<=", value: 15000000000, points: 5}

      # قیمت هر متر (پس از آشتی با متراژ — divar-api.md بخش ۸.۶)
      - field: price_per_square
        tiers:
          - {op: "<=", value: 280000000, points: 20}
          - {op: "<=", value: 350000000, points: 10}

      # عمر بنا = سال شمسی جاری − سال ساخت
      - field: building_age
        tiers:
          - {op: "<=", value: 5, points: 15}
          - {op: "<=", value: 15, points: 5}

      - {field: has_parking, op: "==", value: true, points: 5}
      - {field: has_elevator, op: "==", value: true, points: 5}
      - {field: rooms, op: ">=", value: 2, points: 5}

      # محله (تطبیق contains نرمال‌شده با هر عنصر لیست)
      - {field: district, op: contains_any, value: [نارمک, پونک, شهران], points: 10}

      # کلمات کلیدی عنوان (جریمه)
      - {field: title, op: contains_any, value: [سرمایه‌گذاری, کلید نخورده], points: -10}

      # جریمه (امتیاز منفی)
      - {field: price, op: "==", value: null, points: -10}   # توافقی (null صریح)
      - {field: is_promoted, op: "==", value: true, points: -5}   # نردبان شده (اختیاری)
```

قواعد موتور:

- عملگرها: `==`، `!=`، `<`، `<=`، `>`، `>=`، `in` (عضویت دقیق در لیست)، `contains_any` (حداقل یکی از عناصر لیست در متن نرمال‌شده باشد — برای `title`/`district`).
- فیلدهای مجاز: از کارت search — `price`، `district`، `city`، `title`، `is_promoted`؛ از جزئیات — `price_per_square`، `size`، `rooms`، `construction_year`، `building_age`، `floor`، `total_floors`، `has_parking`، `has_elevator`، `has_warehouse` (`divar-api.md` بخش ۷.۱ و ۷.۴). `rebuilt` فقط بافت جستجو (بخش ۷.۲). `is_dealer` خارج از دامنه است.
- **غایب در برابر null:** فیلد **غایب** (منبع ندارد) → کل قاعده `skip` (یا `zero` مطابق `on_missing_field`)؛ فیلد با مقدار **null صریح** (مثل قیمت «توافقی») → فقط `== null`/`!= null` ارزیابی می‌شود و قواعد عددی `skip` می‌شوند — قیمت توافقی آگهی را حذف نمی‌کند ولی جریمه می‌گیرد.
- `points` می‌تواند منفی باشد (جریمه). امتیاز نهایی = جمع امتیاز همه قواعد برقرار (در tiers فقط پله اول).
- `score >= min_score` → نوتیف؛ **پیام شامل امتیاز کل و شکست آن است** تا کالیبره‌کردن قواعد ممکن باشد.
- قواعد نسبی کمیابی → فاز بعد (backlog). معیار مصوب: **درصد/صدک زیر میانهٔ قیمت‌متری همتای غلتان** + `robust_z` (ADR-0008). عبارت قدیمی `below_neighborhood_avg` کنار گذاشته شد (مرجع میانگین نیست). پیش‌نیاز `size` / `price_per_square` از جزئیات تأمین شده؛ خود بلوک `relative` هنوز فعال نمی‌شود. قالب کانفیگ (شامل باند متراژ ±۲۰٪ با کف `min_size_band_width_m: 7.5`، جدول مجاورت `neighbor_map` و قاعدهٔ `robust_z_lte`)، تعریف همتا، پنجرهٔ زمانی و شکست امتیاز: [`deal-scoring.md`](deal-scoring.md) بخش‌های ۴، ۶ و ۹.

## ۳. اطلاع‌رسانی (`notify`)

```yaml
notify:
  channels: [telegram]            # ترتیب = اولویت fallback
  telegram:
    chat_id: "123456789"
    # توکن بات فقط از .env → TELEGRAM_BOT_TOKEN
    message:
      fields: [title, price, price_per_square, size, rooms, construction_year, building_age, floor, has_parking, has_elevator, has_warehouse, district, city, published_at, score, score_breakdown, link]
      link_template: "https://divar.ir/v/{token}"
      # published_at = زمان انتشار اولیهٔ آگهی در دیوار — از جزئیات آگهی (divar-api.md بخش ۷.۴)؛
      # سطر غایب در ویجت → فیلد غایب → آن فیلد از پیام حذف می‌شود (نمایش شمسی طبق بخش ۸.۱)
    # فاز نسبی: score_breakdown شامل cohort_median_pps، discount_pct، percentile، robust_z
    # (docs/deal-scoring.md بخش ۶). نمایش دلار در پیام ساخته نمی‌شود (ADR-0008).
```

## ۴. پایش و نرخ درخواست (`polling`)

```yaml
polling:
  search_min_interval: 30s        # حداقل فاصله بین دو درخواست search (مستقل)
  detail_min_interval: 30s        # حداقل فاصله بین دو درخواست جزئیات (مستقل)
  # رفتار واقعی rate limit دادهٔ رسمی ندارد و در اجرا کشف می‌شود → هر دو مقدار قابل ویرایش؛
  # اجرا همچنان یک صف سریال واحد است (concurrency = ۱)
  default_interval: 5m            # پیش‌فرض جستجوها
  jitter: ±30s
  backoff: exponential            # روی 429/5xx
  max_consecutive_errors: 5       # بعد از آن، توقف موقت + لاگ
  max_pages_per_poll: 5           # سقف صفحه‌بندی هر poll (divar-api.md بخش ۹)
  notify_on_bump: false           # آگهی bumpشده (token موجود + sort_date جدید) دوباره نوتیف نشود
  fetch_post_detail: true         # GET posts-v2/web برای آگهی جدید پس از جغرافیا (ADR-0009)
```

## ۵. متغیرهای محیطی (`.env`)

```
TELEGRAM_BOT_TOKEN=...            # هرگز commit نمی‌شود
# HTTPS_PROXY=...                 # اگر سرویس داخل ایران است (ADR-0002)
```

## ۶. اعتبارسنجی startup

1. ساختار YAML (schema validation).
2. `id` یکتا؛ `interval >= polling.default_interval` حداقل مجاز.
3. فیلدهای قواعد امتیازدهی ⊆ فیلدهای نرمال‌شده شناخته‌شده (`divar-api.md` بخش ۷.۱ / ۷.۲ / ۷.۴) (خطا).
4. کلیدهای `form_data` ناشناخته → هشدار (نه خطا).
5. وجود `.env` و مقادیر لازم برای کانال‌های فعال.
6. `polling.search_min_interval` یا `polling.detail_min_interval` کمتر از `5s` → هشدار (خطا نیست).
