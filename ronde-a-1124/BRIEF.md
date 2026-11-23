# Brief subagen Ronde A, Selasa 24 Nov 2026 (dibuat agen News ±05:10 WIB)

Kamu menyiapkan PAKET ARTIKEL (naskah + gambar final di disk). Kamu TIDAK membuat post WordPress dan TIDAK mengunggah ke WordPress — agen induk yang mengunggah & menjadwalkan. TARGET: paket siap ≤ 06:20 WIB (cek `TZ=Asia/Jakarta date`); slot pertama terbit 07:00. Kerja cepat tapi aturan tetap utuh.

## Aturan wajib (baca dulu, utuh)
- `/home/khaeruddien/elharamain-news/routine/prompt_ronde_a.md` (aturan lengkap: gaya rumah, frasa AI terlarang, sortir, KEBIJAKAN TOPIK HAJI PLUS & UMROH, TIPS NUSUK & HIMPUH, GAMBAR & GERBANG GAMBAR, aturan haji.go.id/BPKH/MEDIA ARAB/Kegiatan). Jalankan persis untuk artikelmu, kecuali bagian membuat post/unggah (dikerjakan induk).
- `/home/khaeruddien/elharamain-news/ATURAN_REDAKSI.md`.
- KEBIJAKAN: utamakan HAJI PLUS/HAJI KHUSUS dan UMROH. Ronde A hari ini TIDAK mengambil haji reguler. Berita haji reguler tingkat daerah (Kanwil/kab/kota: pelunasan reguler, paspor, manasik reguler, porsi wafat, PLHUT, UMKM, seremoni, senam/jalan sehat pegawai, pembinaan pegawai, evaluasi anggaran) TIDAK diambil. Ragu reguler/daerah → ganti topik Haji Plus/Umroh.
- Judul situs 9-23 Nov: `/home/khaeruddien/elharamain-news/ronde-a-1124/judul_14hari.txt` (urut terbaru: id tanggal c[kategori] judul). Topik WAJIB beda dari semua itu; cek juga isi badan post bila topik mirip (`curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts/<id>?_fields=content"`). Seri Edukasi Haji Khusus 2027 (tag 2115, tiap 09:00 s.d. 1 Des; hari ini 19027 "Istithaah Kesehatan Haji 2027 Diperketat") membahas: cek status, prioritas lansia, lunas tunda/penawaran tanpa antre, checklist dokumen, istithaah, tujuh tahapan, tiga kelompok pengisi kuota, cadangan, beda reguler-khusus, mitos, rukun haji, kalender pelunasan khusus — JANGAN dobel.
- Hindari topik draft lama yang ditahan (Pohuwato biometrik, PLHUT Manggarai, Dairi majelis taklim, visitasi Bogor, 311 calon PHD Jateng, KSrelief Flores, KBIHU Jabar, STAIN Majene) dan berita serangan/militer/politik.
- NAMA TRAVEL LAIN DILARANG disebut sama sekali (termasuk nama bank/travel di slug link; lepas link bila slug memuat nama travel).
- Foto Elharamain sebagai ilustrasi (bukan dari kegiatan yang diberitakan) TANPA caption; "Foto ilustrasi: Dokumentasi Elharamain Wisata" DILARANG. Jangan pakai foto yang sudah dipakai 7 hari terakhir: cek paket di /home/khaeruddien/elharamain-news/ronde-a-11{17..23}, ronde-b-11{17..23}, haji-khusus-2027 (article.json field images/evidence); bila ragu bandingkan gambar post via `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?after=2026-11-17T00:00:00&per_page=100&_fields=id,title,jetpack_featured_media_url"`.
- Daftar rilis haji.go.id terbaru (pusat 50 + 10/provinsi): `ronde-a-1124/rilis.txt` (tanggal UTC | provinsi | judul | slug). Detail `https://<prov>.haji.go.id/api/news/<slug>` (pusat: `https://haji.go.id/api/news/<slug>`). referenceUrl provinsi sering kosong → link `https://<prov>.haji.go.id/berita/<slug>` (cek HTTP 200). Berita haji.go.id 48 jam terakhir didominasi haji reguler/daerah — JANGAN dipaksakan.
- HIMPUH: https://himpuh.or.id (artikel `https://himpuh.or.id/blog/detail/<id>/<slug>`, terbaca curl). Hanya tips/panduan & info regulasi; tanpa nama travel/anggota/kasus/promosi; tulis ulang total; cek tanggal berlaku, tulis "per <bulan tahun>". Sudah dipakai: umrah Rajab (19118), stroller Masjidil Haram, pelunasan haji khusus 16% (19070), miqat (19066), asuransi perjalanan (19122), umrah musim dingin busana (19176), Tasheel Card Nabawi (19234, blog 5294), memilih penerbangan umrah (19311), kuliner Haramain (19315), tidak tersesat di Masjidil Haram (19372), cek rincian biaya paket umrah (19425) — cek juga field sources paket ronde-a-1122/ronde-b-1122.
- Nusuk: www.nusuk.sa memblokir bot — jangan diakali. SPA: `https://portalapi.spa.gov.sa/api/v1/news?page=N&locale=en` (curl; teks + foto portalcdn).

