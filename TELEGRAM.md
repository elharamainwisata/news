# Perintah Claude Code lewat Telegram

Bot: **@elharamainews_bot**. Memakai fitur resmi Claude Code **Channels** (plugin Telegram).

> Token bot TIDAK disimpan di repo ini. Token ada di `~/.claude/channels/telegram/.env` (hanya di Mac). Bila token bocor, buat ulang di @BotFather dengan `/revoke`.

## Syarat

- Bun terpasang: `brew install oven-sh/bun/bun` (cek: `bun --version`)
- Claude Code login dengan akun claude.ai
- Mac menyala dan sesi Claude Code tetap terbuka (bot hanya membalas selama sesi berjalan)

## Pemasangan (sekali saja)

1. Buat bot di Telegram lewat **@BotFather** → `/newbot` → salin token.
2. Di Claude Code:
   ```
   /plugin install telegram@claude-plugins-official
   /telegram:configure <TOKEN>
   ```
   (pilih scope **user**; bila diminta, jalankan `/reload-plugins`)

## Menjalankan

```
cd ~/Desktop/news
claude --channels plugin:telegram@claude-plugins-official
```

## Memasangkan akun (sekali saja)

1. Kirim pesan apa saja ke @elharamainews_bot → bot membalas kode pairing.
2. Di Claude Code:
   ```
   /telegram:access pair <KODE>
   /telegram:access policy allowlist
   ```
   `allowlist` = hanya akun yang sudah dipasangkan yang bisa memberi perintah.

## Contoh perintah

- `berita hari ini apa saja`
- `cek artikel yang belum tayang`
- `ganti gambar artikel <judul> dengan foto asli`
- `jalankan Ronde A sekarang`

Dokumentasi: https://code.claude.com/docs/en/channels.md

## Mesin bot 24 jam (sejak 31/10/2026): Mac mini Ubuntu

Bot jalan di **Mac mini** (Ubuntu, Tailscale `100.125.20.102`, user `khaeruddien`), bukan di Mac lain dan **bukan di VPS Tencent `elharamain`** (server itu untuk pekerjaan lain, jangan dipasangi apa pun). Jangan jalankan bot di dua mesin bersamaan.

- Repo: `~/elharamain-news` (folder `~/news` di Mac mini adalah folder lain, jangan disentuh).
- Skrip start: `~/elharamain-news-bot.sh` — mount memori Google Drive (`~/.local/bin/rclone`, folder `claude-memory-elharamain` → `~/gdrive-memory`), lalu menjalankan `claude --channels plugin:telegram@claude-plugins-official` di tmux sesi `bot`.
- Otomatis saat restart: baris `@reboot` di crontab user (ditambahkan manual oleh pemilik).
- Akses: `dmPolicy allowlist`, hanya akun Telegram pemilik.

Perintah berguna (di Mac mini, atau dari MacBook: `ssh -i ~/.ssh/macmini khaeruddien@100.125.20.102`):
```
tmux attach -t bot                 # lihat/setujui sesi bot (keluar: Ctrl+B lalu D)
tmux kill-session -t bot; ~/elharamain-news-bot.sh   # restart bot
cd ~/elharamain-news && git pull   # ambil perubahan prompt terbaru
```
