# Brief subagen Ronde A, Minggu 22 Nov 2026 (dibuat agen News ±05:15 WIB)

Kamu menyiapkan PAKET ARTIKEL (naskah + gambar final di disk). Kamu TIDAK membuat post WordPress dan TIDAK mengunggah ke WordPress — agen induk yang mengunggah & menjadwalkan. TARGET: paket siap ≤ 06:20 WIB (cek `TZ=Asia/Jakarta date`); slot pertama terbit 07:00. Kerja cepat tapi aturan tetap utuh.

## Aturan wajib (baca dulu, utuh)
- `/home/khaeruddien/elharamain-news/routine/prompt_ronde_a.md` (aturan lengkap: gaya rumah, frasa AI terlarang, sortir, KEBIJAKAN TOPIK HAJI PLUS & UMROH, TIPS NUSUK & HIMPUH, GAMBAR & GERBANG GAMBAR, aturan haji.go.id/BPKH/MEDIA ARAB/Kegiatan). Jalankan persis untuk artikelmu, kecuali bagian membuat post/unggah (dikerjakan induk).
- `/home/khaeruddien/elharamain-news/ATURAN_REDAKSI.md`.
- KEBIJAKAN: utamakan HAJI PLUS/HAJI KHUSUS dan UMROH. Ronde A hari ini TIDAK mengambil haji reguler. Berita haji reguler tingkat daerah (Kanwil/kab/kota: pelunasan reguler, paspor, manasik reguler, porsi wafat, PLHUT, UMKM, seremoni, senam/jalan sehat pegawai, pembinaan pegawai, evaluasi anggaran) TIDAK diambil. Ragu reguler/daerah → ganti topik Haji Plus/Umroh.
- Judul situs 7-21 Nov: `/home/khaeruddien/elharamain-news/ronde-a-1122/judul_14hari.txt` (urut terbaru: id tanggal c[kategori] judul). Topik WAJIB beda dari semua itu; cek juga isi badan post bila topik mirip (`curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts/<id>?_fields=content"`). Seri Edukasi Haji Khusus 2027 (tag 2115, tiap 09:00 s.d. 1 Des; hari ini 19025 "Waspada tawaran haji khusus tanpa antre / lunas tunda") membahas: cek status, prioritas lansia, lunas tunda/penawaran tanpa antre, checklist dokumen, istithaah, tujuh tahapan, tiga kelompok pengisi kuota, cadangan, beda reguler-khusus, mitos, rukun haji, kalender pelunasan khusus — JANGAN dobel.
- Hindari topik draft lama yang ditahan (Pohuwato biometrik, PLHUT Manggarai, Dairi majelis taklim, visitasi Bogor, 311 calon PHD Jateng, KSrelief Flores, KBIHU Jabar, STAIN Majene) dan berita serangan/militer/politik.
- NAMA TRAVEL LAIN DILARANG disebut sama sekali (termasuk nama bank/travel di slug link; lepas link bila slug memuat nama travel).
- Foto Elharamain sebagai ilustrasi (bukan dari kegiatan yang diberitakan) TANPA caption; "Foto ilustrasi: Dokumentasi Elharamain Wisata" DILARANG. Jangan pakai foto yang sudah dipakai 7 hari terakhir: cek paket di /home/khaeruddien/elharamain-news/ronde-a-11{15..21}, ronde-b-11{15..21}, haji-khusus-2027 (article.json field images/evidence); bila ragu bandingkan gambar post via `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?after=2026-11-15T00:00:00&per_page=100&_fields=id,title,jetpack_featured_media_url"`.
- Daftar rilis haji.go.id terbaru (pusat 50 + 10/provinsi): `ronde-a-1122/rilis.txt` (tanggal UTC | provinsi | judul | slug). Detail `https://<prov>.haji.go.id/api/news/<slug>` (pusat: `https://haji.go.id/api/news/<slug>`). referenceUrl provinsi sering kosong → link `https://<prov>.haji.go.id/berita/<slug>` (cek HTTP 200). Berita haji.go.id 48 jam terakhir didominasi haji reguler/daerah — JANGAN dipaksakan.
- HIMPUH: https://himpuh.or.id (artikel `https://himpuh.or.id/blog/detail/<id>/<slug>`, terbaca curl). Hanya tips/panduan & info regulasi; tanpa nama travel/anggota/kasus/promosi; tulis ulang total; cek tanggal berlaku, tulis "per <bulan tahun>". Sudah dipakai: umrah Rajab (19118), stroller Masjidil Haram, pelunasan haji khusus 16% (19070), miqat (19066), asuransi perjalanan (19122), umrah musim dingin busana (19176).
- Nusuk: www.nusuk.sa memblokir bot — jangan diakali. SPA: `https://portalapi.spa.gov.sa/api/v1/news?page=N&locale=en` (curl; teks + foto portalcdn).

