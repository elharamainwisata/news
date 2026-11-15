# Brief subagen Ronde A, Senin 16 Nov 2026 (dibuat agen News 05:25 WIB)

Kamu menyiapkan PAKET ARTIKEL (naskah + gambar final di disk). Kamu TIDAK membuat post WordPress dan TIDAK mengunggah ke WordPress — agen induk yang mengunggah & menjadwalkan.

## Aturan wajib (baca dulu, utuh)
- `/home/khaeruddien/elharamain-news/routine/prompt_ronde_a.md` (aturan lengkap: gaya rumah, frasa AI terlarang, sortir, GAMBAR & GERBANG GAMBAR, aturan haji.go.id/BPKH/MEDIA ARAB/Kegiatan/Nusuk). Jalankan persis untuk artikelmu, kecuali bagian membuat post/unggah (dikerjakan induk).
- `/home/khaeruddien/elharamain-news/ATURAN_REDAKSI.md`.
- Judul situs 1-15 Nov: `/home/khaeruddien/elharamain-news/ronde-a-1116/judul_14hari.txt` (paling atas = terbaru). Topik WAJIB beda dari semua itu. Belum ada post 16 Nov (dicek 05:05 WIB).
- Foto Elharamain sebagai ilustrasi (bukan dari kegiatan yang diberitakan) TANPA caption; "Foto ilustrasi: Dokumentasi Elharamain Wisata" DILARANG. Jangan pakai foto yang sudah dipakai 7 hari terakhir: cek paket di /home/khaeruddien/elharamain-news/ronde-a-1114, ronde-b-1114, ronde-a-1113, ronde-b-1113, ronde-a-1112, ronde-b-1112 (file article.json field images). Post 15 Nov dibuat di mesin lain (tanpa paket di disk): bila memakai Drive, cek juga gambar post 15 Nov lewat `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?after=2026-11-15T00:00:00&per_page=30&_fields=id,title,jetpack_featured_media_url"` dan hindari foto yang sama.
- Daftar rilis haji.go.id 9-15 Nov: `rilis.txt` (tanggal | provinsi | judul | slug). Mentah: pusat.json & prov_*.json di folder ini; detail lewat `https://<prov>.haji.go.id/api/news/<slug>` (pusat: haji.go.id).
- Ronde ini dibagi ke 8 subagen; tiap subagen hanya memakai sumber yang ditugaskan. Penugasan seluruh ronde (JANGAN ambil rilis milik slot lain):
  07:00 U&H (29): jambi "Kemenhaj Tetapkan Dua Tahap Pelunasan Bipih Haji Reguler 2027, Ini Jadwalnya" + jambi "Ini 5 Syarat Wajib Pelunasan Bipih Haji Reguler 2027" (15 Nov; boleh digabung jadi satu artikel) | 12:20 Tanya Jawab (30): jambi "Cek Istithaah dan Biaya Pelunasan Haji, Jemaah Bisa Akses Lewat Aplikasi Satu Haji" (15 Nov) — sudut pertanyaan jemaah, beda dari artikel 07:00 | 07:40 Berita (23): kalsel "Jemput Bola Pelunasan Haji Reguler, Kemenhaj Balangan Gandeng BSI KC Tanjung..." (12 Nov) | 10:20 Berita (23): maluku "Edukasi Haji Sejak Dini, Kemenhaj Maluku Sapa Siswa MAN Ambon" (12 Nov) | 09:00 U&H (29): pusat "Kemenhaj Dorong PIHK dan PPIU Patuhi Regulasi demi Pelayanan Jemaah Berkualitas" (12 Nov; nama travel/PIHK/PPIU DILARANG disebut) | 13:00 U&H (29): gorontalo "Kemenhaj Kab. Gorontalo Lanjutkan Pendampingan Paspor..." (11 Nov; cadangan kalteng "Kemenhaj Pulang Pisau Koordinasikan Pelaksanaan Manasik dan Pelunasan Haji 2027 dengan BSI Kuala Kapuas" 13 Nov) | 13:40 Berita (23): rilis BPKH terbaru yang belum ditulis (cadangan: jateng "Seleksi CAT Petugas Haji Daerah, 311 Calon Petugas..." 14 Nov) | 08:20 Fiqih (26, evergreen, beda dari Fiqih 14 hari) | 09:40 Sejarah Islam (27) | 11:00 Kegiatan (24) | 11:40 MEDIA ARAB (29/25) | 14:20 Dunia islam (25) | Nusuk 08:00 / 10:40 / 13:20 — kategori 29.
