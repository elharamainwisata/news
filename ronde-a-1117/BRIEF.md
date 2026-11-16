# Brief subagen Ronde A, Selasa 17 Nov 2026 (dibuat agen News 05:15 WIB)

Kamu menyiapkan PAKET ARTIKEL (naskah + gambar final di disk). Kamu TIDAK membuat post WordPress dan TIDAK mengunggah ke WordPress — agen induk yang mengunggah & menjadwalkan.

## Aturan wajib (baca dulu, utuh)
- `/home/khaeruddien/elharamain-news/routine/prompt_ronde_a.md` (aturan lengkap: gaya rumah, frasa AI terlarang, sortir, GAMBAR & GERBANG GAMBAR, aturan haji.go.id/BPKH/MEDIA ARAB/Kegiatan/Nusuk). Jalankan persis untuk artikelmu, kecuali bagian membuat post/unggah (dikerjakan induk).
- `/home/khaeruddien/elharamain-news/ATURAN_REDAKSI.md`.
- Judul situs 3-16 Nov: `/home/khaeruddien/elharamain-news/ronde-a-1117/judul_14hari.txt` (paling atas = terbaru). Topik WAJIB beda dari semua itu. Belum ada post 17 Nov (dicek 05:05 WIB).
- Juga hindari topik DRAFT 16 Nov (ditahan, tidak tampil di judul_14hari): Pohuwato rekam biometrik lansia; PLHUT Manggarai; Dairi majelis taklim Sinehu & Parbuluan (usia bukan alasan menunda daftar haji); Kanwil DKI visitasi penyelenggara di Bogor; moratorium izin baru travel umrah/3.600 PPIU; 311 calon PHD Jateng CAT; KSrelief Flores; Yayasan Sultan bin Abdulaziz & UNESCO; Group Agustus 2026 12 Hari Quba; Group Juli 2026 Bronze payung Nabawi.
- Foto Elharamain sebagai ilustrasi (bukan dari kegiatan yang diberitakan) TANPA caption; "Foto ilustrasi: Dokumentasi Elharamain Wisata" DILARANG. Jangan pakai foto yang sudah dipakai 7 hari terakhir: cek paket di /home/khaeruddien/elharamain-news/ronde-a-1116, ronde-b-1116, cadangan-b-1116, ronde-a-1114, ronde-b-1114, ronde-a-1113, ronde-b-1113 (file article.json field images); bila ragu bandingkan juga gambar post terbit via `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?after=2026-11-10T00:00:00&per_page=100&_fields=id,title,jetpack_featured_media_url"`.
- Daftar rilis haji.go.id 3-16 Nov: `rilis.txt` (tanggal UTC | provinsi | judul | slug). Mentah: pusat.json & prov_*.json di folder ini; detail lewat `https://<prov>.haji.go.id/api/news/<slug>` (pusat: haji.go.id). Slug yang sudah pernah dipakai: `used_all.txt`.
- Ronde ini dibagi ke 7 subagen; tiap subagen hanya memakai sumber yang ditugaskan. Penugasan seluruh ronde (JANGAN ambil rilis milik slot lain):
  07:00 U&H (29): pusat "Transformasi Layanan Haji 2027, PPIH Dituntut Lebih Responsif dan Berorientasi Jemaah" (16 Nov) | 09:00 U&H (29): kepri "Tak Hanya Pelunasan Haji, Kemenhaj Batam Siapkan Langkah Strategis Buka Akses Penerbangan Langsung ke Saudi" (16 Nov) (cadangan: kepri "Sri Mulelni Dorong Percepatan Pelunasan Haji dan Kesiapan Paspor Jemaah Cadangan") | 13:00 U&H (29): kalteng "Hadirkan Pelayanan Jemput Bola, Kantor Kemenhaj Kabupaten Katingan Fasilitasi Pembatalan Haji Jemaah karena Sakit" (15 Nov; topik sakit = SENSITIF → ilustrasi AI, tanpa foto Elharamain; cadangan: bengkulu "Kemenhaj Kabupaten Mukomuko Kupas Tuntas Regulasi dan Mitigasi Jemaah Haji Cadangan", sudut beda dari TJ 18427) | 07:40 Berita (23): gorontalo "Kemenhaj Gorontalo Perkenalkan Haji dan Umrah Store, Buka Peluang UMKM Masuk Ekosistem Ekonomi Haji" (16 Nov) + boleh digabung gorontalo "Chandra Sulistio: Potensi Ekonomi Haji dan Umrah Rp74 Triliun..." / "Chandra Sulistio Paparkan Empat Strategi..." / "UMKM Perhatikan Standar Produk untuk Tembus Pasar Arab Saudi" (semua jadi milik slot 07:40) | 10:20 Berita (23): rilis BPKH terbaru yang belum ditulis (cek judul_14hari: 18630 kanal informasi 5,7 juta jemaah SUDAH; cadangan: sumut "Perkuat Pemahaman Ibadah, Kakan Kemenhaj Dairi Bimbing 100 Peserta PB3S Praktik Manasik Haji" 16 Nov) | 13:40 Berita (23): bengkulu "Kemenhaj Bengkulu Utara Monitor Pemeriksaan Kesehatan CJH Tambahan Tahun 2027" (16 Nov) (cadangan: ntt "40 Jemaah Haji NTT Telah Lunasi Bipih Tahap I" / kalteng "Operator Siskohat Laporkan Perkembangan Pelunasan Bipih Tahap I") | 08:20 Fiqih (26, evergreen, beda dari Fiqih 14 hari) | 12:20 Tanya Jawab (30): usahakan berangkat dari rilis haji.go.id yang TIDAK ditugaskan di atas (mis. aceh/kalteng/kepri "Pengumuman Seleksi PHD 1448 H" → "Apa itu Petugas Haji Daerah dan bagaimana seleksinya?" bila belum pernah ditulis; atau topik evergreen) | 09:40 Sejarah Islam (27) | 11:00 Kegiatan (24) | 11:40 MEDIA ARAB (29/25) | 14:20 Dunia islam (25) | Nusuk 08:00 / 10:40 / 13:20 — kategori 29.
