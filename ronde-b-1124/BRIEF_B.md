# Brief subagen Ronde B, Selasa 24 Nov 2026 (dibuat agen News ±11:10 WIB)

Kamu menyiapkan PAKET ARTIKEL (naskah + gambar final di disk). Kamu TIDAK membuat post WordPress dan TIDAK mengunggah — induk yang mengunggah & menjadwalkan. TARGET: paket siap ≤ 12:45 WIB (cek `TZ=Asia/Jakarta date`); slot pertama terbit 15:00. Kerja cepat tapi aturan tetap utuh.

## Aturan wajib (baca dulu, utuh)
- `/home/khaeruddien/elharamain-news/routine/prompt_ronde_b.md` (aturan lengkap: gaya rumah, frasa AI terlarang, sortir, KEBIJAKAN TOPIK HAJI PLUS & UMROH, TIPS NUSUK & HIMPUH, CADANGAN SLOT NUSUK, GAMBAR & GERBANG GAMBAR, haji.go.id/BPKH/MEDIA ARAB/Kegiatan). Jalankan persis untuk artikelmu, kecuali bagian membuat post/unggah.
- `/home/khaeruddien/elharamain-news/ATURAN_REDAKSI.md`.
- KEBIJAKAN: utamakan HAJI PLUS/HAJI KHUSUS dan UMROH. Ronde A hari ini haji reguler = 0 (seri Edukasi 19027 istithaah = seri, bukan ronde). Ronde B sebaiknya 0 haji reguler (maks 1 hanya kebijakan nasional besar). Berita haji reguler daerah (Kanwil/kab/kota: pelunasan reguler daerah, bio visa, manasik reguler, mahram, PLHUT, seremoni ASN, DPRD kunjungan, PPL mahasiswa, anggaran) TIDAK diambil. Ragu → ganti topik Haji Plus/Umroh.
- Judul situs 9–24 Nov (termasuk 13 post hari ini & 10 post Ronde B kemarin): `/home/khaeruddien/elharamain-news/ronde-b-1124/judul_14hari.txt` (id tanggal c[kategori] judul). Topik WAJIB beda dari semua itu, terutama HARI INI: daftar berhak lunas haji khusus 1448 H diperbarui (19463), saldo nilai manfaat Rp3,4 juta & e-Wallet BPKH Apps (19464), ramal saat tawaf (19465), istithaah kesehatan 2027 (19027), Masjid Addas Thaif (19466), Rakornas Pesantren 25–26 Nov & Pesantren Award (19467), TIPS HIMPUH bugar di pesawat (19468), Group Juli 2026 Platinum (19469), durasi umrah 124 menit SPA (19470), umrah untuk orang tua wafat (19471), PPIU Mukomuko serahkan izin (19472), city terminal Makkah (19473), Distrik Budaya Jabal Tsur Discover Makkah (19474). Ronde B kemarin: visa furoda wajib PIHK (19420), ekspor beras basmati (19421), forum arsitektur Madinah (19422), Group Juli 2026 Bronze naik unta (19424), HIMPUH cek rincian biaya paket (19425), BI Rate & tabungan haji (19426), doa musafir (19427), Makkah Route umrah 2027 (19428), Masjid Penyengat (19429), bisht (19430). Paket Ronde A hari ini di `ronde-a-1124/<slot>/article.json`, Ronde B kemarin `ronde-b-1123/<slot>/article.json` (cek field sources agar tidak memakai sumber sama). Cek isi badan post bila topik mirip (`curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts/<id>?_fields=content"`; post future tidak terbaca publik → baca paket disk).
- Seri Edukasi Haji Khusus 2027 (tag 2115, 09:00 s.d. 1 Des): cek status, prioritas lansia, lunas tunda, checklist dokumen, istithaah, tujuh tahapan, tiga kelompok pengisi kuota, cadangan, beda reguler-khusus, mitos, rukun haji, kalender pelunasan — JANGAN dobel.
- Hindari draft lama yang ditahan & berita serangan/militer/politik.
- NAMA TRAVEL LAIN DILARANG disebut sama sekali (juga di slug link; lepas link bila slug memuat nama travel).
- Foto Elharamain sebagai ilustrasi TANPA caption; "Foto ilustrasi: Dokumentasi Elharamain Wisata" DILARANG. Berita negatif: tanpa foto Elharamain → ilustrasi AI (induk yang membuat; tulis ai_prompt). Jangan pakai foto yang sudah dipakai 7 hari terakhir: cek paket ronde-a-11{17..24}, ronde-b-11{17..23} (article.json images/evidence) dan `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?after=2026-11-17T00:00:00&per_page=100&_fields=id,title,jetpack_featured_media_url"`.
- Rilis haji.go.id terbaru (pusat 50 + 10/provinsi, diambil 11:05 WIB): `ronde-b-1124/rilis.txt` (tanggal UTC | prov | judul | slug). Sejak 23 Nov hampir semua haji reguler daerah/seremoni (TIDAK diambil). Daftar berhak lunas haji khusus (pusat & sulsel) dan PPIU Mukomuko SUDAH dipakai Ronde A. Kemungkinan tidak ada rilis yang layak → jangan memaksakan.
- HIMPUH: https://himpuh.or.id (artikel `https://himpuh.or.id/blog/detail/<id>/<slug>`, terbaca curl). Hanya tips/panduan & info regulasi; tanpa nama travel/anggota/kasus/promosi; tulis ulang total; cek tanggal berlaku, tulis "per <bulan tahun>". Blog yang SUDAH dipakai (paket 11–24 Nov): 3612, 5137, 5149, 5199, 5234, 5235, 5271, 5273, 5291, 5292, 5294, 5314, 5318, 5320, 5322, 5323, 5339, 5340 (+ cek sources 19425 & 19468). Topik HIMPUH yang sudah ada: umrah Rajab, stroller, pelunasan haji khusus 16%, miqat, asuransi, busana musim dingin, Tasheel Card, penerbangan umrah, anti nyasar Masjidil Haram, cek rincian biaya paket, bugar di pesawat.
- Nusuk: www.nusuk.sa memblokir bot — jangan diakali. SPA: `https://portalapi.spa.gov.sa/api/v1/news?page=N&locale=en` (curl; teks + foto portalcdn). Ronde A 05:09 mencatat: tidak ada kabar Nusuk baru (`ronde-a-1124/nusuk.txt`).

