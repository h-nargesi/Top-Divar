# کانفیگ (Configuration)

> قالب پیشنهادی: **YAML** در `config.yaml` (نسخه‌بندی‌شده در git). همه مقادیر حساس فقط از `.env` (که gitignore است).
> فیلترهای دیوار **عیناً و بدون ترجمه** وارد کانفیگ می‌شوند — مرجع کلیدها: [`divar-api.md`](divar-api.md) بخش ۴.

## ۱. جستجوها (`searches`)

```yaml
searches:
  - id: tehran-apt-40-60          # شناسه یکتا (انگلیسی)
    label: آپارتمان تهران          # برچسب فارسی برای نمایش در پیام (اختیاری؛ غایب → همان id)
    enabled: true
    interval: 5m                  # بازه poll (کف: polling.min_interval — پیش‌فرض 5m)
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

    scoring_ref: default          # ارجاع به بلوک scoring (پیش‌فرض: default؛ بلوک ناموجود = خطای startup — بخش ۷)
```

قواعد:

- **Pass-through:** `form_data` بایت‌به‌بایت به `search_data.form_data.data` بدنه درخواست تبدیل می‌شود؛ فیلتر جدید دیوار بدون تغییر کد پشتیبانی می‌شود.
- **`label` (اختیاری):** برچسب فارسی جستجو که در خط اول پیام اطلاع‌رسانی می‌آید؛ غایب → همان `id` نمایش داده می‌شود. برچسب آگهیِ مشترک بین چند جستجو = اولین جستجوی مچ‌شده (ADR-0007؛ قالب پیام: بخش ۳).
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
- قواعد نسبی کمیابی → فاز بعد (backlog). معیار مصوب: **درصد/صدک زیر میانهٔ قیمت‌متری مؤثر همتای غلتان** (`pps_eff` — متراژ مؤثر) + `robust_z` (ADR-0008). عبارت قدیمی `below_neighborhood_avg` کنار گذاشته شد (مرجع میانگین نیست). پیش‌نیاز `size` / `price_per_square` از جزئیات تأمین شده؛ خود بلوک `relative` هنوز فعال نمی‌شود. قالب کانفیگ (شامل باند متراژ ±۲۰٪ با کف `min_size_band_width_m: 7.5`، باند سن نسبی `age_band_years`، متراژ مؤثر با نقشهٔ `amenity_eq_m` و فرمول آسانسور `elevator_eq_per_floor` / `elevator_eq_cap`، جدول مجاورت `neighbor_map` و قاعدهٔ `robust_z_lte`)، تعریف همتا، پنجرهٔ زمانی و شکست امتیاز: [`deal-scoring.md`](deal-scoring.md) بخش‌های ۴، ۶ و ۹. purge مرتبط از بلوک `history` (بخش ۵) مشتق می‌شود.

## ۳. اطلاع‌رسانی (`notify`)

کانال‌های MVP: **تلگرام + ایمیل** — مستقل، بدون زنجیرهٔ fallback (ADR-0002). مدل گیرنده‌ها: **پخش عمومی (broadcast)** — همهٔ کاربران تلگرامِ ثبت‌شده و همهٔ گیرنده‌های ایمیلِ کانفیگ، همهٔ آگهی‌های ممتاز را می‌گیرند؛ فیلتر per-user وجود ندارد (ADR-0010).

```yaml
notify:
  channels: [telegram, email]     # کانال‌های فعال؛ مستقل — ترتیب معنای fallback ندارد (ADR-0002)
  retry_interval: 30m             # سویپ دوره‌ای ردیف‌های pending تا موفقیت/purge (ADR-0010 اصلاح ۲۰۲۶-۰۹-۱۷)
  telegram:
    backfill_days: 7              # سقف پنجرهٔ جبران pendingهای هر کاربر (≤ 30 — ADR-0010)
    # توکن بات → .env: TELEGRAM_BOT_TOKEN؛ پسورد ثبت‌نام → .env: TELEGRAM_BOT_PASSWORD
  email:
    smtp:
      host: smtp.example.com
      port: 587
      encryption: starttls        # starttls (پیش‌فرض) | tls (465) | none (آزمایش محلی → هشدار بخش ۷)
      username: bot@example.com
      password_env: SMTP_PASSWORD # نام متغیر محیطی؛ خود رمز فقط در .env
      from: "Top Divar <bot@example.com>"
    to:                           # گیرنده‌ها فقط از کانفیگ؛ هر گیرنده = یک ردیف delivery مستقل
      - user1@example.com
      - user2@example.com
```

