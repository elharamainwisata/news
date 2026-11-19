# Brief subagen Ronde A, Jumat 20 Nov 2026 (dibuat agen News 05:15 WIB)

Kamu menyiapkan PAKET ARTIKEL (naskah + gambar final di disk). Kamu TIDAK membuat post WordPress dan TIDAK mengunggah ke WordPress — agen induk yang mengunggah & menjadwalkan.

## Aturan wajib (baca dulu, utuh)
- `/home/khaeruddien/elharamain-news/routine/prompt_ronde_a.md` (aturan lengkap: gaya rumah, frasa AI terlarang, sortir, KEBIJAKAN TOPIK HAJI PLUS & UMROH (BERLAKU MULAI HARI INI 20 Nov), TIPS NUSUK & HIMPUH, GAMBAR & GERBANG GAMBAR, aturan haji.go.id/BPKH/MEDIA ARAB/Kegiatan). Jalankan persis untuk artikelmu, kecuali bagian membuat post/unggah (dikerjakan induk).
- `/home/khaeruddien/elharamain-news/ATURAN_REDAKSI.md`.
- KEBIJAKAN HARI INI: utamakan HAJI PLUS/HAJI KHUSUS dan UMROH. Haji reguler maks 1 artikel per hari (hanya kebijakan nasional besar) — Ronde A TIDAK mengambil haji reguler kecuali disebut di penugasan. Berita haji reguler tingkat daerah (Kanwil/kab/kota: pelunasan reguler, paspor, manasik reguler, UMKM haji daerah, seremoni) TIDAK diambil.
- Judul situs 5-19 Nov: `/home/khaeruddien/elharamain-news/ronde-a-1120/judul_14hari.txt` (urut terbaru, format: id tanggal c[kategori] judul). Topik WAJIB beda dari semua itu. Hari ini sudah ada 19023 (09:00, seri Edukasi Haji Khusus 2027: "Tiga Langkah Cek Status Haji Khusus 2027, dari Nomor Porsi hingga Konfirmasi ke PIHK"). Seri itu (tag 2115, 19023-19034) membahas: cek status, prioritas lansia, lunas tunda/penawaran tanpa antre, checklist dokumen, istithaah, tujuh tahapan, tiga kelompok pengisi kuota, cadangan, beda reguler-khusus, mitos, rukun haji, kalender pelunasan khusus — JANGAN dobel.
- Hindari juga topik draft lama yang ditahan (Pohuwato biometrik, PLHUT Manggarai, Dairi majelis taklim, visitasi Bogor, moratorium 3.600 PPIU, 311 calon PHD Jateng, KSrelief Flores, Yayasan Sultan bin Abdulaziz & UNESCO).
- Foto Elharamain sebagai ilustrasi (bukan dari kegiatan yang diberitakan) TANPA caption; "Foto ilustrasi: Dokumentasi Elharamain Wisata" DILARANG. Jangan pakai foto yang sudah dipakai 7 hari terakhir: cek paket di /home/khaeruddien/elharamain-news/ronde-a-1119, ronde-b-1119, ronde-a-1118, ronde-b-1118, ronde-a-1117, ronde-b-1117, ronde-b-1116, haji-khusus-2027 (article.json field images/evidence); bila ragu bandingkan gambar post terbit via `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?after=2026-11-13T00:00:00&per_page=100&_fields=id,title,jetpack_featured_media_url"`.
- Daftar rilis haji.go.id 6-19 Nov: `rilis.txt` (tanggal UTC | provinsi | judul | slug). WAJIB cek judul_14hari.txt agar rilis belum dipakai. Mentah: pusat.json & prov_*.json; detail via `https://<prov>.haji.go.id/api/news/<slug>` (pusat: `https://haji.go.id/api/news/<slug>`). referenceUrl provinsi sering kosong → link `https://<prov>.haji.go.id/berita/<slug>` (cek HTTP 200).
- HIMPUH: https://himpuh.or.id (artikel `https://himpuh.or.id/blog/detail/<id>/<slug>`, terbaca curl). Hanya tips/panduan & info regulasi; tanpa nama travel/anggota/kasus/promosi; tulis ulang total; cek tanggal berlaku, tulis "per <bulan tahun>".
- Tiap subagen hanya memakai sumber yang ditugaskan. Penugasan seluruh ronde (JANGAN ambil rilis milik slot lain):
  07:00 U&H (29) [S1]: kepri "KANWIL KEMENHAJ KEPRI SOSIALISASIKAN PMHU NOMOR 2 TAHUN 2026 ..." (19 Nov) → angkat isi PMHU 2/2026 (cek apakah tentang umrah/PPIU; nama travel di judul rilis DILARANG disebut — tulis "sebuah biro perjalanan" atau jangan sebut sama sekali). Cadangan: pusat "Kemenhaj Dorong PIHK dan PPIU Patuhi Regulasi..." (12 Nov) bila belum ditulis (cek judul).
  07:40 Berita (23) [S1]: jabar "Aturan Baru KBIHU Resmi Berlaku, Jemaah Haji dan Umrah Jabar Dijamin Lebih Terlindungi" (19 Nov). Beda sudut dari 18414 (seleksi pembimbing KBIHU) & 17383. Cadangan: sulbar "Kemenhaj Sulbar Dukung STAIN Majene Buka Prodi Manajemen Haji dan Umrah" (19 Nov).
  10:40 U&H (29) [S2] (slot digeser dari 09:00 karena 09:00 diisi seri Edukasi): TIPS HIMPUH atau TIPS NUSUK bertopik UMROH praktis (mis. aturan umrah terbaru, miqat, persiapan musim dingin, adab di Haram) — beda dari layanan Nusuk yang sudah ditulis (lihat judul Nusuk 11-19 Nov).
  13:00 U&H (29) [S2]: topik HAJI PLUS/HAJI KHUSUS (berita resmi terbaru Kemenhaj/HIMPUH/media allowlist tentang PIHK, kuota/BPIH khusus, regulasi haji khusus 1448 H) atau explainer haji khusus terverifikasi yang TIDAK dobel dengan seri Edukasi (tag 2115).
  08:20 Fiqih (26) dan 09:40 Sejarah Islam (27) [S3]: evergreen, beda dari c[26]/c[27] 14 hari; Fiqih utamakan manasik umrah.
  12:20 Tanya Jawab (30) [S4]: satu pertanyaan jemaah UMROH/haji khusus, jawaban berbasis rujukan ulama/regulasi resmi (sumber jelas); beda dari c[30] 14 hari.
  10:20 Berita (23) dan 13:40 Berita (23) [S5]: (a) rilis BPKH terbaru yang belum ditulis (SUDAH: 18803 mobil dakwah Lazismu, 18668 target dana kelolaan 2027, 18630 kanal informasi) — bpkh.go.id sering 403, pakai liputan media allowlist; (b) berita Kemenag/halal/ekonomi syariah/pesantren 48 jam terakhir dari media allowlist yang bersinggungan dengan jemaah umrah/haji. Cadangan: sulbar Majene (hanya bila 07:40 tidak memakainya; S1 tulis pilihannya ke `0740/PILIHAN.txt` sedini mungkin). JANGAN haji reguler daerah.
  11:40 MEDIA ARAB (29/25) dan 14:20 Dunia islam (25) [S6]: dua berita Saudi/dunia Muslim BERBEDA, 72 jam terakhir, relevan jemaah, beda dari c[25]/MEDIA ARAB 14 hari (mis. 18964 Nabawi Nusuk, 18917 As-Sudais AI, 18921 seni Islam). MEDIA ARAB pakai foto SPA (tools/spa_credit.py untuk kredit "Foto: SPA"). SPA: `https://portalapi.spa.gov.sa/api/v1/news?page=N&locale=en`.
  08:00 / 13:20 NUSUK (29) [S6 juga]: cek kabar Nusuk BARU (setelah 19 Nov 11:00 WIB; daftar sudah ditulis: lihat ../ronde-b-1119/nusuk_kosong.txt dan judul Nusuk). nusuk.sa memblokir bot: jangan diakali. Bila tidak ada bahan baru, JANGAN mengarang; tulis alasan di `nusuk_kosong.txt` (0 artikel itu wajar).
  11:00 Kegiatan (24) [S7]: lihat bagian Kegiatan di bawah.

