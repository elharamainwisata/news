# Brief subagen Ronde A, Kamis 19 Nov 2026 (dibuat agen News 05:10 WIB)

Kamu menyiapkan PAKET ARTIKEL (naskah + gambar final di disk). Kamu TIDAK membuat post WordPress dan TIDAK mengunggah ke WordPress — agen induk yang mengunggah & menjadwalkan.

## Aturan wajib (baca dulu, utuh)
- `/home/khaeruddien/elharamain-news/routine/prompt_ronde_a.md` (aturan lengkap: gaya rumah, frasa AI terlarang, sortir, GAMBAR & GERBANG GAMBAR, aturan haji.go.id/BPKH/MEDIA ARAB/Kegiatan/Nusuk). Jalankan persis untuk artikelmu, kecuali bagian membuat post/unggah (dikerjakan induk).
- `/home/khaeruddien/elharamain-news/ATURAN_REDAKSI.md`.
- Judul situs 4-18 Nov: `/home/khaeruddien/elharamain-news/ronde-a-1119/judul_14hari.txt` (urut terbaru dulu, format: id tanggal c[kategori] judul). Topik WAJIB beda dari semua itu (termasuk Ronde B kemarin 18855-18864). Hari ini belum ada post sama sekali.
- Juga hindari topik draft lama yang ditahan (Pohuwato biometrik, PLHUT Manggarai, Dairi majelis taklim, visitasi Bogor, moratorium 3.600 PPIU, 311 calon PHD Jateng, KSrelief Flores, Yayasan Sultan bin Abdulaziz & UNESCO).
- Foto Elharamain sebagai ilustrasi (bukan dari kegiatan yang diberitakan) TANPA caption; "Foto ilustrasi: Dokumentasi Elharamain Wisata" DILARANG. Jangan pakai foto yang sudah dipakai 7 hari terakhir: cek paket di /home/khaeruddien/elharamain-news/ronde-a-1118, ronde-b-1118, ronde-a-1117, ronde-b-1117, ronde-b-1116, cadangan-b-1116, ronde-a-1116, tambahan-1117 (article.json field images/evidence); bila ragu bandingkan gambar post terbit via `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?after=2026-11-12T00:00:00&per_page=100&_fields=id,title,jetpack_featured_media_url"`.
- Daftar rilis haji.go.id 4-18 Nov: `rilis.txt` (tanggal UTC | provinsi | judul | slug; tanda [DIPAKAI] TIDAK lengkap — WAJIB cek juga judul_14hari.txt, mis. Dirjen Harun mahram (18856), Sumbar-Polda (18855), regulasi Makassar (18858), Mukomuko paspor (18860), Barru MPP (18862) sudah ditulis). Mentah: pusat.json & prov_*.json di folder ini; detail via `https://<prov>.haji.go.id/api/news/<slug>` (pusat: `https://haji.go.id/api/news/<slug>`). referenceUrl provinsi sering kosong → link dibentuk `https://<prov>.haji.go.id/berita/<slug>` (cek HTTP 200).
- Ronde ini dibagi ke 7 subagen; tiap subagen hanya memakai sumber yang ditugaskan. Penugasan seluruh ronde (JANGAN ambil rilis milik slot lain):
  07:00 U&H (29): dki "Verifikasi Jemaah BATU Haji Reguler, Kanwil Kemenhaj DKI Jakarta Perkuat Akurasi Data dan Pemetaan Keberangkatan Jemaah" (18 Nov). Cadangan: kalteng "Monitor Pelunasan Bipih 1448 H ke BPS Bipih ..." (18 Nov).
  07:40 Berita (23): dki "Kepala Kanwil Kemenhaj DKI Jakarta Perkuat Sinergi dengan Dinas Kesehatan, Matangkan Kesiapan Layanan Kesehatan Haji 1448 H/2027 M" (18 Nov). Beda dari 18795 (diklat PPIH DKI). Cadangan: sumsel "Wujudkan Pelayanan Humanis ... Service Excellence" hanya bila ada nilai bagi jemaah.
  09:00 U&H (29): pusat "Puskes Haji Kemenhaj dan Dinkes Kota Bekasi Evaluasi Pemeriksaan Kesehatan, Tarif, dan Kesiapan Layanan Haji" (17 Nov) — boleh tambah konteks dari rilis pusat "Puskes Haji Kemenhaj dan RSUD Kota Bekasi ..." (17 Nov 22:58) karena peristiwa sama (satu artikel saja). Cadangan: sumbar "Pelunasan Haji Sumbar Baru 26,4 Persen ..." (18 Nov).
  10:20 Berita (23): bali "Angkasa Pura I Rancang Shelter Meeting Point Jemaah Umrah Bali" (18 Nov). Cadangan: gorontalo "Dari Gorontalo ke Arab Saudi, Produk UMKM Dibidik Masuk Rantai Pasok Haji" (17 Nov).
  12:20 Tanya Jawab (30): gorontalo "Kakan Kemenhaj.....Tidak semua jemaah haji terpisah dari mahromnya dapat digabungkan berangkat haji bersama" (17 Nov) → satu pertanyaan jemaah soal syarat penggabungan mahram/pendamping; WAJIB sudut beda dari 18856 (Dirjen minta verifikasi dokumen mahram diperketat) dan 18800. Cadangan: bengkulu "Antrean Haji di Mukomuko Capai 4.536 Jemaah, Kemenhaj Dorong Program Haji Muda" (18 Nov) → pertanyaan soal mendaftar haji di usia muda (beda dari 18615 Dairi & 18860).
  13:00 U&H (29): riau "Kemenhaj Riau Panggil PPIU Terkait Fasilitasi Travel Umrah Tanpa Izin" (18 Nov) — BERITA NEGATIF: NAMA TRAVEL/PPIU DILARANG disebut; angkat imbauan (cek izin PPIU, dll.); gambar ilustrasi AI (tulis ai_prompt). Cadangan: sumbar pelunasan 26,4% (hanya bila 09:00 tidak memakainya; 09:00 menulis pilihannya ke `0900/PILIHAN.txt` sedini mungkin).
  08:20 Fiqih (26) dan 09:40 Sejarah Islam (27) — satu subagen: evergreen, beda dari Fiqih/Sejarah 14 hari (cek c[26]/c[27]).
  13:40 Berita (23): rilis BPKH terbaru yang belum ditulis (SUDAH: 18803 mobil dakwah Lazismu, 18668 target dana kelolaan 2027, 18630 kanal informasi). bpkh.go.id sering 403 — pakai liputan media allowlist; jangan mengakali. Cadangan: pusat "Kemenhaj Ajak Seluruh Jajaran Optimalkan Pelunasan Kuota Haji dengan Semangat 5K" (17 Nov) atau gorontalo UMKM (bila 10:20 tidak memakainya).
  08:00 / 10:40 / 13:20 NUSUK (29) — subagen yang sama dengan 13:40: cari kabar Nusuk BARU (setelah 18 Nov pagi; lihat ../ronde-a-1118/nusuk_kosong.txt untuk daftar topik Nusuk yang SUDAH ditulis) di SPA portalapi `https://portalapi.spa.gov.sa/api/v1/news?page=N&locale=en`, Arab News, haj.gov.sa. nusuk.sa memblokir bot sejak 13 Nov: jangan diakali. Bila tidak ada bahan baru, JANGAN mengarang; buat lebih sedikit (boleh 0) dan tulis alasannya di `nusuk_kosong.txt`.
  11:40 MEDIA ARAB (29/25) dan 14:20 Dunia islam (25) — satu subagen: dua berita Saudi/dunia Muslim BERBEDA, 72 jam terakhir, relevan jemaah, beda dari c[25] 14 hari (mis. Menara Jam Guinness 18857, Qiblatain 18806, Al-Misfalah 18799, Presiden Mauritania 18723). MEDIA ARAB pakai foto SPA (tools/spa_credit.py untuk kredit "Foto: SPA"). Dunia islam boleh SPA/Arab News/Antara; gambar ikuti aturan.
  11:00 Kegiatan (24): pilih grup sendiri yang BELUM diberitakan (lihat bagian Kegiatan di bawah).

