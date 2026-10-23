# Elharamain News

Alat bantu otomasi untuk [news.elharamainwisata.com](https://news.elharamainwisata.com).

## Isi

- `routine/prompt_ronde_a.md` dan `routine/prompt_ronde_b.md` — prompt dua routine Claude Code (cloud): Ronde A pukul 05:00 WIB dan Ronde B pukul 11:00 WIB, masing-masing 10 artikel (9 kategori + 1 kegiatan jemaah), terbit tiap 45 menit 07:00–21:15 WIB.
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
