# استقرار (Deployment)

> مرحلهٔ ۷ — سرویس همیشه‌روشن با systemd روی VPS داخل ایران (ADR-0003).
> تلگرام از طریق `HTTPS_PROXY` روی **همهٔ** فراخوانی‌های Bot API می‌گذرد: ارسال نوتیف،
> درگاه بات (`getUpdates`) و پیام `curl`ی شکست (ADR-0002).

## ۱. نصب بسته روی سرور

```bash
sudo mkdir -p /opt/top-divar && sudo chown -R "$USER" /opt/top-divar
git clone <repo> /opt/top-divar
cd /opt/top-divar
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt .
```

## ۲. تنظیمات

- `config.yaml` — جستجوها، امتیازدهی، کانال‌های اطلاع‌رسانی (`docs/configuration.md`)
- `.env` — مقادیر حساس (نمونهٔ کلیدها: `docs/configuration.md` بخش ۶):

```
TELEGRAM_BOT_TOKEN=...
TELEGRAM_BOT_PASSWORD=...
TELEGRAM_OPS_CHAT_ID=...   # مقصد هشدارهای اپراتور (OnFailure/Watchdog/خطای متوالی دیوار)
SMTP_PASSWORD=...          # فقط اگر کانال email فعال است
HTTPS_PROXY=http://...     # اگر بود، همهٔ فراخوانی‌های بات تلگرام از آن می‌گذرند
```

اعتبارسنجی پیش از اجرا: `.venv/bin/top-divar validate`

## ۳. یونیت‌های systemd

`deploy/top-divar.service` این رفتارها را می‌دهد (ADR-0003):

- `Type=notify` + `WatchdogSec=300` — برنامه `READY=1` می‌فرستد و تسک heartbeat جدا از
  صف کاری هر ۱۵۰ ثانیه `WATCHDOG=1` می‌زند؛ قفل‌شدن حلقه → ری‌استارت خودکار
- `Restart=always` — کرش → راه‌اندازی مجدد
- `OnFailure=top-divar-failure.service` — پیام «از راه افتاد» با `curl` به
  `TELEGRAM_OPS_CHAT_ID` از همان `HTTPS_PROXY`
- `ExecReload=/bin/kill -HUP $MAINPID` — `systemctl reload top-divar` یعنی SIGHUP یعنی
  بارگذاری مجدد زندهٔ کانفیگ؛ YAML خراب سرویس را نمی‌کشد و کانفیگ قبلی می‌ماند (ADR-0011)
- پشتیبان روزانه: `deploy/top-divar-backup.timer` دستور `top-divar backup` را می‌زند —
  `VACUUM INTO` در `data/backups/` با چرخش ~۷ نسخه (ADR-0001)

```bash
chmod +x /opt/top-divar/deploy/on-failure.sh
sudo cp deploy/top-divar*.service deploy/top-divar-backup.timer /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now top-divar.service top-divar-backup.timer
```

نکته: مسیر پیش‌فرض نصب `/opt/top-divar` است؛ اگر جای دیگری است، `WorkingDirectory`،
`ExecStart`، `EnvironmentFile` و `ExecStart`ِ یونیت پشتیبان را هم‌زمان عوض کنید.

## ۴. عملیات روزمره

```bash
systemctl status top-divar          # وضعیت (خروجی journalctl -u top-divar -f برای لاگ JSON)
systemctl reload top-divar          # اعمال زندهٔ تغییر config.yaml
systemctl restart top-divar         # ری‌استارت؛ گفتگوهای نیمه‌کارهٔ ثبت‌نام می‌افتند (طراحی همین است)
journalctl -u top-divar -f          # دنبال‌کردن لاگ
top-divar user list                 # فهرست کاربران بات + تعداد pending هر کدام
top-divar user remove <username>    # حذف کاربر + dead شدن pendingهای او
top-divar reset-watermark <id>      # baseline عمدی یک جستجو
top-divar backup                    # پشتیبان دستی (تایمر روزانه هم همین را می‌زند)
```

## ۵. نکات تک‌نمونه و بات

- بات با `getUpdates` کار می‌کند؛ تلگرام فقط **یک** poller فعال تحمل می‌دهد. سرویس در
  شروع `run` قفل `data/top_divar.lock` می‌گیرد — نمونهٔ دوم با پیام روشن بالا نمی‌آید
  (قفل با مرگ پروسه آزاد می‌شود و با `Restart=always` سازگار است)
- اگر وب‌هوک جانبی روی همان توکن باشد یا نمونهٔ قدیمی هنوز زنده باشد، تلگرام 409
  می‌دهد — گذرا تلقی می‌شود، بات backoff کوتاه می‌کند و ادامه می‌دهد
- کاربران با `/start` → پسورد مشترک → username ثبت‌نام می‌کنند؛ هر پیام متنی‌شان
  pendingهای عقب‌افتاده (تا ۷ روز) را فوری می‌فرستد
