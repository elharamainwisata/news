# Brief subagen Ronde B, Minggu 22 Nov 2026 (dibuat agen News ±11:10 WIB)

Kamu menyiapkan PAKET ARTIKEL (naskah + gambar final di disk). Kamu TIDAK membuat post WordPress dan TIDAK mengunggah ke WordPress — agen induk yang mengunggah & menjadwalkan. TARGET: paket siap ≤ 13:15 WIB (cek `TZ=Asia/Jakarta date`); slot pertama terbit 15:00. Kerja cepat tapi aturan tetap utuh.

## Aturan wajib (baca dulu, utuh)
- `/home/khaeruddien/elharamain-news/routine/prompt_ronde_b.md` (aturan lengkap: gaya rumah, frasa AI terlarang, sortir, KEBIJAKAN TOPIK HAJI PLUS & UMROH, TIPS NUSUK & HIMPUH, GAMBAR & GERBANG GAMBAR, aturan haji.go.id/BPKH/MEDIA ARAB/Kegiatan). Jalankan persis untuk artikelmu, kecuali bagian membuat post/unggah (dikerjakan induk).
- `/home/khaeruddien/elharamain-news/ATURAN_REDAKSI.md`.
- KEBIJAKAN: utamakan HAJI PLUS/HAJI KHUSUS dan UMROH. Ronde A hari ini haji reguler = 0; Ronde B boleh MAKS 1 haji reguler hanya bila kebijakan nasional besar (sebaiknya 0). Berita haji reguler tingkat daerah (Kanwil/kab/kota: pelunasan reguler, paspor, manasik reguler, porsi wafat, PLHUT, UMKM, seremoni, evaluasi anggaran, embarkasi daerah, petugas/PPIH daerah, prodi kampus) TIDAK diambil. Ragu → ganti topik Haji Plus/Umroh.
- Judul situs 8-22 Nov (termasuk 12 post Ronde A hari ini): `/home/khaeruddien/elharamain-news/ronde-b-1122/judul_14hari.txt` (id tanggal c[kategori] judul). Topik WAJIB beda dari semua itu, terutama Ronde A hari ini: cadangan haji khusus tanpa pendamping (19229), tabungan haji santri OJK Cirebon (19230), niat ihram bersyarat (19231), lunas tunda/haji khusus tanpa antre (19025), Masjid As-Suqya (19232), BPJPH ekonomi halal 27% PDB (19233), Tasheel Card Nabawi Jumat (19234), Group Juni 2026 Bronze (19235), khutbah Jumat Haramain (19236), tawaf wada umrah (19237), Thaif destinasi wisata umrah (19238), 53 jemaah Boyolali tertahan di Bangkok (19239), mushaf pameran buku Kuwait (19240). Paket Ronde A ada di `ronde-a-1122/<slot>/article.json` (cek field sources agar tidak memakai sumber yang sama). Cek juga isi badan post bila topik mirip (`curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts/<id>?_fields=content"`).
- Seri Edukasi Haji Khusus 2027 (tag 2115, tiap 09:00 s.d. 1 Des) membahas: cek status, prioritas lansia, lunas tunda/penawaran tanpa antre, checklist dokumen, istithaah, tujuh tahapan, tiga kelompok pengisi kuota, cadangan, beda reguler-khusus, mitos, rukun haji, kalender pelunasan khusus — JANGAN dobel.
- Hindari topik draft lama yang ditahan (Pohuwato biometrik, PLHUT Manggarai, Dairi majelis taklim, visitasi Bogor, 311 calon PHD Jateng, KSrelief Flores, KBIHU Jabar, STAIN Majene) dan berita serangan/militer/politik.
- NAMA TRAVEL LAIN DILARANG disebut sama sekali (termasuk di slug link; lepas link bila slug memuat nama travel).
- Foto Elharamain sebagai ilustrasi (bukan dari kegiatan yang diberitakan) TANPA caption; "Foto ilustrasi: Dokumentasi Elharamain Wisata" DILARANG. Berita negatif: tanpa foto Elharamain → ilustrasi AI (induk yang membuat). Jangan pakai foto yang sudah dipakai 7 hari terakhir: cek paket di /home/khaeruddien/elharamain-news/ronde-a-11{15..22}, ronde-b-11{15..21} (article.json field images/evidence); bandingkan gambar post via `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?after=2026-11-15T00:00:00&per_page=100&_fields=id,title,jetpack_featured_media_url"`.
- Daftar rilis haji.go.id terbaru (pusat 50 + 10/provinsi, diambil 11:05 WIB; TIDAK ada rilis baru sejak 22 Nov 05:00 WIB): `ronde-b-1122/rilis.txt` (tanggal UTC | provinsi | judul | slug). Detail `https://<prov>.haji.go.id/api/news/<slug>` (pusat: `https://haji.go.id/api/news/<slug>`). referenceUrl provinsi sering kosong → link `https://<prov>.haji.go.id/berita/<slug>` (cek HTTP 200). Kandidat umrah yang mungkin belum ditulis (WAJIB cek judul_14hari + sources dulu): Bali shelter meeting point jemaah umrah (bali, 18 Nov), Kemenhaj Sumbar gandeng Polda awasi haji-umrah (17 Nov), Kemenhaj Riau panggil PPIU fasilitasi travel tanpa izin (18 Nov; tanpa nama travel), Papua Barat-Imigrasi awasi travel umrah (16 Nov). Bagasi Soetta (19159), Mukomuko (19152), HSS (19113), SIGAP Kaltim (19114) SUDAH ditulis.
- HIMPUH: https://himpuh.or.id (artikel `https://himpuh.or.id/blog/detail/<id>/<slug>`, terbaca curl). Hanya tips/panduan & info regulasi; tanpa nama travel/anggota/kasus/promosi; tulis ulang total; cek tanggal berlaku, tulis "per <bulan tahun>". Sudah dipakai: umrah Rajab (19118), stroller Masjidil Haram, pelunasan haji khusus 16% (19070), miqat (19066), asuransi perjalanan (19122), umrah musim dingin busana (19176), Tasheel Card (19234, blog 5294).
- Nusuk: www.nusuk.sa memblokir bot — jangan diakali. SPA: `https://portalapi.spa.gov.sa/api/v1/news?page=N&locale=en` (curl; teks + foto portalcdn).

