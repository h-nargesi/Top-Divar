#!/usr/bin/env bash
# پیام «سرویس از راه افتاد» به اپراتور — ADR-0003.
# از همان HTTPS_PROXY روی Bot API تلگرام می‌گذرد (ADR-0002)؛
# TELEGRAM_BOT_TOKEN و TELEGRAM_OPS_CHAT_ID از EnvironmentFile (.env) می‌آیند.

set -u

UNIT_NAME="${1:-top-divar.service}"

if [ -z "${TELEGRAM_BOT_TOKEN:-}" ] || [ -z "${TELEGRAM_OPS_CHAT_ID:-}" ]; then
    echo "on-failure: TELEGRAM_BOT_TOKEN/TELEGRAM_OPS_CHAT_ID تنظیم نیستند؛ هشدار مقصدی ندارد." >&2
    exit 0
fi

PROXY_ARGS=()
if [ -n "${HTTPS_PROXY:-}" ]; then
    PROXY_ARGS=(--proxy "${HTTPS_PROXY}")
fi

TEXT="هشدار: سرویس Top Divar (${UNIT_NAME}) از راه افتاد — $(date '+%Y-%m-%d %H:%M:%S')"
PAYLOAD=$(printf '{"chat_id": "%s", "text": "%s", "disable_web_page_preview": true}' \
    "${TELEGRAM_OPS_CHAT_ID}" "${TEXT}")

curl -sS --max-time 15 "${PROXY_ARGS[@]}" \
    -H 'Content-Type: application/json' \
    -d "${PAYLOAD}" \
    "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" >/dev/null || true