### ۳.۱. ثبت‌نام و دستورات بات

`chat_id` در کانفیگ **وجود ندارد**؛ کاربران از طریق خود بات ثبت‌نام می‌کنند (ADR-0010):

1. ساخت بات با BotFather → توکن در `.env: TELEGRAM_BOT_TOKEN`
2. کاربر `/start` را می‌فرستد
3. بات پسورد مشترک را می‌پرسد (`.env: TELEGRAM_BOT_PASSWORD`) — تلاش ناموفق → پیام خطا + لاگ
4. کاربر یک **username یونیک** انتخاب می‌کند (تکراری → پیام خطا و انتخاب دوباره)
5. `chat_id` به‌صورت خودکار در دیتابیس (جدول `users`) به کاربر وصل می‌شود

**دستورات بات (فقط همین‌ها — مصوب ۲۰۲۶-۰۹-۱۷):**

| دستور | کار |
|---|---|
| `/start` | شروع/ادامهٔ ثبت‌نام؛ از کاربرِ ثبت‌شده، محرک جبران `pending`ها (ADR-0010) |
| `/resend YYYY/MM/DD` | ارسال مجدد از تاریخ شمسی (مثل `/resend 1405/06/01`)؛ فقط به همین کاربر؛ سقف ۳۰ روز؛ فرمت دیگر → پیام راهنما |
| `/help` | فهرست همین دستورات |
| `/status` | نام کاربری و تعداد `pending`های او |

**ماشین حالت ثبت‌نام (مصوب ۲۰۲۶-۰۹-۱۷):**

- وضعیت گفتگو (انتظار پسورد / انتظار username) **فقط در حافظهٔ پروسه** با تایم‌اوت **۱۰ دقیقه**؛ ری‌استارت سرویس گفتگوی نیمه‌کاره را می‌اندازد — کاربر دوباره `/start` می‌زند (ذخیرهٔ state در دیتابیس لازم نیست).
- پسورد: حداکثر **۵ تلاش ناموفق در ۱۰ دقیقه** به‌ازای هر chat → بیشتر از آن **بلاک موقت ۳۰ دقیقه** + لاگ هشدار.
- username: `^[a-z0-9_]{3,30}$` (حروف کوچک انگلیسی، رقم و `_`؛ ۳ تا ۳۰ کاراکتر)؛ یونیک بودن case-insensitive؛ نامعتبر/تکراری → پیام خطا و تکرار.
- هر پیام متنی کاربرِ ثبت‌شده (نه فقط دستورها) محرک جبران است (ADR-0010).

### ۳.۲. قالب پیام تلگرام (مصوب ۲۰۲۶-۰۹-۱۷)

- ارسال با Bot API مستقیم: `POST api.telegram.org/bot<TOKEN>/sendMessage` با `chat_id`, `text`, `parse_mode=HTML` (ADR-0002)؛ بدون وابستگی اجباری به کتابخانه — پس از تصمیم پشته ممکن است کتابخانهٔ سبک بیاید. خطاهای معتبر: 429 / 403 / 400.
- **همیشه تک‌پیام** (پیام دوم ممنوع)؛ عبور از سقف ~۴۰۹۶ کاراکتر → برش از انتها با «…».
- **HTML ایمن (مصوب ۲۰۲۶-۰۹-۱۷):** متن‌های متغیر (عنوان، محله، شهر، برچسب جستجو، شکست امتیاز و…) قبل از درج در قالب escape می‌شوند (`&`→`&amp;`، `<`→`&lt;`، `>`→`&gt;`)؛ تگ‌های HTML فقط در قالب خود پیام‌اند.
- **پیش‌نمایش لینک خاموش:** ارسال با `disable_web_page_preview: true` (مصوب ۲۰۲۶-۰۹-۱۷) — لینک آخر پیام هست؛ preview در بارست چندپیامی حجیم و ناخواناست.
- چیدمان:
  1. خط اول: **«عنوان آگهی — برچسب جستجو»** بولد (برچسب = `label` و غایب → `id` — بخش ۱)
  2. فیلدها به‌صورت «کلید: مقدار» خط‌به‌خط: قیمت، قیمت هر متر، متراژ، اتاق، ساخت/عمر، طبقه، امکانات، محله، شهر، انتشار
  3. خط امتیاز: امتیاز کل + شکست فشردهٔ آن (بخش ۳.۳)
  4. لینک مستقیم `https://divar.ir/v/{token}` در آخر
