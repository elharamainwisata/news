#!/bin/bash
# Cadangan Claude API untuk news.elharamainwisata.com.
# Pemakaian: backup/cadangan_api.sh A|B [--paksa]
# Dijalankan cron. Mengecek slot ronde hari ini; bila routine cloud gagal (slot kosong),
# menjalankan prompt ronde yang sama lewat Claude API (ANTHROPIC_API_KEY, bukan langganan).
set -u
RONDE="${1:-}"
PAKSA="${2:-}"
REPO="$HOME/elharamain-news"
ENV_FILE="$HOME/.config/elharamain-news/api-backup.env"
LOGDIR="$REPO/backup/log"
mkdir -p "$LOGDIR" "$REPO/backup/kerja"
export PATH="$HOME/.local/bin:$PATH"
cd "$REPO" || exit 1

case "$RONDE" in
  A) AFTER="06:55"; BEFORE="14:25"; PROMPT_FILE="routine/prompt_ronde_a.md" ;;
  B) AFTER="14:55"; BEFORE="22:25"; PROMPT_FILE="routine/prompt_ronde_b.md" ;;
  *) echo "Pakai: $0 A|B [--paksa]"; exit 1 ;;
esac

LOG="$LOGDIR/$(date +%F)-ronde-$RONDE.log"
exec >>"$LOG" 2>&1
echo "=== $(date '+%F %T') cek cadangan API ronde $RONDE ==="

[ -f "$ENV_FILE" ] || { echo "File $ENV_FILE tidak ada."; exit 1; }
set -a; . "$ENV_FILE"; set +a
[ -n "${ANTHROPIC_API_KEY:-}" ] || { echo "ANTHROPIC_API_KEY kosong."; exit 1; }
BUDGET="${BATAS_BIAYA_USD:-30}"

LOCK="$REPO/backup/kerja/.lock-$RONDE"
exec 9>"$LOCK"
flock -n 9 || { echo "Run cadangan ronde $RONDE lain masih berjalan."; exit 0; }

hitung() {
  local today; today=$(date +%F)
  python3 backup/wp.py posts.list "{\"status\":\"future,publish,draft\",\"after\":\"${today}T${AFTER}:00\",\"before\":\"${today}T${BEFORE}:00\",\"per_page\":50,\"include_fields\":[\"id\"]}" \
    | python3 -c 'import json,sys; print(len(json.load(sys.stdin)["data"]))'
}

N1=$(hitung) || { echo "Gagal membaca WordPress."; exit 1; }
echo "Post di slot ronde $RONDE: $N1"
if [ "$N1" -ge 10 ] && [ "$PAKSA" != "--paksa" ]; then
  echo "Ronde $RONDE sudah lengkap. Selesai."; exit 0
fi

# Pastikan routine cloud tidak sedang berjalan (jumlah post masih bertambah).
if [ "$PAKSA" != "--paksa" ]; then
  sleep 1200
  N2=$(hitung) || exit 1
  echo "Cek ulang setelah 20 menit: $N2"
  if [ "$N2" -ge 10 ]; then echo "Sudah lengkap. Selesai."; exit 0; fi
  if [ "$N2" -gt "$N1" ]; then echo "Routine cloud masih menulis. Cadangan API tidak dijalankan."; exit 0; fi
fi

TMP_PROMPT="$REPO/backup/kerja/prompt-$RONDE.md"
sed -e "s/__RONDE__/$RONDE/g" -e "s/__AFTER__/$AFTER/g" -e "s/__BEFORE__/$BEFORE/g" backup/header_api.md > "$TMP_PROMPT"
cat "$PROMPT_FILE" >> "$TMP_PROMPT"
printf '\nTanggal dan jam sekarang: %s WIB.\n' "$(date '+%A %F %H:%M')" >> "$TMP_PROMPT"

echo "Menjalankan Claude API (model claude-opus-5-5, batas biaya \$$BUDGET)..."
claude --bare -p \
  --model claude-opus-5-5 \
  --max-budget-usd "$BUDGET" \
  --permission-mode dontAsk \
  --allowedTools "Bash" "Read" "Write" "Edit" "Glob" "Grep" "WebSearch" "WebFetch" \
  < "$TMP_PROMPT"
echo "=== selesai $(date '+%F %T'), kode keluar $? ==="