- Rilis yang SUDAH ditulis (jangan dipakai): semua yang judulnya cocok di judul_14hari.txt atau slug di used_all.txt.

## Lingkungan
- Python gambar: `/tmp/v/bin/python` (Pillow sudah tersedia; JANGAN buat ulang venv). ffmpeg di ~/.local/bin/ffmpeg.
- Kerja di folder `/home/khaeruddien/elharamain-news/ronde-a-1117/<SLOT>/` (SLOT mis. `0700`). Unduhan mentah di subfolder `raw/`.
- Cek tag: `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/tags?search=<kata>&_fields=id,name"` — pakai HANYA ID tag yang sudah ada (3-5 tag) + 34 (elharamain wisata).
- Link internal: cari via `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?search=<kata>&_fields=id,link,title"`; pakai URL `link` asli.
- WebSearch/WebFetch boleh (domain allowlist di prompt). Jangan mengakali 403/406.
- Ilustrasi AI (hanya bila aturan mengharuskan, mis. berita negatif): kamu TIDAK bisa membuatnya. Tulis prompt Inggris lengkap (sesuai aturan gaya foto dokumenter, wajah Indonesia/Arab, tanpa teks/logo/masjid) di article.json `images.N.ai_prompt` dan biarkan `file` kosong; induk yang membuat.

## Keluaran per artikel: `<SLOT>/article.json`
```json
{
 "slot": "2026-11-17T07:00:00",
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
- Kegiatan: baca/isi `/home/khaeruddien/elharamain-news/kegiatan-1117/klaim.txt` (tambahkan satu baris klaimmu). Grup yang SUDAH diberitakan/sedang dipakai (JANGAN): 1448 H 19 Jul Platinum, 26 Jul Prem, 26 Jul Plat-Sil, 12 Jul Silver, 13 Jul Bronze, 20 Jul Bronze, 16 Jul 12H, 5 Agt Bronze, 12 Agt 12H, 5 Nov 12H, 6 Nov Bronze, 8 Nov Plat-Sil, 9 Nov Bronze, serta semua judul Kegiatan di judul_14hari.txt dan arsip (cek `posts?categories=24&per_page=100`). Kandidat: grup Agustus 2026 lain (17 Agt, 20 Agt Silver, 24 Agt Silver, 9 Agt Silver) atau grup September/Oktober 1448 H yang belum ditulis dengan tema berbeda.