## SLOT RONDE B (tiap subagen hanya slotnya; tulis pilihan sumber ke `<SLOT>/PILIHAN.txt` SEDINI MUNGKIN dan cek PILIHAN.txt slot lain agar tidak dobel)
  1500 U&H (29) #1 dan 1940 U&H (29) #2 [S1]: 1500 = berita UMROH/HAJI KHUSUS terbaru (48–72 jam) dari sumber resmi/allowlist (Kemenhaj, Kemenag, Imigrasi, Antara/Republika/Kompas/Detik; Arab News/SPA milik S4). 1940 = berita/explainer UMROH atau HAJI KHUSUS lain dari sumber resmi (BUKAN tips HIMPUH — HIMPUH dipakai S7), topik beda dari 1500.
  1540 Berita (23) #1 dan 1740 Berita (23) #2 [S2]: 1540 = rilis BPKH terbaru yang belum ditulis (cek judul_14hari; 19464 saldo nilai manfaat/e-Wallet & 19426 BI Rate sudah) — bpkh.go.id sering 403, pakai liputan allowlist; bila tak ada: Kemenag/zakat-wakaf/halal/ekonomi syariah 48 jam yang bersinggungan dengan jemaah. 1740 = Kemenag/pesantren/halal/ekonomi syariah 48 jam, beda dari 1540 dan dari 19467 Rakornas Pesantren.
  2100 Berita (23) #3 dan 2220 Lifestyle Muslim (32) [S3]: 2100 = perlindungan jemaah UMROH/pengawasan PPIU/imigrasi/bandara/kesehatan jemaah umrah 72 jam (media allowlist/Kemenkes/Imigrasi), tanpa nama travel; BUKAN 19428/19472/19313/19306. Bila tak ada: berita Kemenag/halal beda dari S2 (koordinasi lewat ../1540/PILIHAN.txt & ../1740/PILIHAN.txt). 2220 = gaya hidup muslim/persiapan fisik/keuangan syariah/perlengkapan jemaah umrah, terverifikasi, beda dari c[32] 14 hari (19430 bisht, 19315 kuliner Haramain, 19176 busana musim dingin, 19122 asuransi, dll.) dan dari 19468 bugar di pesawat.
  1700 MEDIA ARAB (29/25) [S4]: berita Saudi 72 jam relevan jemaah (SPA portalapi/Arab News), beda dari MEDIA ARAB/c[25]/c[29] 14 hari (19470 durasi umrah, 19473 city terminal, 19474 Jabal Tsur, 19422 forum arsitektur, 19378 kurma, 19374 Raudhah, dll.). Foto SPA (tools/spa_credit.py untuk kredit "Foto: SPA"). Juga cek kabar Nusuk BARU (setelah 24 Nov 05:00 WIB) di SPA/Arab News; catat di `ronde-b-1124/nusuk.txt` (ada/kosong + sumber). Bila ada bahan Nusuk baru yang kuat, tulis 1 paket tambahan di `ronde-b-1124/1600/` (kategori 29, slot 16:00) — bila tidak, cukup catat kosong.
  2020 Hikmah (28) dan 2140 Wisata Halal (31) [S5]: Hikmah = renungan akhlak/ibadah dari kitab/ulama dengan sumber jelas (beda dari c[28] 14 hari: 19427 doa musafir, 19312 Arbain, 19173, 19119 sabar, 18968 syukur, dll.). Wisata Halal = destinasi religi/halal (Indonesia, Turki, Mesir, Saudi, Yordania, Uzbekistan, Maroko...), beda dari c[31] 14 hari (19429 Penyengat, 19314 Sunan Ampel, 19175 Masjid Biru, 19121, 18970) dan dari 19466 Addas/19474 Jabal Tsur. Masjid/landmark WAJIB foto asli (aturan masjid + kredit pendek bila CC BY).
  1820 Kegiatan (24) [S6]: lihat bagian Kegiatan di bawah.
  1620 dan 1900 SLOT GRID NUSUK — CADANGAN (Juragan 24 Nov: total harian jangan turun) [S7]: karena tidak ada kabar Nusuk baru, isi berurutan: (1) TIPS NUSUK/HIMPUH kategori 29 (blog HIMPUH yang belum dipakai, topik umroh/haji plus praktis yang tidak dobel 14 hari & seri 2115; tips Nusuk hanya dari halaman Nusuk/liputan resmi yang terbaca & bertanggal); 1620 dan 1900 harus beda topik satu sama lain. (2) Bila tidak ada bahan tips yang lolos, 1620 → Sejarah Islam (27, 250–450 kata, beda dari c[27] 14 hari termasuk 19466 Addas, 19370 Sumur Raumah) dan 1900 → Dunia islam (25, berita dunia Islam terbaru, beda dari c[25] 14 hari dan dari slot S4 — cek ../1700/PILIHAN.txt). Tulis pilihan cadangan & alasannya di article.json notes.

