# Brief subagen Ronde A, Rabu 18 Nov 2026 (dibuat agen News 05:20 WIB)

Kamu menyiapkan PAKET ARTIKEL (naskah + gambar final di disk). Kamu TIDAK membuat post WordPress dan TIDAK mengunggah ke WordPress — agen induk yang mengunggah & menjadwalkan.

## Aturan wajib (baca dulu, utuh)
- `/home/khaeruddien/elharamain-news/routine/prompt_ronde_a.md` (aturan lengkap: gaya rumah, frasa AI terlarang, sortir, GAMBAR & GERBANG GAMBAR, aturan haji.go.id/BPKH/MEDIA ARAB/Kegiatan/Nusuk). Jalankan persis untuk artikelmu, kecuali bagian membuat post/unggah (dikerjakan induk).
- `/home/khaeruddien/elharamain-news/ATURAN_REDAKSI.md`.
- Judul situs 4-17 Nov: `/home/khaeruddien/elharamain-news/ronde-a-1118/judul_14hari.txt` (urut terbaru dulu, format: id tanggal c[kategori] judul). Topik WAJIB beda dari semua itu (termasuk Ronde B kemarin 18721-18730 & 18772 Nusuk undian umrah gratis). Hari ini belum ada post sama sekali.
- Juga hindari topik draft lama yang ditahan (Pohuwato biometrik, PLHUT Manggarai, Dairi majelis taklim, visitasi Bogor, moratorium 3.600 PPIU, 311 calon PHD Jateng, KSrelief Flores, Yayasan Sultan bin Abdulaziz & UNESCO).
- Foto Elharamain sebagai ilustrasi (bukan dari kegiatan yang diberitakan) TANPA caption; "Foto ilustrasi: Dokumentasi Elharamain Wisata" DILARANG. Jangan pakai foto yang sudah dipakai 7 hari terakhir: cek paket di /home/khaeruddien/elharamain-news/ronde-a-1117, ronde-b-1117, ronde-b-1116, cadangan-b-1116, ronde-a-1116, ronde-a-1114, ronde-b-1114, tambahan-1117 (article.json field images/evidence); bila ragu bandingkan gambar post terbit via `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?after=2026-11-11T00:00:00&per_page=100&_fields=id,title,jetpack_featured_media_url"`.
- Daftar rilis haji.go.id 4-17 Nov: `rilis.txt` (tanggal UTC | provinsi | judul | slug; tanda [DIPAKAI] tidak lengkap — cek juga judul_14hari.txt). Mentah: pusat.json & prov_*.json di folder ini; detail via `https://<prov>.haji.go.id/api/news/<slug>` (pusat: `https://haji.go.id/api/news/<slug>`).
- Ronde ini dibagi ke 7 subagen; tiap subagen hanya memakai sumber yang ditugaskan. Penugasan seluruh ronde (JANGAN ambil rilis milik slot lain):
  07:00 U&H (29): pusat "Inspektur Wilayah III Kemenhaj Tegaskan Pengawasan Pelunasan Haji 2027, Cegah Pungli dan Travel Ilegal" (16 Nov). Nama travel DILARANG; angkat imbauan. Beda dari 17169 & 17222.
  07:40 Berita (23): dki "Matangkan Kesiapan Diklat PPIH 1448 H/2027 M, Kepala Kanwil Kemenhaj DKI Jakarta Tekankan Persiapan Menyeluruh" (17 Nov). Beda dari 18663 (ToT PPIH Saudi) & 18522.
  09:00 U&H (29): kaltim "Kemenhaj Kaltim Dalami Aplikasi SIGAP, Pengaduan Haji dan Umrah ..." (17 Nov) — WAJIB info baru dibanding 17169 (SIGAP 7 Nov); bila tak ada info baru, pakai cadangan kepri "PROGRES PELUNASAN HAJI 1448 H/2027 M PROVINSI KEPRI CAPAI 22,26 PERSEN" (17 Nov; beda dari 18728 Sulsel & 18666 Batam).
  10:20 Berita (23): sulteng "Pemprov Sulteng dan Kemenhaj Matangkan Kesiapan Sulawesi Tengah Menuju Embarkasi Haji Antara" (17 Nov) — sudut perkembangan baru dibanding 16885 (4 Nov). Cadangan: diy "Perkuat Sinergi Lintas Sektoral, Kemenhaj DIY Gelar Evaluasi dan Matangkan Kesiapan Embarkasi YIA 1448 H/2027 M" (16 Nov).
  12:20 Tanya Jawab (30): bengkulu "Kemenhaj Bengkulu Utara Ikuti Sosialisasi Pendaftaran dan Pembatalan Haji Tahun 1448 H" (17 Nov) → satu pertanyaan jemaah (mis. syarat/ketentuan pendaftaran atau pembatalan haji 1448 H), rujuk aturan resmi yang terbaca; beda dari 18672, 18313, 18427. Cadangan: sumut "Sosialisasi Layanan Data Keimigrasian" (17 Nov; beda dari 17841).
  13:00 U&H (29): maluku "Haji 2027 Makin Dekat, Jemaah Maluku Diimbau Siapkan Kesehatan" (17 Nov) — beda dari 18518 & 18315 (Maluku). Cadangan: sumut "Koordinasi Dinas Kesehatan Kota Pematangsiantar Dengan Kementerian Haji dan Umrah Kota Pematang Siantar" (17 Nov).
  Kepri pelunasan hanya boleh dipakai slot 09:00 (cadangan); DIY YIA hanya 10:20 atau 13:40 (cadangan) — koordinasi: 13:40 hanya memakai DIY bila 10:20 tidak memakainya (10:20 menulis pilihannya ke `1020/PILIHAN.txt` sedini mungkin).
  08:20 Fiqih (26) dan 09:40 Sejarah Islam (27) — satu subagen: evergreen, beda dari Fiqih/Sejarah 14 hari (cek c[26]/c[27]).
  13:40 Berita (23): rilis BPKH terbaru yang belum ditulis (SUDAH: 18668 target dana kelolaan 2027, 18630 kanal informasi). bpkh.go.id sering 403 — pakai liputan media allowlist; jangan mengakali. Cadangan: diy YIA (lihat koordinasi) atau sumut "Kemenhaj Kota Binjai Hadiri Sosialisasi PMHU Nomor 5 Tahun 2026 tentang KBIHU" (17 Nov; beda dari 18414).
  08:00 / 10:40 / 13:20 NUSUK (29) — subagen yang sama dengan 13:40: cari kabar Nusuk BARU (setelah 17 Nov pagi; 18772 undian umrah gratis Nusuk SUDAH ditulis) di SPA portalapi `https://portalapi.spa.gov.sa/api/v1/news?page=N&locale=en`, Arab News, haj.gov.sa. nusuk.sa memblokir bot sejak 13 Nov: jangan diakali. Bila tidak ada bahan baru, JANGAN mengarang; buat lebih sedikit (boleh 0) dan tulis alasannya di `nusuk_kosong.txt`.
  11:40 MEDIA ARAB (29/25) dan 14:20 Dunia islam (25) — satu subagen: dua berita Saudi/dunia Muslim BERBEDA, 72 jam terakhir, relevan jemaah, beda dari c[25] 14 hari (mis. Presiden Mauritania di Nabawi, Corniche Jeddah, Pekan Riset UIM). MEDIA ARAB pakai foto SPA (tools/spa_credit.py untuk kredit "Foto: SPA"). Dunia islam boleh SPA/Arab News/Antara; gambar ikuti aturan.
  11:00 Kegiatan (24): pilih grup sendiri yang BELUM diberitakan (lihat bagian Kegiatan di bawah).

