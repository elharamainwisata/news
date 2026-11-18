# Brief subagen Ronde B, Rabu 18 Nov 2026 (dibuat agen News 11:15 WIB)

Kamu menyiapkan PAKET ARTIKEL (naskah + gambar final di disk). Kamu TIDAK membuat post WordPress dan TIDAK mengunggah ke WordPress — agen induk yang mengunggah & menjadwalkan.

## Aturan wajib (baca dulu, utuh)
- `/home/khaeruddien/elharamain-news/routine/prompt_ronde_b.md` (aturan lengkap: gaya rumah, frasa AI terlarang, sortir, GAMBAR & GERBANG GAMBAR, aturan haji.go.id/BPKH/MEDIA ARAB/Kegiatan/Nusuk). Jalankan persis untuk artikelmu, kecuali bagian membuat post/unggah (dikerjakan induk).
- `/home/khaeruddien/elharamain-news/ATURAN_REDAKSI.md`.
- Judul situs 4-18 Nov: `/home/khaeruddien/elharamain-news/ronde-b-1118/judul_14hari.txt` (urut terbaru dulu, format: id tanggal c[kategori] judul; 5 baris teratas = post future Ronde A hari ini 11:40-14:20). Topik WAJIB beda dari semua itu, termasuk 12 post Ronde A hari ini (18794-18808: Itjen awasi pelunasan/Siskohat, Diklat PPIH DKI, batu/tanah Tanah Haram oleh-oleh, pelunasan Kepri 22,26%, Masjid Namirah, embarkasi Antara Palu, Group Agustus 2026 Bronze kebun kurma/unta, Taman Al-Misfalah, data surat pendaftaran haji vs KTP, Maluku periksa kesehatan awal, BPKH-Lazismu mobil dakwah, destinasi Qiblatain teh Madinah).
- Juga hindari topik draft lama yang ditahan (Pohuwato biometrik, PLHUT Manggarai, Dairi majelis taklim, visitasi Bogor, moratorium 3.600 PPIU, 311 calon PHD Jateng, KSrelief Flores, Yayasan Sultan bin Abdulaziz & UNESCO).
- Foto Elharamain sebagai ilustrasi (bukan dari kegiatan yang diberitakan) TANPA caption; "Foto ilustrasi: Dokumentasi Elharamain Wisata" DILARANG. Jangan pakai foto yang sudah dipakai 7 hari terakhir: cek paket di /home/khaeruddien/elharamain-news/ronde-a-1118, ronde-a-1117, ronde-b-1117, ronde-b-1116, cadangan-b-1116, ronde-a-1116, ronde-a-1114, ronde-b-1114, tambahan-1117 (article.json field images/evidence); bila ragu bandingkan gambar post terbit via `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?after=2026-11-11T00:00:00&per_page=100&_fields=id,title,jetpack_featured_media_url"`.
- Daftar rilis haji.go.id 4-18 Nov: `/home/khaeruddien/elharamain-news/ronde-b-1118/rilis.txt` (tanggal UTC | provinsi | judul | slug). Mentah: pusat.json & prov_*.json di folder itu; detail via `https://<prov>.haji.go.id/api/news/<slug>` (pusat: `https://haji.go.id/api/news/<slug>`). Sebelum memakai rilis, pastikan slug-nya belum ada di field sources paket lama (`grep -l <potongan-slug> /home/khaeruddien/elharamain-news/*/*/article.json`).
- Ronde ini dibagi ke 6 subagen; tiap subagen hanya memakai sumber yang ditugaskan. Penugasan seluruh ronde (JANGAN ambil rilis milik slot lain):
  15:00 U&H (29): sumbar "Kemenhaj Sumbar Gandeng Polda, Perkuat Pengawasan Haji dan Umrah" (18 Nov). Nama travel DILARANG; angkat imbauan/pengawasan; beda dari 18794 (Itjen pelunasan). Cadangan: pusat "Kemenhaj Ajak Seluruh Jajaran Optimalkan Pelunasan Kuota Haji dengan Semangat 5K" (17 Nov; beda dari 18794 & 18796).
  19:40 U&H (29): bengkulu "PERMUDAH LAYANAN PASPOR JEMAAH, KEMENHAJ MUKOMUKO GANDENG KESBANGPOL UPAYAKAN UKK IMIGRASI" (18 Nov). Cadangan: pusat 5K (hanya bila 15:00 tidak memakainya).
  15:40 Berita (23): kalsel "Dirjen Pengendalian Haji dan Umrah Tekankan Pentingnya Pembinaan Jemaah dan Penertiban Dokumen Haji 1448 H/2027 M" (18 Nov). Cadangan: kalteng "Pastikan Kesiapan Lembaga, Kemenhaj Palangka Raya Visitasi KBIHU ..." (17 Nov; JANGAN tulis nama KBIHU/yayasan).
  17:40 Berita (23): sulsel "Sosialisasikan Regulasi Baru Pendaftaran hingga Pelunasan, Dirjen Kemenhaj Tekankan Pelayanan Sepenuh Hati" (17 Nov) — beda dari 18800 (data surat pendaftaran vs KTP) & 18794. Cadangan: kalsel "Tinjau Pembangunan PLHUT HSS, Dirjen Harun Al Rasyid Tekankan Kontraktor Tepati Jadwal" (18 Nov; beda dari post PLHUT Tabalong 12 Nov).
  21:00 Berita (23): rilis BPKH terbaru yang belum ditulis (SUDAH: 18803 BPKH-Lazismu mobil dakwah, 18668 target dana kelolaan 2027, 18630 kanal informasi; cek judul 14 hari). bpkh.go.id sering 403 — pakai liputan media allowlist; jangan mengakali. Cadangan: sulsel "Kemenhaj Barru Hadir di Mall Pelayanan Publik" (17 Nov).
  22:20 Lifestyle Muslim (32): sumut "Koordinasi Dinas Kesehatan Kota Pematangsiantar Dengan Kementerian Haji dan Umrah Kota Pematang Siantar" (17 Nov) → sudut persiapan kesehatan jemaah; beda dari 18801 (Maluku) & 18730 (Pulang Pisau) & Lifestyle 14 hari.
  16:20 NUSUK (29) dan 19:00 NUSUK (29) + 17:00 MEDIA ARAB (29/25) — satu subagen: cari kabar Nusuk BARU (setelah 18 Nov 04:43 WIB; Ronde A tadi pagi tak menemukan kabar baru, lihat ronde-a-1118/nusuk_kosong.txt) di SPA portalapi `https://portalapi.spa.gov.sa/api/v1/news?page=N&locale=en`, Arab News, haj.gov.sa. nusuk.sa memblokir bot sejak 13 Nov: jangan diakali. Bila tidak ada bahan baru, JANGAN mengarang; buat lebih sedikit (boleh 0) dan tulis alasannya di `ronde-b-1118/nusuk_kosong.txt`. MEDIA ARAB: berita Saudi 72 jam terakhir relevan jemaah, beda dari 18799 (Taman Al-Misfalah), 18806 (Qiblatain teh Madinah), "Taif Governor umrah services" boleh bila belum ditulis, dan Media Arab/Dunia islam 14 hari; foto SPA (tools/spa_credit.py untuk kredit).
  18:20 Kegiatan (24): pilih grup sendiri yang BELUM diberitakan. Pagi ini 18798 = 17 AGUSTUS 2026 Bronze — wajib grup lain (lihat bagian Kegiatan di bawah).
  20:20 Hikmah (28) dan 21:40 Wisata Halal (31) — satu subagen: evergreen, beda dari Hikmah/Wisata Halal 14 hari (cek c[28]/c[31]; Wisata Halal 14 hari hampir semua masjid Indonesia — boleh variasi destinasi religi lain, Indonesia/Turki/Mesir/Saudi, asal foto asli lolos aturan landmark).
