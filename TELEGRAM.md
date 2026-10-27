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
