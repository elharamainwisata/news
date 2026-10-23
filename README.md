# Elharamain News

Alat bantu otomasi untuk [news.elharamainwisata.com](https://news.elharamainwisata.com).

## Isi

- `routine/prompt.md` — prompt routine Claude Code (cloud) yang setiap hari pukul 06:00 WIB membuat 9 artikel (1 per kategori), dijadwalkan terbit tiap jam 09:00–17:00 WIB, lengkap dengan caption sosmed.
- `sosmed/buat_kartu.py` — pembuat kartu Instagram gaya @elharamainnews (feed 1080x1350 / story 1080x1920).
- `sosmed/fonts/` — font Poppins (SIL Open Font License).

## Kartu Instagram

```bash
pip install pillow
python3 sosmed/buat_kartu.py --foto foto.jpg --judul "Judul artikel" --out kartu.jpg --format feed
# opsional: --logo sosmed/logo.png  (PNG transparan logo ELHARAMAIN NEWS)
```

## Posting sosmed

Caption ditulis routine ke meta `jetpack_publicize_message` (tersimpan sebagai `_wpas_mess`).
Plugin Bit Social Pro memposting saat artikel terbit dengan template `{custom_field_[_wpas_mess]}`.