## SLOT HARI INI (09:00 sudah diisi seri Edukasi 19025 → U&H#2 digeser ke 10:40). Tiap subagen hanya memakai sumber yang ditugaskan; tulis pilihan sumbermu ke `<SLOT>/PILIHAN.txt` SEDINI MUNGKIN dan cek PILIHAN.txt slot lain agar tidak dobel.
  0700 U&H (29) #1 dan 1300 U&H (29) #3 [S1]: 0700 = HAJI PLUS/HAJI KHUSUS: berita resmi terbaru (Kemenhaj pusat/HIMPUH/media allowlist 72 jam) tentang PIHK, kuota/BPIH/pelunasan khusus, regulasi haji khusus 1448 H; TIDAK dobel seri Edukasi & 19070/19116. 1300 = berita UMROH terbaru (regulasi/layanan Saudi atau Kemenhaj untuk jemaah umrah: visa, bandara, Haramain, PPIU) 48-72 jam dari sumber resmi/allowlist; BUKAN tips (tips milik S4), BUKAN bagasi Soetta (19159), BUKAN cuaca Makkah (19172).
  0740 Berita (23) #1 dan 1020 Berita (23) #2 [S2]: 0740 = rilis BPKH terbaru yang belum ditulis (SUDAH: 19153 guru ngaji Rumah Zakat, 19116, 18803, 18668) — bpkh.go.id sering 403, pakai liputan allowlist; bila tak ada yang baru: berita Kemenag/zakat-wakaf/halal 48 jam yang bersinggungan dengan jemaah (BUKAN 19174 Menag dana umat). 1020 = halal/ekonomi syariah/pesantren/Kemenag 48 jam, topik beda dari 0740.
  0820 Fiqih (26) dan 0940 Sejarah Islam (27) [S3]: evergreen, beda dari c[26]/c[27] 14 hari; Fiqih utamakan manasik umrah. Sejarah 250-450 kata; kandidat Pemakaman Baqi (foto mentah sudah ada di /home/khaeruddien/elharamain-news/ronde-a-1121/1220/raw + urls.txt, belum pernah terunggah — cek lisensi/identitas lagi) atau tempat lain.
  1040 U&H (29) #2 dan 1220 Tanya Jawab (30) [S4]: 1040 = TIPS HIMPUH/TIPS NUSUK bertopik UMROH praktis; kandidat: Tasheel Card Masjid Nabawi saat salat Jumat (HIMPUH blog 5294, belum pernah ditulis; cek tanggal berlaku). 1220 = satu pertanyaan jemaah UMROH/haji khusus, jawaban berbasis rujukan ulama/regulasi resmi (sumber jelas); beda dari c[30] 14 hari (19163 sakit saat umrah/dam, 19069 Jumat musafir, 18918, 18800, 18671); s.d. 700 kata.
  1340 Berita (23) #3 [S5]: berita perlindungan jemaah UMROH/pengawasan PPIU/imigrasi/layanan umrah 48-72 jam dari haji.go.id (pusat/provinsi, mis. rilis.txt) atau media allowlist, tanpa nama travel; BUKAN Mukomuko (19152), BUKAN 19120/19114/19113. Bila tak ada: berita Kemenag/halal yang beda dari pilihan S2 (cek ../0740/PILIHAN.txt & ../1020/PILIHAN.txt).
  1140 MEDIA ARAB (29/25) dan 1420 Dunia islam (25) [S6]: dua berita Saudi/dunia Muslim BERBEDA, 72 jam terakhir, relevan jemaah, beda dari c[25]/MEDIA ARAB 14 hari (19161 murajaah Nabawi, 19160 Dawariq, 19172 cuaca, 19072, 19068, 19115, 18964, 18917, 18921, 18857, 18806, 18799). MEDIA ARAB pakai foto SPA (tools/spa_credit.py untuk kredit "Foto: SPA"). Cek juga kabar Nusuk BARU (setelah 21 Nov 04:00 WIB): catat di `/home/khaeruddien/elharamain-news/ronde-a-1122/nusuk.txt` (ada/kosong + sumber); slot Nusuk 08:00 & 13:20 diisi hanya bila ada bahan baru (beritahu induk).
  1100 Kegiatan (24) [S7]: lihat bagian Kegiatan di bawah.