## Lingkungan
- Python gambar: `python3` sistem (Pillow tersedia; /tmp/v tidak ada, jangan buat venv). ffmpeg di ~/.local/bin/ffmpeg.
- Kerja di folder `/home/khaeruddien/elharamain-news/ronde-b-1124/<SLOT>/` (SLOT mis. `1500`). Unduhan mentah di `raw/` (JANGAN simpan HTML pihak ketiga di luar raw/).
- Cek tag: `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/tags?search=<kata>&_fields=id,name"` — pakai HANYA ID tag yang sudah ada (total 3-5 tag termasuk 34 "elharamain wisata").
- Link internal: `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?search=<kata>&_fields=id,link,title"`; pakai URL `link` asli.
- WebSearch/WebFetch boleh (domain allowlist di prompt). Jangan mengakali 403/406.
- Ilustrasi AI (hanya bila aturan mengharuskan, mis. berita negatif): kamu TIDAK membuatnya. Tulis prompt Inggris lengkap (gaya foto dokumenter sesuai aturan, wajah Indonesia/Arab, tanpa teks/logo/masjid) di `images.N.ai_prompt`, biarkan `file` kosong; induk yang membuat.

## Keluaran per artikel: `<SLOT>/article.json`
```json
{
 "slot": "2026-11-24T15:00:00",
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
Cek akhir: `python3 /home/khaeruddien/elharamain-news/ronde-b-1124/fin.py <SLOT_DIR>` (hitung kata, frasa terlarang, CTA, pembuka). 450-600 kata (Kegiatan 450-650). Tanpa tanda pisah panjang (—), tanpa subjudul/bullet. Link keluar MAKSIMAL 1 (sumber utama); link internal, CTA WA, elharamainwisata.com tidak dihitung.

Laporan akhirmu ke induk: ringkas (slot, judul, path article.json, gambar + apa yang terlihat, sumber, calon digugurkan). Jangan tempel naskah lengkap.

## Kegiatan [S6]
Klaim grup di `/home/khaeruddien/elharamain-news/kegiatan-1124/klaim.txt` (BACA dulu). Sudah dipakai: 3 JULI 2026 PLAT 2 (Ronde A hari ini, 19469), 3 JULI BRONZE ? (19424 kemarin — cek klaim kegiatan-1123/klaim.txt untuk grup persisnya), PLAT 1 (19373), SILVER 1 (19310), 25 JUNI BRONZE (19235), grup Juni lain. Pilih SATU yang masih bebas dari 1448 H/2.JULI 2026 (album 1cmzsm7NsKxb9LB_DqHzEuigNgm4frkNv): kandidat 3 JULI BRONZE 1/2 (yang belum), 3 JULI SILVER 2, 5 JULI 12 HARI, 6 JULI BRONZE. SEGERA tambahkan baris klaim "RONDE B 24 Nov S6 (<jam>): dipilih <grup> | folder <id> | slot 2026-11-24T18:20 | tema ..." ke klaim.txt. Cek semua judul c[24] (`curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?categories=24&per_page=100&_fields=id,title,date"` juga page=2) agar grup belum pernah ditulis. Bila album didominasi foto keberangkatan, pilih grup lain dan perbarui klaim. Tanpa tanggal keberangkatan di teks mana pun (cukup "Group Juli 2026 Silver"); tanpa maskapai/kota asal/bandara. Semua gambar hanya dari album Drive itu, caption "Foto: Dokumentasi Elharamain Wisata"; 2–3 sisipan. Bandingkan dengan artikel grup Juni/Juli lain (19469, 19424, 19373, 19310, 19235, 19154, 19117) agar foto/tema/judul tidak kembar; cari kegiatan khas album. Skrip lembar kontak: ronde-b-1124/sheet.py. Setelah selesai tambahkan "-> SELESAI <jam> (Ronde B 18:20): paket ... foto ..." ke klaim.txt.