## SLOT HARI INI (09:00 sudah diisi seri Edukasi 19027 → U&H#2 di 10:40). Tiap subagen hanya memakai sumber yang ditugaskan; tulis pilihan sumbermu ke `<SLOT>/PILIHAN.txt` SEDINI MUNGKIN dan cek PILIHAN.txt slot lain agar tidak dobel. Topik kemarin (23 Nov, 19367-19378 & 19420-19430) termasuk: pelimpahan porsi haji khusus wafat/sakit, Menag Muslimat NU sampah, iqamah saat tawaf, Sumur Raumah, PPPA pesantren ramah anak, tips tak tersesat Masjidil Haram HIMPUH, Raudhah 55.000/hari & Nusuk 60 juta, salat di hotel Makkah, JKN syarat umrah, produk kreatif ekosistem haji, kurma Saudi 2 juta ton AlUla, visa furoda lewat PIHK, beras basmati Bekasi, forum arsitektur Madinah, BI Rate & tabungan haji, rincian biaya paket umrah HIMPUH, doa musafir, Makkah Route umrah 2027, Masjid Penyengat, bisht — JANGAN diulang.
  0700 U&H (29) #1 dan 1300 U&H (29) #3 [S1]: 0700 = HAJI PLUS: rilis pusat 23 Nov "Kemenhaj Perbarui Daftar Jemaah Haji Khusus Berhak Lunas 1448 H/2027 M, PIHK Diminta Segera Sosialisasikan" (cek rilis.txt untuk slug pusat; versi sulsel = rilis sama, jangan dipakai lagi); pastikan beda dari 19070, 19025, 19306, 19420 dan seri Edukasi (sudut: pembaruan daftar & apa yang harus dilakukan jemaah). Foto: thumbnail haji.go.id bila non-sensitif. 1300 = berita UMROH terbaru 48-72 jam (regulasi/layanan Saudi atau Kemenhaj untuk jemaah umrah: visa, bandara, Haramain, pengawasan PPIU) dari sumber resmi/allowlist; kandidat: gorontalo 23 Nov "Kemenhaj Kab. Gorontalo Awasi Jemaah Umrah di Bandara" atau bengkulu 23 Nov PPIU Mukomuko serahkan dokumen izin (hanya bila isinya imbauan umrah bernilai umum, TANPA nama travel; beda dari 19152). BUKAN tips (milik S4), BUKAN Makkah Route (19428), BUKAN JKN (19376).
  0740 Berita (23) #1 dan 1020 Berita (23) #2 [S2]: 0740 = rilis BPKH terbaru yang belum ditulis (SUDAH: 19153, 19116, 18803, 18668, 19426 BI rate) — bpkh.go.id sering 403, pakai liputan allowlist; bila tak ada yang baru: berita Kemenag/zakat-wakaf/halal 48 jam yang bersinggungan dengan jemaah. 1020 = halal/ekonomi syariah/pesantren/Kemenag 48 jam, topik beda dari 0740 dan dari 19368, 19371, 19377, 19421.
  0820 Fiqih (26) dan 0940 Sejarah Islam (27) [S3]: evergreen, beda dari c[26]/c[27] 14 hari (19369 iqamah saat tawaf, 19231 ihram bersyarat, 19063 Hajar Aswad, 18912 makmum hotel, 19370 Sumur Raumah, 19232 As-Suqya, 19064 Shafa-Marwah, 18914 Hijir Ismail, dll.); Fiqih utamakan manasik umrah. Sejarah 250-450 kata; tempat bersejarah Makkah/Madinah/Thaif yang belum ditulis (cek judul & content.search).
  1040 U&H (29) #2 dan 1220 Tanya Jawab (30) [S4]: 1040 = TIPS HIMPUH/TIPS NUSUK bertopik UMROH praktis yang belum pernah ditulis (cek daftar "Sudah dipakai" di atas; cek tanggal berlaku). 1220 = satu pertanyaan jemaah UMROH/haji khusus, jawaban berbasis rujukan ulama/regulasi resmi (sumber jelas); beda dari c[30] 14 hari (19375 salat di hotel, 19237 tawaf wada, 19163, 19069, 18918, 18800, 18671); s.d. 700 kata.
  1340 Berita (23) #3 [S5]: berita perlindungan jemaah UMROH/imigrasi/layanan umrah/haji khusus 48-72 jam dari haji.go.id (pusat/provinsi; JANGAN rilis yang dipakai S1: Daftar Berhak Lunas Haji Khusus, Gorontalo bandara umrah, Mukomuko PPIU — cek ../1300/PILIHAN.txt) atau media allowlist (kompas/detik/antara/republika: umrah, PPIU, Saudi-Indonesia); BUKAN 19428, 19313, 19239, 19152. Bila tak ada: berita Kemenag/halal yang beda dari pilihan S2 (cek ../0740 & ../1020 PILIHAN.txt).
  1140 MEDIA ARAB (29/25) dan 1420 Dunia islam (25) [S6]: dua berita Saudi/dunia Muslim BERBEDA, 72 jam terakhir, relevan jemaah, beda dari c[25]/MEDIA ARAB 14 hari (19374 Raudhah 55.000, 19378 kurma AlUla, 19422 forum arsitektur Madinah, 19236, 19240, 19308, 19238, 19161, 19160, 19172, 19072, 19068, 19115). MEDIA ARAB pakai foto SPA (tools/spa_credit.py untuk kredit "Foto: SPA"). Cek juga kabar Nusuk BARU (setelah 23 Nov 04:00 WIB): catat di `/home/khaeruddien/elharamain-news/ronde-a-1124/nusuk.txt` (ada/kosong + sumber); slot Nusuk 08:00 & 13:20 diisi hanya bila ada bahan baru (beritahu induk).
  1100 Kegiatan (24) [S7]: lihat bagian Kegiatan di bawah.