## Lingkungan
- Python gambar: `python3` sistem (Pillow tersedia; /tmp/v tidak ada, jangan buat venv). ffmpeg di ~/.local/bin/ffmpeg.
- Kerja di folder `/home/khaeruddien/elharamain-news/ronde-a-1122/<SLOT>/` (SLOT mis. `0700`). Unduhan mentah di `raw/`.
- Cek tag: `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/tags?search=<kata>&_fields=id,name"` — pakai HANYA ID tag yang sudah ada (total 3-5 tag termasuk 34 "elharamain wisata").
- Link internal: `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?search=<kata>&_fields=id,link,title"`; pakai URL `link` asli.
- WebSearch/WebFetch boleh (domain allowlist di prompt). Jangan mengakali 403/406.
- Ilustrasi AI (hanya bila aturan mengharuskan, mis. berita negatif): kamu TIDAK membuatnya. Tulis prompt Inggris lengkap (gaya foto dokumenter sesuai aturan, wajah Indonesia/Arab, tanpa teks/logo/masjid) di `images.N.ai_prompt`, biarkan `file` kosong; induk yang membuat.

## Keluaran per artikel: `<SLOT>/article.json`
```json
{
 "slot": "2026-11-22T07:00:00",
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
Cek akhir: `python3 /home/khaeruddien/elharamain-news/ronde-a-1122/fin.py <SLOT_DIR>` (hitung kata, frasa terlarang, CTA, pembuka). 450-600 kata (Kegiatan 450-650, Sejarah 250-450, TJ s.d. 700). Tanpa tanda pisah panjang (—), tanpa subjudul/bullet. Link keluar MAKSIMAL 1 (sumber utama); link internal, CTA WA, elharamainwisata.com tidak dihitung.

Laporan akhirmu ke induk: ringkas (slot, judul, path article.json, gambar + apa yang terlihat, sumber, calon digugurkan). Jangan tempel naskah lengkap.

## Kegiatan [S7]
Grup SUDAH diklaim di `/home/khaeruddien/elharamain-news/kegiatan-1122/klaim.txt` = 25 JUNI 2026 BRONZE (folder 108AsNLXnOe_PIwZ5fov4usV4outZvODg, 1448 H/1.JUNI 2026). Bila album didominasi foto keberangkatan atau sudah pernah ditulis (cek semua judul c[24] `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?categories=24&per_page=100&_fields=id,title,date"` juga page=2), ganti ke grup 3 JULI 2026 (Silver/Plat) dari folder 1448 H/2.JULI 2026 dan perbarui klaim.txt. Tanpa tanggal keberangkatan di teks mana pun (cukup "Group Juni 2026 Bronze"); tanpa maskapai/kota asal/bandara. Semua gambar hanya dari album Drive itu, caption "Foto: Dokumentasi Elharamain Wisata"; 2-3 sisipan. Bandingkan dengan artikel grup Juni lain (19154, 19117, 19067, 18966, 18916) agar foto/tema tidak kembar. Skrip lembar kontak: ronde-a-1122/sheet.py. Setelah selesai tambahkan baris "-> SELESAI <jam> (Ronde A 11:00): paket ... foto ..." ke klaim.txt.