## SLOT RONDE B (tiap subagen hanya memakai sumber yang ditugaskan; tulis pilihan sumbermu ke `<SLOT>/PILIHAN.txt` SEDINI MUNGKIN dan cek PILIHAN.txt slot lain + paket ronde-a-1122 agar tidak dobel)
  1500 U&H (29) #1 dan 1940 U&H (29) #2 [S1]: 1500 = berita UMROH/HAJI KHUSUS terbaru (48-72 jam) dari sumber resmi/allowlist (Kemenhaj pusat/provinsi kandidat umrah di atas, Antara/Republika/Kompas/Detik, Arab News bukan milik S4) — BUKAN Boyolali-Bangkok (19239), BUKAN Thaif (19238). 1940 = TIPS HIMPUH atau TIPS NUSUK bertopik UMROH praktis (blog HIMPUH yang belum dipakai; cek tanggal berlaku); beda dari tips yang sudah ada.
  1540 Berita (23) #1 dan 1740 Berita (23) #2 [S2]: 1540 = rilis BPKH terbaru yang belum ditulis (SUDAH: 19153, 19116, 18803, 18668; cek judul_14hari) — bpkh.go.id sering 403, pakai liputan allowlist; bila tak ada: berita Kemenag/zakat-wakaf/halal/ekonomi syariah 48 jam yang bersinggungan dengan jemaah (BUKAN 19233 BPJPH 27% PDB, BUKAN 19230 OJK Cirebon, BUKAN 19174). 1740 = Kemenag/pesantren/halal/ekonomi syariah 48 jam, topik beda dari 1540.
  2100 Berita (23) #3 dan 2220 Lifestyle Muslim (32) [S3]: 2100 = perlindungan jemaah UMROH/pengawasan PPIU/imigrasi/bandara 72 jam (kandidat provinsi di atas yang tidak dipakai S1 — koordinasi lewat ../1500/PILIHAN.txt; atau media allowlist), tanpa nama travel; BUKAN 19239/19152/19113/19114/19120. Bila tak ada: berita Kemenag/halal beda dari S2. 2220 = gaya hidup muslim/persiapan fisik/keuangan syariah/perlengkapan jemaah umrah (boleh berbasis TIPS HIMPUH/Kemenkes/haji.go.id yang terverifikasi), beda dari c[32] 14 hari (19176 busana musim dingin, dll.).
  1700 MEDIA ARAB (29/25) [S4]: berita Saudi 72 jam relevan jemaah (SPA portalapi/Arab News), beda dari MEDIA ARAB/c[25]/c[29] 14 hari (19236 khutbah, 19238 Thaif, 19240 mushaf Kuwait, 19161, 19160, 19172 cuaca, 19115, dll.). Foto SPA (tools/spa_credit.py untuk kredit "Foto: SPA"). Juga cek kabar Nusuk BARU (setelah 22 Nov 05:25 WIB) di SPA/Arab News; catat di `ronde-b-1122/nusuk.txt` (ada/kosong + sumber). Bila ada bahan Nusuk baru yang kuat, tulis 1 paket tambahan di folder `ronde-b-1122/1620/` (kategori 29, slot 16:20) — bila tidak, cukup catat kosong.
  2020 Hikmah (28) dan 2140 Wisata Halal (31) [S5]: Hikmah = renungan akhlak/ibadah dari kitab/ulama dengan sumber jelas (beda dari c[28] 14 hari: 19173 Riyadhus Shalihin sedekah tulang, 19119 sabar Ibnu Abid Dunya, dll.). Wisata Halal = destinasi religi/halal (Indonesia, Turki, Mesir, Saudi, Yordania, Uzbekistan...), beda dari c[31] 14 hari (19175 Masjid Biru, 19121 Amr bin Ash, dll.) dan dari 19238 Thaif & 19232 As-Suqya. Masjid/landmark WAJIB foto asli (aturan masjid + kredit pendek bila CC BY).
  1820 Kegiatan (24) [S6]: lihat bagian Kegiatan di bawah.