- **زمان:** همهٔ زمان‌ها شمسی/تهران با قالب خود دیوار: «روز ماه سال، ساعت» (مثل «۲۲ شهریور ۱۴۰۵، ۱۷:۱۹»). سطر «زمان ارسال» نداریم — تلگرام خودش timestamp پیام را نشان می‌دهد.
- فیلد غایب → آن فیلد از پیام حذف می‌شود (مثلاً `published_at` وقتی سطرش در ویجت نیست — `divar-api.md` بخش ۷.۴).

نمونهٔ کامل پیام (HTML تلگرام):

```html
<b>آپارتمان ۵۵ متری پونک — آپارتمان تهران</b>
قیمت: ۱۲,۹۰۰,۰۰۰,۰۰۰ تومان
قیمت هر متر: ۲۳۴,۵۰۰,۰۰۰ تومان
متراژ: ۵۵
اتاق: ۲
ساخت: ۱۴۰۳ (عمر ۲ سال)
طبقه: ۳ از ۸
امکانات: پارکینگ · آسانسور · انباری
محله: پونک
شهر: تهران
انتشار: ۲۲ شهریور ۱۴۰۵، ۱۷:۱۹
امتیاز: ۶۵ — قیمت≤۱۳.۵B: ۱۵ · قیمت‌متری≤۲۸۰M: ۲۰ · عمر≤۵: ۱۵ · اتاق≥۲: ۵ · پارکینگ: ۵ · آسانسور: ۵
https://divar.ir/v/gapa1FMk
```

### ۳.۳. شکست امتیاز در پیام — فشرده

- فقط **قواعد برقرار** به‌صورت «نام: امتیاز» با جداکنندهٔ «·».
- قاعدهٔ نسبیِ skipشده → دلیل آن می‌آید (مثل `cohort_too_small` / `missing_construction_year`؛ `deal-scoring.md` بخش ۶). در فاز نسبی، آمار همتا (`cohort_median_pps` + `cohort_median_pps_eff`، `candidate_pps` + `candidate_pps_eff`، `discount_pct`، `percentile`، `robust_z`) به همین شکل فشرده ثبت می‌شود — مبنای تصمیم مقادیر مؤثر (`pps_eff`) است و نمایش کاربر روی قیمت‌متری واقعی می‌ماند.
- نمایش دلار در پیام ساخته نمی‌شود (ADR-0008).

### ۳.۴. ایمیل

- گیرنده‌ها فقط از کانفیگ (`to: []`) — ثبت‌نام ایمیل از بات وجود ندارد؛ هر گیرنده = یک ردیف delivery جدا (ADR-0010).
- **Subject (مصوب ۲۰۲۶-۰۹-۱۷):** `Top Divar — {عنوان آگهی} (امتیاز {N})` — قالب ثابت، قابل فیلتر در ایمیل‌کلاینت.
- محتوا: متن ساده (plain text) با همان فیلدهای پیام تلگرام (بدون HTML) + لینک مستقیم در آخر.
- **رمزنگاری:** کلید `smtp.encryption: starttls | tls | none` با پیش‌فرض `starttls` (مناسب port 587؛ `tls` برای 465؛ `none` فقط آزمایش محلی — هشدار startup، نه خطا).
- **معیار تحویل:** پذیرش پیام توسط سرور SMTP (پاسخ `250`)؛ bounce پایش نمی‌شود (خارج از دامنه MVP).
- خطای ارسال → ستون‌های `attempts` / `last_error` / `last_attempt_at` روی ردیف delivery + لاگ ERROR؛ تلاش مجدد در سویپ بعدی (بخش ۳.۵).