## Lingkungan
- Python gambar: `python3` sistem (Pillow tersedia; /tmp/v tidak ada, jangan buat venv). ffmpeg di ~/.local/bin/ffmpeg.
- Kerja di folder `/home/khaeruddien/elharamain-news/ronde-a-1124/<SLOT>/` (SLOT mis. `0700`). Unduhan mentah di `raw/`.
- Cek tag: `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/tags?search=<kata>&_fields=id,name"` — pakai HANYA ID tag yang sudah ada (total 3-5 tag termasuk 34 "elharamain wisata").
- Link internal: `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?search=<kata>&_fields=id,link,title"`; pakai URL `link` asli.
- WebSearch/WebFetch boleh (domain allowlist di prompt). Jangan mengakali 403/406.
- Ilustrasi AI (hanya bila aturan mengharuskan, mis. berita negatif): kamu TIDAK membuatnya. Tulis prompt Inggris lengkap (gaya foto dokumenter sesuai aturan, wajah Indonesia/Arab, tanpa teks/logo/masjid) di `images.N.ai_prompt`, biarkan `file` kosong; induk yang membuat.

## Keluaran per artikel: `<SLOT>/article.json`
```json
{
 "slot": "2026-11-24T07:00:00",
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
 "notes": "catatan untuk redaktur, calon topik yang digugurkan + alasan"
}
```
`content.html` = blok Gutenberg (`<!-- wp:paragraph --><p>...</p><!-- /wp:paragraph -->`), pembuka `<strong>ELHARAMAIN NEWS</strong> –`, penutup praktis, lalu paragraf CTA miring persis dari prompt. Gambar 1 = foto utama (TIDAK ditaruh di content). Gambar sisipan N≥2: baris placeholder `%%IMG2%%` (sendirian di barisnya) di antara blok paragraf; induk menggantinya dengan blok wp:image.
Gambar final: JPEG q82, foto utama 16:9 lebar 1600 (min 1200), sisipan 4:5 atau 16:9. Read setiap gambar final (gerbang gambar 6 langkah) sebelum dimasukkan.
Cek akhir: `python3 /home/khaeruddien/elharamain-news/ronde-a-1124/fin.py <SLOT_DIR>` (hitung kata, frasa terlarang, CTA, pembuka). 450-600 kata (Kegiatan 450-650, Sejarah 250-450, TJ s.d. 700). Tanpa tanda pisah panjang (—), tanpa subjudul/bullet. Link keluar MAKSIMAL 1 (sumber utama); link internal, CTA WA, elharamainwisata.com tidak dihitung.