## Lingkungan
- Python gambar: `python3` sistem (Pillow tersedia; /tmp/v tidak ada, jangan buat venv). ffmpeg di ~/.local/bin/ffmpeg.
- Kerja di folder `/home/khaeruddien/elharamain-news/ronde-b-1122/<SLOT>/` (SLOT mis. `1500`). Unduhan mentah di `raw/` (JANGAN simpan HTML pihak ketiga di luar raw/).
- Cek tag: `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/tags?search=<kata>&_fields=id,name"` — pakai HANYA ID tag yang sudah ada (total 3-5 tag termasuk 34 "elharamain wisata").
- Link internal: `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?search=<kata>&_fields=id,link,title"`; pakai URL `link` asli.
- WebSearch/WebFetch boleh (domain allowlist di prompt). Jangan mengakali 403/406.
- Ilustrasi AI (hanya bila aturan mengharuskan, mis. berita negatif): kamu TIDAK membuatnya. Tulis prompt Inggris lengkap (gaya foto dokumenter sesuai aturan, wajah Indonesia/Arab, tanpa teks/logo/masjid) di `images.N.ai_prompt`, biarkan `file` kosong; induk yang membuat.

## Keluaran per artikel: `<SLOT>/article.json`
```json
{
 "slot": "2026-11-22T15:00:00",
 "category": 29,
 "title": "...", "excerpt": "140-160 karakter",
 "tags": [34, ...],
 "content_file": "content.html",
 "images": {
   "1": {"file": "/abs/path/utama.jpg", "alt": "...", "caption": "Foto: Kementerian Haji dan Umrah RI | Foto: Dokumentasi Elharamain Wisata | Ilustrasi | \"\" (stok/kredit-di-gambar/ilustrasi Elharamain)", "seen": "kalimat apa yang benar-benar terlihat", "evidence": "URL/caption/subfolder sumber", "ai_prompt": ""},
   "2": {...}
 },
 "sensitive": false,
 "topic_type": "HAJI PLUS|UMROH|HAJI REGULER|LAIN",
 "word_count": 0,
 "sources": ["url ..."],
 "haji_go_id": "pusat|dki|...|tidak + referenceUrl",
 "bpkh": "url rilis atau tidak",
 "notes": "catatan untuk redaktur, calon topik yang digugurkan + alasan"
}
```
`content.html` = blok Gutenberg (`<!-- wp:paragraph --><p>...</p><!-- /wp:paragraph -->`), pembuka `<strong>ELHARAMAIN NEWS</strong> –`, penutup praktis, lalu paragraf CTA miring persis dari prompt. Gambar 1 = foto utama (TIDAK ditaruh di content). Gambar sisipan N≥2: baris placeholder `%%IMG2%%` (sendirian di barisnya) di antara blok paragraf; induk menggantinya dengan blok wp:image.
Gambar final: JPEG q82, foto utama 16:9 lebar 1600 (min 1200), sisipan 4:5 atau 16:9. Read setiap gambar final (gerbang gambar 6 langkah) sebelum dimasukkan. Hindari kursi roda, close-up wajah anak.
Cek akhir: `python3 /home/khaeruddien/elharamain-news/ronde-b-1122/fin.py <SLOT_DIR>` (hitung kata, frasa terlarang, CTA, pembuka). 450-600 kata (Kegiatan 450-650). Tanpa tanda pisah panjang (—), tanpa subjudul/bullet. Link keluar MAKSIMAL 1 (sumber utama); link internal, CTA WA, elharamainwisata.com tidak dihitung.

