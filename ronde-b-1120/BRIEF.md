# Brief subagen Ronde B, Jumat 20 Nov 2026 (dibuat agen News 11:20 WIB)

Kamu menyiapkan PAKET ARTIKEL (naskah + gambar final di disk). Kamu TIDAK membuat post WordPress dan TIDAK mengunggah ke WordPress — agen induk yang mengunggah & menjadwalkan.

## Aturan wajib (baca dulu, utuh)
- `/home/khaeruddien/elharamain-news/routine/prompt_ronde_b.md` (aturan lengkap: gaya rumah, frasa AI terlarang, sortir, KEBIJAKAN TOPIK HAJI PLUS & UMROH (berlaku mulai 20 Nov), TIPS NUSUK & HIMPUH, GAMBAR & GERBANG GAMBAR, haji.go.id/BPKH/MEDIA ARAB/Kegiatan/Nusuk). Jalankan persis untuk artikelmu, kecuali bagian membuat post/unggah (dikerjakan induk).
- `/home/khaeruddien/elharamain-news/ATURAN_REDAKSI.md`.
- KEBIJAKAN: utamakan HAJI PLUS/HAJI KHUSUS dan UMROH. Haji reguler maks 1/hari; Ronde B TIDAK mengambil haji reguler. Berita haji reguler tingkat daerah (Kanwil/kab/kota: pelunasan reguler, paspor, manasik reguler, istithaah daerah, UMKM haji daerah, seremoni/olahraga pegawai, sosialisasi/bimtek) TIDAK diambil — saring saat memilih topik (teguran Bos: Ronde A tadi pagi 2 artikel Kanwil daerah ditahan Pemred). Ragu → ganti topik Haji Plus/Umroh/tips Nusuk-HIMPUH.
- Judul situs 6-20 Nov (termasuk Ronde A hari ini & draft ditahan): `/home/khaeruddien/elharamain-news/ronde-b-1120/judul_14hari.txt` (urut terbaru, format: id tanggal c[kategori] judul). Topik WAJIB beda dari semua itu, terutama hari ini: 19061 izin PPIU biro wisata, 19063 Hajar Aswad isyarat, 19064 Shafa-Marwah, 19066 empat miqat (HIMPUH), 19067 Kegiatan Juni Silver, 19068 jalur pejalan kaki Nabawi (SPA), 19069 Jumat musafir, 19070 pelunasan haji khusus 16% (HIMPUH), 19071 pameran haji Jeddah, 19072 terjemahan khutbah 11 bahasa. Seri Edukasi Haji Khusus 2027 (tag 2115, 19023-19034: cek status, prioritas lansia, lunas tunda/penawaran tanpa antre, checklist dokumen, istithaah, tujuh tahapan, tiga kelompok kuota, cadangan, beda reguler-khusus, mitos, rukun haji, kalender pelunasan khusus) — JANGAN dobel.
- Foto Elharamain sebagai ilustrasi (bukan dari kegiatan yang diberitakan) TANPA caption; "Foto ilustrasi: Dokumentasi Elharamain Wisata" DILARANG. Jangan pakai foto yang sudah dipakai 7 hari terakhir: cek paket di /home/khaeruddien/elharamain-news/ronde-a-1120, ronde-a-1119, ronde-b-1119, ronde-a-1118, ronde-b-1118, ronde-a-1117, ronde-b-1117, haji-khusus-2027 (article.json field images/evidence); bila ragu bandingkan gambar post via `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?after=2026-11-13T00:00:00&per_page=100&_fields=id,title,jetpack_featured_media_url"`.
- Daftar rilis haji.go.id 6-20 Nov: `rilis.txt` (tanggal UTC | provinsi | judul | slug). Mentah: pusat.json & prov_*.json; detail via `https://<prov>.haji.go.id/api/news/<slug>` (pusat: `https://haji.go.id/api/news/<slug>`). referenceUrl provinsi sering kosong → link `https://<prov>.haji.go.id/berita/<slug>` (cek HTTP 200). Lepas link bila slug memuat nama travel.
- HIMPUH: https://himpuh.or.id (artikel `https://himpuh.or.id/blog/detail/<id>/<slug>`, terbaca curl). Hanya tips/panduan & info regulasi; tanpa nama travel/anggota/kasus/promosi; tulis ulang total; cek tanggal berlaku, tulis "per <bulan tahun>". Ronde A sudah memakai HIMPUH 5314 (miqat), 5320 & 5323 (pelunasan haji khusus) — JANGAN pakai lagi.
- Tiap subagen hanya memakai sumber yang ditugaskan; cadangan unik per slot. Penugasan seluruh ronde (JANGAN ambil rilis milik slot lain):
  15:00 U&H (29) [S1]: kalsel "Perkuat Perlindungan Jemaah Umrah, Kemenhaj HSS Pantau Perizinan PPIU hingga Kesiapan Tiket dan Akomodasi" (16 Nov) → sudut perlindungan jemaah UMRAH (cek tiket/akomodasi sebelum bayar); beda dari 19061/18919. Nama travel DILARANG disebut. Cadangan S1-a: pusat "Kementerian Haji dan Umrah Perketat Pengawasan: Targetkan Minimal Satu PPNS di Setiap Provinsi" (10 Nov).
  15:40 Berita (23) [S1]: kaltim "Kemenhaj Kaltim Dalami Aplikasi SIGAP, Pengaduan Haji dan Umrah Disiapkan Lebih Cepat & Transparan" (17 Nov) → sudut kanal pengaduan jemaah umrah/haji. Cadangan S1-b: pusat "Kemenhaj Benahi Komunikasi Publik, Jemaah Harus Mudah Dapat Kepastian Layanan" (13 Nov).
  17:40 Berita (23) dan 21:00 Berita (23) [S2]: (a) rilis BPKH terbaru yang belum ditulis (SUDAH: 18803 mobil dakwah Lazismu, 18668 target dana kelolaan 2027, 18630 kanal informasi, 17306 kemaslahatan) — bpkh.go.id sering 403, pakai liputan media allowlist; (b) berita Kemenag/halal/ekonomi syariah/umrah 48 jam terakhir dari media allowlist (antaranews, republika, kompas, detik, infopublik, cnnindonesia) yang bersinggungan dengan jemaah umrah/haji khusus; (c) cadangan S2: pusat "Kemenhaj Perketat Pengawasan Haji dan Umrah: Langkah Strategis Berantas Penipuan dan 'Bandit Agama'" (11 Nov; cek beda dari 17662/18794). JANGAN haji reguler daerah. Dua artikel WAJIB topik berbeda.
  19:40 U&H (29) dan 22:20 Lifestyle Muslim (32) [S3]: 19:40 = TIPS HIMPUH atau TIPS NUSUK bertopik UMROH/HAJI KHUSUS praktis (mis. aturan & dokumen umrah terbaru, adab di Haram, umrah musim dingin, umrah lansia), atau berita resmi terbaru haji khusus/PIHK — beda dari miqat & pelunasan khusus (hari ini) dan layanan Nusuk yang sudah ditulis. 22:20 Lifestyle = kesehatan/persiapan fisik/perlengkapan/keuangan syariah jemaah umrah (boleh tips HIMPUH lain yang belum dipakai, sumber jelas). Dua topik WAJIB beda.
  20:20 Hikmah (28) dan 21:40 Wisata Halal (31) [S4]: evergreen bersumber jelas, beda dari c[28]/c[31] 14 hari (Al-Ghazali syukur & ghibah, Topkapi, Masjid Gedhe Kauman, dll.). Wisata Halal yang dekat paket Elharamain (Turki/Mesir/Saudi) diutamakan; masjid/landmark WAJIB foto asli tempat itu.
  16:20 NUSUK (29), 19:00 NUSUK (29) dan 17:00 MEDIA ARAB (29/25) [S5]: cari kabar Nusuk BARU (setelah 20 Nov 04:30 WIB; Ronde A tak menemukan, lihat ../ronde-a-1120/nusuk_kosong.txt) di SPA portalapi `https://portalapi.spa.gov.sa/api/v1/news?page=N&locale=en`, Arab News, haj.gov.sa. nusuk.sa memblokir bot: jangan diakali. Bila tidak ada, JANGAN mengarang; tulis alasan di `ronde-b-1120/nusuk_kosong.txt` (0 wajar). MEDIA ARAB: berita Saudi 72 jam terakhir relevan jemaah, BEDA dari 19068 (jalur pejalan kaki Nabawi), 19072 (terjemahan khutbah), 18964, 18917, 18921, 18857 dan c[25]/MEDIA ARAB 14 hari; foto SPA (tools/spa_credit.py untuk kredit "Foto: SPA").
  18:20 Kegiatan (24) [S6]: lihat bagian Kegiatan di bawah.
