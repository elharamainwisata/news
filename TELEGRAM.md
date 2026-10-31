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

## Server 24 jam (sejak 31/10/2026)

Bot sekarang jalan di VPS `elharamain` (Ubuntu 24.04, `ssh elharamain`), **bukan di Mac**. Jangan jalankan bot di Mac bersamaan.

- Service `claude-telegram` (systemd) menjalankan `claude --channels plugin:telegram@claude-plugins-official` di sesi tmux `bot`, folder `~/news`, otomatis hidup lagi setelah reboot.
- Service `rclone-claude-memory` me-mount Google Drive `claude-memory-elharamain` ke `~/gdrive-memory`; memori Claude server (`~/.claude/projects/-home-ubuntu-news/memory`) menunjuk ke sana, sama dengan Mac.
- Akses: `dmPolicy allowlist`, hanya akun Telegram yang sudah dipasangkan.

Perintah berguna (di server):
```
tmux attach -t bot                      # lihat/setujui sesi bot (keluar: Ctrl+B lalu D)
sudo systemctl restart claude-telegram  # restart bot
systemctl status claude-telegram rclone-claude-memory
cd ~/news && git pull                   # ambil perubahan prompt terbaru
```