## Lingkungan
- Python gambar: `python3` sistem (Pillow 10.2 tersedia; /tmp/v TIDAK ada, jangan buat venv). ffmpeg di ~/.local/bin/ffmpeg.
- Kerja di folder `/home/khaeruddien/elharamain-news/ronde-a-1120/<SLOT>/` (SLOT mis. `1540`). Unduhan mentah di subfolder `raw/`.
- Cek tag: `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/tags?search=<kata>&_fields=id,name"` — pakai HANYA ID tag yang sudah ada (3-5 tag) + 34 (elharamain wisata).
- Link internal: cari via `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?search=<kata>&_fields=id,link,title"`; pakai URL `link` asli.
- WebSearch/WebFetch boleh (domain allowlist di prompt). Jangan mengakali 403/406.
- Ilustrasi AI (hanya bila aturan mengharuskan, mis. berita negatif): kamu TIDAK bisa membuatnya. Tulis prompt Inggris lengkap (sesuai aturan gaya foto dokumenter, wajah Indonesia/Arab, tanpa teks/logo/masjid) di article.json `images.N.ai_prompt` dan biarkan `file` kosong; induk yang membuat.

## Keluaran per artikel: `<SLOT>/article.json`
```json
{
 "slot": "2026-11-20T07:00:00",
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
- Kegiatan: baca/isi `/home/khaeruddien/elharamain-news/kegiatan-1120/klaim.txt` (buat bila belum ada; tambahkan satu baris klaimmu: grup | folder | slot 2026-11-20T11:00 Ronde A | tema | jam klaim). Daftar grup bebas & yang sudah ditulis: `/home/khaeruddien/elharamain-news/kegiatan-1119/klaim.txt` (22 Juni Platinum = 18916 dan 24 Juni Premium = 18966 SUDAH ditulis kemarin). Cek juga semua judul c[24] (`curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?categories=24&per_page=100&_fields=id,title,date"`, juga page=2) dan ../kegiatan-11*/klaim.txt. Kandidat: 14 Juni Bronze/Silver, 21 Juni Silver, 25 Juni Bronze, 3 Juli, 5 Juli 12 Hari, 6 Juli Bronze (1448 H). Tanpa tanggal keberangkatan di teks mana pun (cukup "Group Juni 2026 Silver").