## Lingkungan
- Python gambar: `python3` sistem (Pillow 10.2 tersedia; /tmp/v TIDAK ada, jangan buat venv). ffmpeg di ~/.local/bin/ffmpeg.
- Kerja di folder `/home/khaeruddien/elharamain-news/ronde-a-1119/<SLOT>/` (SLOT mis. `1540`). Unduhan mentah di subfolder `raw/`.
- Cek tag: `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/tags?search=<kata>&_fields=id,name"` — pakai HANYA ID tag yang sudah ada (3-5 tag) + 34 (elharamain wisata).
- Link internal: cari via `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?search=<kata>&_fields=id,link,title"`; pakai URL `link` asli.
- WebSearch/WebFetch boleh (domain allowlist di prompt). Jangan mengakali 403/406.
- Ilustrasi AI (hanya bila aturan mengharuskan, mis. berita negatif): kamu TIDAK bisa membuatnya. Tulis prompt Inggris lengkap (sesuai aturan gaya foto dokumenter, wajah Indonesia/Arab, tanpa teks/logo/masjid) di article.json `images.N.ai_prompt` dan biarkan `file` kosong; induk yang membuat.

## Keluaran per artikel: `<SLOT>/article.json`
```json
{
 "slot": "2026-11-19T07:00:00",
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
- Kegiatan: baca/isi `/home/khaeruddien/elharamain-news/kegiatan-1119/klaim.txt` (buat bila belum ada; tambahkan satu baris klaimmu: grup | folder | slot 2026-11-19T11:00 Ronde A | tema | jam klaim). Grup yang SUDAH diberitakan (JANGAN): 1448 H 19 Jul Platinum, 26 Jul Prem, 26 Jul Plat-Sil, 12 Jul Silver, 13 Jul Bronze, 20 Jul Bronze, 16 Jul 12H, 5 Agt Bronze, 12 Agt 12H, 20 Agt Silver, 24 Agt Silver, 5 Nov 12H, 6 Nov Bronze, 8 Nov Plat-Sil, 9 Nov Bronze, 17 Agt Bronze, 9 Agt Silver, 20 Agt Silver, 24 Agt Silver, Agustus 12 Hari (18634), serta semua judul Kegiatan (c[24]) di judul_14hari.txt dan arsip (cek `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?categories=24&per_page=100&_fields=id,title,date"`, juga page=2). Lihat juga klaim di ../kegiatan-11*/klaim.txt. Kandidat: grup Agustus/September/Oktober 2026 (1448 H) yang belum ditulis.