- Slot tengah Nusuk 16:00/18:40/21:20 opsional hanya bila bahan Nusuk benar-benar ada (S5 tentukan; tulis di laporan).

## Lingkungan
- Python gambar: `python3` sistem (Pillow 10.2 tersedia; /tmp/v TIDAK ada, jangan buat venv). ffmpeg di ~/.local/bin/ffmpeg.
- Kerja di folder `/home/khaeruddien/elharamain-news/ronde-b-1120/<SLOT>/` (SLOT mis. `1540`). Unduhan mentah di subfolder `raw/`.
- Cek tag: `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/tags?search=<kata>&_fields=id,name"` — pakai HANYA ID tag yang sudah ada (3-5 tag) + 34 (elharamain wisata).
- Link internal: cari via `curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?search=<kata>&_fields=id,link,title"`; pakai URL `link` asli.
- WebSearch/WebFetch boleh (domain allowlist di prompt). Jangan mengakali 403/406.
- Ilustrasi AI (hanya bila aturan mengharuskan, mis. berita negatif): kamu TIDAK bisa membuatnya. Tulis prompt Inggris lengkap (sesuai aturan gaya foto dokumenter, wajah Indonesia/Arab, tanpa teks/logo/masjid) di article.json `images.N.ai_prompt` dan biarkan `file` kosong; induk yang membuat.

## Keluaran per artikel: `<SLOT>/article.json`
```json
{
 "slot": "2026-11-20T15:00:00",
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
- Kegiatan [S6]: baca/isi `/home/khaeruddien/elharamain-news/kegiatan-1120/klaim.txt` (sudah ada klaim 21 JUNI 2026 SILVER Ronde A; tambahkan satu baris klaimmu: grup | folder | slot 2026-11-20T18:20 Ronde B | tema | jam klaim). Pilih grup BERBEDA, utamakan paket selain Silver (Silver sudah tadi pagi): 14 JUNI 2026 BRONZE (folder 1r1AuGbnsrWYNu2RSPLmeHCWXD7SLJkYc) atau 25 JUNI 2026 BRONZE (108AsNLXnOe_PIwZ5fov4usV4outZvODg) — keduanya bebas (lihat ../kegiatan-1119/klaim.txt). Cek juga semua judul c[24] (`curl -s "https://public-api.wordpress.com/wp/v2/sites/257737206/posts?categories=24&per_page=100&_fields=id,title,date"`, juga page=2). Tanpa tanggal keberangkatan di teks mana pun (cukup "Group Juni 2026 Bronze"). Tema/foto beda dari 19067 (mukena Nabawi, payung Madinah, depan Ka'bah) bila album memungkinkan.
