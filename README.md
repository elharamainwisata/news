# Elharamain News

Alat bantu otomasi untuk [news.elharamainwisata.com](https://news.elharamainwisata.com).

## Isi

- `routine/prompt_ronde_a.md` dan `routine/prompt_ronde_b.md` — prompt dua routine Claude Code (cloud): Ronde A pukul 05:00 WIB dan Ronde B pukul 11:00 WIB, masing-masing 12 artikel (24 per hari, termasuk 2 Kegiatan jemaah dan 2 Media Arab), terbit tiap 40 menit 07:00–22:20 WIB. Routine cadangan pukul 14:00 WIB memakai `routine/prompt_ronde_b_cadangan_header.md` + `routine/prompt_ronde_b.md` dan hanya mengisi slot sore yang kosong.
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