- Rilis yang SUDAH ditulis (jangan dipakai): semua yang judulnya cocok di judul_14hari.txt, termasuk seleksi pembimbing KBIHU (kepri 14 Nov), Bandung pemeriksaan kesehatan, MagangHub, Bali YHM NU, DKI rakor & evaluasi pelunasan, Jambi eselon IV PHD, Lampung seleksi PHD, Murung Raya, Gorontalo pelunasan 21 persen, Parepare satgas & imigrasi, NTT pengajian, Sikka jalan santai, Bengkalis.

## Lingkungan
- Python gambar: `/tmp/v/bin/python` (Pillow sudah tersedia; JANGAN buat ulang venv). ffmpeg di ~/.local/bin/ffmpeg.
- Kerja di folder `/home/khaeruddien/elharamain-news/ronde-a-1116/<SLOT>/` (SLOT mis. `1500`). Unduhan mentah di subfolder `raw/`.
- Cek tag: `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/tags?search=<kata>&_fields=id,name"` — pakai HANYA ID tag yang sudah ada (3-5 tag) + 34 (elharamain wisata).
- Link internal: cari via `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?search=<kata>&_fields=id,link,title"`; pakai URL `link` asli.
- WebSearch/WebFetch boleh (domain allowlist di prompt). Jangan mengakali 403/406.
- Ilustrasi AI (hanya bila aturan mengharuskan, mis. berita negatif): kamu TIDAK bisa membuatnya. Tulis prompt Inggris lengkap (sesuai aturan gaya foto dokumenter, wajah Indonesia/Arab, tanpa teks/logo/masjid) di article.json `images.N.ai_prompt` dan biarkan `file` kosong; induk yang membuat.

## Keluaran per artikel: `<SLOT>/article.json`
```json
{
 "slot": "2026-11-16T07:00:00",
 "category": 29,
 "title": "...", "excerpt": "140-160 karakter",
 "tags": [34, ...],
 "content_file": "content.html",
 "images": {
   "1": {"file": "/abs/path/utama.jpg", "alt": "...", "caption": "Foto: Kementerian Haji dan Umrah RI | Foto: Dokumentasi Elharamain Wisata | Ilustrasi | \"\" (stok/SPA-kredit-di-gambar)", "seen": "kalimat apa yang benar-benar terlihat", "evidence": "URL/caption/subfolder sumber", "ai_prompt": ""},
   "2": {...}
 },
 "sensitive": false,
 "word_count": 0,
 "sources": ["url ..."],
 "haji_go_id": "pusat|dki|riau|...|tidak + referenceUrl",
 "notes": "catatan untuk redaktur, calon topik yang digugurkan + alasan"
}
```
`content.html` = blok Gutenberg (`<!-- wp:paragraph --><p>...</p><!-- /wp:paragraph -->`), pembuka `<strong>ELHARAMAIN NEWS</strong> –`, penutup praktis, lalu paragraf CTA miring persis dari prompt. Gambar 1 = foto utama (TIDAK ditaruh di content). Untuk gambar sisipan N≥2 taruh baris placeholder `%%IMG2%%` (sendirian di barisnya) di antara blok paragraf; induk menggantinya dengan blok wp:image.
Gambar final: JPEG q82, foto utama 16:9 lebar 1600 (min 1200), sisipan 4:5 atau 16:9. Read setiap gambar final (gerbang gambar 6 langkah) sebelum dimasukkan.

Hitung kata (tanpa tag HTML) dan pastikan 450-600 (Kegiatan 450-650). Baca ulang draf seperti redaktur Kompas: buang frasa AI terlarang, tanpa tanda pisah panjang (—), tanpa subjudul/bullet.

Laporan akhirmu ke induk: ringkas (slot, judul, path article.json, gambar + apa yang terlihat, sumber, catatan). Jangan tempel naskah lengkap di laporan.

- Link keluar MAKSIMAL 1 per artikel (hanya sumber utama); sumber lain disebut nama tanpa link. Link internal, CTA WA, elharamainwisata.com tidak dihitung.
- Kegiatan: baca/isi `/home/khaeruddien/elharamain-news/kegiatan-1116/klaim.txt`. Grup yang SUDAH diberitakan di lokasi: 1448 H 19 Jul Platinum, 26 Jul Prem, 12 Jul Silver, 20 Jul Bronze, 16 Jul 12H, 5 Agt Bronze, 6 Nov Bronze, 8 Nov Plat-Sil, 9 Nov Bronze (+ semua judul Kegiatan di judul_14hari.txt dan arsip lama: cek posts?categories=24). Cadangan bebas per 14 Nov: 26 JULI 2026 PLAT-SIL (1CBLLUh4PwkfLU4YqHImzO77SfsRu5lc2), 13 JULI 2026 BRONZE (15ZG31XCNzo-xkfrY9UzSEnyT-8rYdfQ_), grup Agustus (12 Agt 12H, 17 Agt, 20 Agt Silver, 24 Agt Silver, 9 Agt Silver), grup November 2026 lain yang belum ditulis.