- Slot NUSUK hanya 16:20 dan 19:00 (slot tengah 16:00/18:40/21:20 opsional bila bahan Nusuk benar-benar ada).

## Lingkungan
- Python gambar: `python3` sistem (Pillow 10.2 tersedia; /tmp/v TIDAK ada, jangan buat venv). ffmpeg di ~/.local/bin/ffmpeg.
- Kerja di folder `/home/khaeruddien/elharamain-news/ronde-b-1118/<SLOT>/` (SLOT mis. `1540`). Unduhan mentah di subfolder `raw/`.
- Cek tag: `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/tags?search=<kata>&_fields=id,name"` — pakai HANYA ID tag yang sudah ada (3-5 tag) + 34 (elharamain wisata).
- Link internal: cari via `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?search=<kata>&_fields=id,link,title"`; pakai URL `link` asli.
- WebSearch/WebFetch boleh (domain allowlist di prompt). Jangan mengakali 403/406.
- Ilustrasi AI (hanya bila aturan mengharuskan, mis. berita negatif): kamu TIDAK bisa membuatnya. Tulis prompt Inggris lengkap (sesuai aturan gaya foto dokumenter, wajah Indonesia/Arab, tanpa teks/logo/masjid) di article.json `images.N.ai_prompt` dan biarkan `file` kosong; induk yang membuat.

## Keluaran per artikel: `<SLOT>/article.json`
```json
{
 "slot": "2026-11-18T15:00:00",
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

- Kegiatan: baca/isi `/home/khaeruddien/elharamain-news/kegiatan-1118/klaim.txt` (tambahkan satu baris klaimmu: grup | folder | slot 2026-11-18T18:20 Ronde B | tema | jam klaim). Grup yang SUDAH diberitakan (JANGAN): 1448 H 19 Jul Platinum, 26 Jul Prem, 26 Jul Plat-Sil, 12 Jul Silver, 13 Jul Bronze, 20 Jul Bronze, 16 Jul 12H, 5 Agt Bronze, 12 Agt 12H, 17 Agt Bronze, 20 Agt Silver, 24 Agt Silver, 5 Nov 12H, 6 Nov Bronze, 8 Nov Plat-Sil, 9 Nov Bronze, serta semua judul Kegiatan di judul_14hari.txt dan arsip (cek `posts?categories=24&per_page=100`) dan klaim di kegiatan-11*/klaim.txt. Kandidat: grup Agustus 2026 lain (mis. 9 Agt Silver, 26-31 Agt) atau grup September/Oktober 1448 H yang belum ditulis.