Laporan akhirmu ke induk: ringkas (slot, judul, path article.json, gambar + apa yang terlihat, sumber, calon digugurkan). Jangan tempel naskah lengkap.

## Kegiatan [S7]
Baca `/home/khaeruddien/elharamain-news/kegiatan-1123/klaim.txt` (kemarin: 3 JULI 2026 PLAT 1 dan 6 JULI 2026 BRONZE sudah ditulis; sebelumnya 25 JUNI BRONZE, 3 JULI SILVER 1) dan `/home/khaeruddien/elharamain-news/kegiatan-1124/klaim.txt` (hari ini). Pilih SATU grup 1448 H yang BELUM pernah diberitakan (cek semua judul c[24]: `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?categories=24&per_page=100&_fields=id,title,date"` juga page=2; cocokkan bulan+paket), utamakan folder 1448 H/2.JULI 2026 yang masih bebas (3 JULI BRONZE 1/2, PLAT 2, SILVER 2, 5 JULI 12 HARI) lalu bulan lain yang belum habis. Tulis klaim SEGERA ke kegiatan-1124/klaim.txt (format seperti kemarin) sebelum melihat foto. Album didominasi keberangkatan/nama kota/maskapai → pilih lain. Tanpa tanggal keberangkatan di teks mana pun (cukup "Group Juli 2026 <Paket>"); tanpa maskapai/kota asal/bandara/nama hotel; jangan pakai jam dari nama berkas WhatsApp; jangan kalimat meta ("foto bertanggal ... memperlihatkan") → narasi biasa. Semua gambar hanya dari album Drive itu, caption "Foto: Dokumentasi Elharamain Wisata"; 2-3 sisipan; hindari kursi roda/close-up wajah anak. Bandingkan dengan artikel grup Juni/Juli lain (19424, 19373, 19310, 19235, 19154, 19117, 19067, 18966, 18916) agar foto/tema tidak kembar. Skrip lembar kontak: ronde-a-1124/sheet.py. Setelah selesai tambahkan baris "-> SELESAI <jam> (Ronde A 11:00): paket ... foto ..." ke klaim.txt.

## Catatan Pemred kemarin (hindari)
Kutip lurus "..." → pakai kutip lengkung “...”; jangan kalimat meta foto ("Foto ... di Wikimedia Commons memperlihatkan"); jangan "kutipan" yang sebenarnya narasi penulis media (pakai kalimat tak langsung); excerpt SATU kalimat; jangan "tidak hanya ... tetapi juga"; maksimal 5 tag.