### ۳.۵. تحویل، retry و جبران (خلاصه — تفصیل: ADR-0010)

- تراکنش واحد: ذخیرهٔ آگهی + ردیف‌های `delivery` به‌ازای هر (آگهی، کانال، گیرنده) **قبل از** ارسال؛ علامت `sent` فقط بعد از موفقیت؛ وضعیت‌ها فقط `pending` / `sent` — وضعیت سومی وجود ندارد (اصلاح ۲۰۲۶-۰۹-۱۷).
- **سویپ retry دوره‌ای (اصلاح ۲۰۲۶-۰۹-۱۷ — جایگزین «بدون retry خودکار»):** هر `notify.retry_interval` (پیش‌فرض ۳۰ دقیقه) همهٔ `pending`ها قدیمی‌ترین اول ارسال می‌شوند (تلگرام با فاصلهٔ ~۱ ثانیه) تا موفقیت یا purge (سقف طبیعی ۳۷ روز)؛ خطاها در ستون‌های `attempts` / `last_error` / `last_attempt_at` ردیف delivery و در لاگ ثبت می‌شوند.
- جبران: هر تعامل کاربر ثبت‌شده با بات → ارسال **فوری** `pending`های او (قدیمی‌ترین اول، سقف `backfill_days` = ۷ روز) — در کنار سویپ می‌ماند تا منتظر سویپ بعدی نماند.
- ارسال مجدد از تاریخ (`/resend`؛ تاریخ شمسی): همهٔ ممتازهای از آن تاریخ به **فقط همین کاربر**، سقف ۳۰ روز، مستقل از جدول delivery؛ «ممتاز» = امتیاز ذخیره‌شده ≥ `min_score` لحظهٔ درج (بدون امتیازدهی مجدد).
- بارست: هر آگهی یک پیام، قدیمی‌ترین اول، فاصلهٔ ~۱ ثانیه بین پیام‌های تلگرام؛ ارسال کانال‌ها/گیرنده‌ها مستقل و موازی؛ **429 تلگرام:** انتظار `retry_after` (سقف ۶۰ ثانیه) + یک تلاش مجدد همان پیام — تکرار → `pending` می‌ماند + لاگ (مصوب ۲۰۲۶-۰۹-۱۷).

## ۴. پایش و نرخ درخواست (`polling`)

```yaml
polling:
  search_min_interval: 30s        # حداقل فاصله بین دو درخواست search (مستقل)
  detail_min_interval: 30s        # حداقل فاصله بین دو درخواست جزئیات (مستقل)
  # رفتار واقعی rate limit دادهٔ رسمی ندارد و در اجرا کشف می‌شود → هر دو مقدار قابل ویرایش؛
  # اجرا همچنان یک صف سریال واحد است (concurrency = ۱)
  min_interval: 5m                # کف سختِ interval جستجوها (مصوب ۲۰۲۶-۰۹-۱۷) — جدا از default
  default_interval: 5m            # فقط جایگزین جستجوهای بدون interval؛ دیگر نقش کف ندارد
  jitter: ±30s
  backoff: exponential            # روی 429/5xx
  max_consecutive_errors: 5       # بعد از آن، توقف موقت + لاگ + پیام هشدار اپراتور (throttle ۱/۲۴h — ADR-0003)
  max_pages_per_poll: 5           # سقف صفحه‌بندی هر poll (divar-api.md بخش ۹)
  notify_on_bump: false           # آگهی bumpشده (token موجود + sort_date جدید) دوباره نوتیف نشود
  fetch_post_detail: true         # GET posts-v2/web برای آگهی جدید پس از جغرافیا (ADR-0009)
```

- **کف در برابر پیش‌فرض (مصوب ۲۰۲۶-۰۹-۱۷):** `min_interval` کوچک‌ترین بازهٔ مجاز هر جستجو است (قید ایمنی نرخ درخواست به دیوار)؛ `default_interval` فقط مقدار جایگزینِ غیبت `interval` است و بالابردنش جستجوهای موجود را نمی‌شکند — اعتبارسنجی هر دو نسبت به کف (بخش ۷).