## Lingkungan
- Python gambar: `python3` sistem (Pillow 10.2 tersedia; /tmp/v TIDAK ada, jangan buat venv). ffmpeg di ~/.local/bin/ffmpeg.
- Kerja di folder `/home/khaeruddien/elharamain-news/ronde-a-1118/<SLOT>/` (SLOT mis. `1540`). Unduhan mentah di subfolder `raw/`.
- Cek tag: `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/tags?search=<kata>&_fields=id,name"` — pakai HANYA ID tag yang sudah ada (3-5 tag) + 34 (elharamain wisata).
- Link internal: cari via `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?search=<kata>&_fields=id,link,title"`; pakai URL `link` asli.
- WebSearch/WebFetch boleh (domain allowlist di prompt). Jangan mengakali 403/406.
- Ilustrasi AI (hanya bila aturan mengharuskan, mis. berita negatif): kamu TIDAK bisa membuatnya. Tulis prompt Inggris lengkap (sesuai aturan gaya foto dokumenter, wajah Indonesia/Arab, tanpa teks/logo/masjid) di article.json `images.N.ai_prompt` dan biarkan `file` kosong; induk yang membuat.

## Keluaran per artikel: `<SLOT>/article.json`
```json
{
 "slot": "2026-11-18T07:00:00",
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
- Kegiatan: baca/isi `/home/khaeruddien/elharamain-news/kegiatan-1118/klaim.txt` (buat bila belum ada; tambahkan satu baris klaimmu: grup | folder | slot 2026-11-18T11:00 Ronde A | tema | jam klaim). Grup yang SUDAH diberitakan (JANGAN): 1448 H 19 Jul Platinum, 26 Jul Prem, 26 Jul Plat-Sil, 12 Jul Silver, 13 Jul Bronze, 20 Jul Bronze, 16 Jul 12H, 5 Agt Bronze, 12 Agt 12H, 20 Agt Silver, 24 Agt Silver, 5 Nov 12H, 6 Nov Bronze, 8 Nov Plat-Sil, 9 Nov Bronze, serta semua judul Kegiatan (c[24]) di judul_14hari.txt dan arsip (cek `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?categories=24&per_page=100&_fields=id,title,date"`, juga page=2). Lihat juga klaim di ../kegiatan-11*/klaim.txt. Kandidat: grup Agustus/September/Oktober 2026 (1448 H) yang belum ditulis.