Laporan akhirmu ke induk: ringkas (slot, judul, path article.json, gambar + apa yang terlihat, sumber, calon digugurkan). Jangan tempel naskah lengkap.

## Kegiatan [S6]
Grup diklaim di `/home/khaeruddien/elharamain-news/kegiatan-1122/klaim.txt` = 3 JULI 2026 (pilih salah satu: SILVER, PLAT, atau BRONZE; folder di 1448 H/2.JULI 2026 di bawah album 1cmzsm7NsKxb9LB_DqHzEuigNgm4frkNv). Ronde A hari ini SUDAH memakai 25 JUNI 2026 BRONZE (19235) — jangan dipakai. Cek semua judul c[24] (`curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?categories=24&per_page=100&_fields=id,title,date"` juga page=2) agar grup belum pernah ditulis. Bila album 3 Juli didominasi foto keberangkatan, pilih 5 JULI 12 HARI atau 6 JULI BRONZE dan perbarui klaim.txt. Tanpa tanggal keberangkatan di teks mana pun (cukup "Group Juli 2026 Silver"); tanpa maskapai/kota asal/bandara. Semua gambar hanya dari album Drive itu, caption "Foto: Dokumentasi Elharamain Wisata"; 2-3 sisipan. Bandingkan dengan artikel grup Juni/Juli lain (19235, 19154, 19117, 19067, 18966, 18916) agar foto/tema tidak kembar. Skrip lembar kontak: ronde-b-1122/sheet.py. Tambahkan baris "-> SELESAI <jam> (Ronde B 18:20): paket ... foto ..." ke klaim.txt.