## ۵. تاریخچه (`history`)

بلوک سطح‌بالای **لایهٔ ذخیره‌گاه** — مستقل از `scoring` و **از MVP فعال** (حتی وقتی `scoring.relative` نیست یا `enabled: false` است):

```yaml
history:
  purge_margin_days: 7               # purge_after_days = window_days_max + purge_margin_days
```

- فرمول purge (ADR-0001؛ مصوب ۲۰۲۶-۰۹-۱۷ جلسهٔ دوم): `purge_after_days = window_days_max + purge_margin_days` — حاشیهٔ ۷ روز برای مرز `sort_date`؛ سنجهٔ purge همان `sort_date` است.
- `window_days_max` **پیش‌فرض سامانه‌ای ۳۰** دارد: کلید تنظیم پنجرهٔ همتا داخل `scoring.relative` است، ولی وقتی آن بلوک غایب/غیرفعال است، ذخیره‌گاه همان ۳۰ را مبنا می‌گذارد → purge در MVP = ۳۰+۷ = **۳۷ روز**؛ فعال‌شدن فاز نسبی فقط مبدأ فرمول را از پیش‌فرض سامانه‌ای به مقدار کانفیگ عوض می‌کند.
- برای حفظ dedup، tombstone مینیمال (token + آخرین `sort_date` دیده‌شده) نگه داشته می‌شود (ADR-0001؛ `deal-scoring.md` بخش ۴.۴).

## ۶. متغیرهای محیطی (`.env`)

```
TELEGRAM_BOT_TOKEN=...            # هرگز commit نمی‌شود
TELEGRAM_BOT_PASSWORD=...         # پسورد مشترک ثبت‌نام در بات (ADR-0010) — هرگز commit نمی‌شود
TELEGRAM_OPS_CHAT_ID=...          # مقصد پیام‌های هشدار اپراتور: OnFailure/Watchdog و خطای متوالی دیوار (ADR-0003)
SMTP_PASSWORD=...                 # رمز SMTP؛ لازم فقط اگر کانال email فعال است
# HTTPS_PROXY=...                 # اگر بود، TelegramNotifier از آن استفاده می‌کند (ADR-0002)
```

## ۷. اعتبارسنجی startup

1. ساختار YAML (schema validation).
2. `id` یکتا؛ `interval >= polling.min_interval` و `default_interval >= polling.min_interval` (خطا — تفکیک کف/پیش‌فرض، مصوب ۲۰۲۶-۰۹-۱۷).
3. فیلدهای قواعد امتیازدهی ⊆ فیلدهای نرمال‌شده شناخته‌شده (`divar-api.md` بخش ۷.۱ / ۷.۲ / ۷.۴) (خطا).
4. کلیدهای `form_data` ناشناخته → هشدار (نه خطا).
5. وجود `.env` و مقادیر لازم برای کانال‌های فعال (خطا): کانال `telegram` فعال → `TELEGRAM_BOT_TOKEN` و `TELEGRAM_BOT_PASSWORD`؛ کانال `email` فعال → `SMTP_PASSWORD` و `to` غیرخالی.
6. `notify.telegram.backfill_days <= window_days_max` (خطا) — مبنای `window_days_max`: مقدار `scoring.relative.window_days_max` اگر بلوک نسبی فعال باشد، وگرنه پیش‌فرض سامانه‌ای ۳۰ (مصوب ۲۰۲۶-۰۹-۱۷ جلسهٔ دوم؛ سازگاری با purge مشتق‌شده و سقف ارسال‌مجدد — ADR-0010).
7. `polling.search_min_interval` یا `polling.detail_min_interval` کمتر از `5s` → هشدار (خطا نیست).
8. `history.purge_margin_days` اگر حضور داشت ≥ ۰ (خطا اگر منفی).
9. `scoring_ref` هر جستجو باید به بلوک موجودی در `scoring` ارجاع دهد (خطا — مصوب ۲۰۲۶-۰۹-۱۷؛ غلط تایپی همان اول فاش شود، بدون fallback خاموش به `default`).
10. `notify.email.smtp.encryption == none` → هشدار (خطا نیست — فقط برای آزمایش محلی).
