# Aturan Redaksi Elharamain News

Ringkasan aturan dari pemilik untuk artikel news.elharamainwisata.com. Aturan lengkap yang dijalankan routine ada di `routine/prompt_ronde_a.md` dan `routine/prompt_ronde_b.md`.

## Jadwal & routine

| Routine | Jadwal (WIB) | Isi |
|---|---|---|
| Ronde A | 05:00, terbit 07:00–14:20 (jeda 40 menit) | 12 artikel: Umroh & Haji 3, Berita 3, Fiqih, Sejarah Islam, Tanya Jawab, Kegiatan, Dunia Islam, Media Arab |
| Ronde B | 11:00, terbit 15:00–22:20 (jeda 40 menit) | 12 artikel: Umroh & Haji 2, Berita 3, **Nusuk 2 (16:20 dan 19:00, menggantikan Sejarah Islam dan Dunia Islam kedua)**, Kegiatan, Media Arab, Hikmah, Wisata Halal, Lifestyle Muslim; topik berbeda dari Ronde A |
| Nusuk (tambahan, perintah pemilik 2026-11-11) | ikut Ronde A (3) dan Ronde B (3) | **8 artikel/hari bersumber Nusuk (6 di slot tengah + 2 di slot grid Ronde B)** (kategori Umroh & Haji 29), terjadwal di antara slot grid: Ronde A 08:00, 10:40, 13:20; Ronde B 16:00, 18:40, 21:20. **Total harian tetap 30 artikel** (22 ronde + 8 Nusuk; Sejarah Islam dan Dunia Islam masing-masing 1 per hari, perintah pemilik 2026-11-11). Sumber: situs resmi nusuk.sa (Panduan Layanan `https://www.nusuk.sa/all-services` dan halaman `service-details/<id>`), akun resmi Instagram @mynusuk dan X Nusuk. nusuk.sa menolak curl/WebFetch; dibaca lewat Chrome desktop (halaman dirender di sisi server, bisa diambil dengan fetch dari dalam tab). Bila Chrome tidak tersedia: ambil dari liputan Arab News/SPA/Saudi Gazette/media Indonesia tentang Nusuk; bila tetap kurang, buat lebih sedikit dan laporkan, jangan mengarang. |
| Cadangan Ronde B | 14:00 | Cek slot sore; bila Ronde B gagal, isi slot yang kosong. Bila lengkap, langsung berhenti |
| Laporan WA | 07:00 | Judul + link artikel kemarin ke grup WA redaksi (OneSender) |
| Pemimpin Redaksi (QC) | 06:30 & 12:30 | Kroscek semua artikel terjadwal hasil Ronde A/B sebelum terbit: sortir, nama travel lain, fakta vs sumber, kalimat salinan, gaya AI, gambar. Memperbaiki yang salah, menahan (draft) yang tidak layak, lalu melapor. Prompt: `routine/prompt_pemred.md` |

- Artikel dijadwalkan (status *future*), tidak pernah langsung *publish*.
- Tidak ada lagi caption media sosial.

## Sumber berita

1. **haji.go.id** (Kementerian Haji dan Umrah RI) – sumber resmi utama. ~~Minimal 5 dari 10 artikel kategori per ronde; usahakan 1–2 artikel per ronde dari situs provinsi.~~ **Mulai 20 Nov 2026:** hanya berita umrah, haji khusus/PIHK/PPIU, klarifikasi hoaks, atau kebijakan nasional besar; usahakan 3–5 dari 10 artikel kategori per ronde bila beritanya sesuai, tanpa memaksakan haji reguler. Termasuk ppid.haji.go.id dan **subdomain provinsi** (`dki.haji.go.id`, `jabar.haji.go.id`, `banten.haji.go.id`, dst.; prioritas DKI, Jabar, Banten) – situs provinsi hanya untuk berita umrah/haji khusus.
2. **BPKH** (bpkh.go.id) – dana haji, nilai manfaat, BPIH.
3. **Media Arab** (Arab News, SPA, haj.gov.sa, Nusuk, Saudi Gazette) – 2 artikel per hari (pagi 1, sore 1), kategori Umroh & Haji atau Dunia Islam sesuai isi.
4. **Instagram resmi**: @mediacenterhaji.ri (Media Center Haji) dan @gus.irfanyusuf (Menteri Haji dan Umrah).
5. Situs resmi lain: haj.gov.sa, spa.gov.sa, nusuk.sa, kemlu.go.id, moi.gov.sa, moh.gov.sa, kemkes.go.id.
   - **Nusuk (perintah pemilik 2026-11-11: banyak update terbaru, boleh jadi bahan berita):** fitur aplikasi, izin, Raudhah, layanan baru. Akses (dicek 11 Nov): nusuk.sa menolak WebFetch/curl (HTTP 406 "bot"); umrah.nusuk.sa terbaca tetapi hanya katalog paket. Ambil dari liputan Arab News, SPA, Saudi Gazette, haj.gov.sa, atau Chrome desktop bila tersedia. Tidak memecahkan captcha; fakta hanya dari yang terbaca. Tetap lolos sortir berita dan perhatikan: hajj.nusuk.sa tidak otomatis berlaku untuk jemaah Indonesia.
6. Media: Antara, Republika, Kompas, Detik, NU Online, MUI, Muhammadiyah, dll.

Semua fakta, angka, dan kutipan harus dari sumber yang benar-benar dibaca. Tidak boleh mengarang.

### Kebijakan topik: Haji Plus & Umroh diutamakan (perintah Juragan 19 Nov 2026, berlaku mulai 20 Nov 2026)
> "Kurangi artikel haji reguler karena kita haji plus, dan banyakin berita haji plus dan umroh."

1. **Prioritas topik**: (1) Haji Plus/Haji Khusus – PIHK, kuota khusus, pelunasan/BPIH khusus, regulasi Kemenhaj yang menyangkut haji khusus; (2) Umroh – regulasi Saudi/Kemenhaj, visa, Nusuk, Masjidil Haram/Nabawi, tips, kegiatan jemaah Elharamain.
2. **Haji reguler maksimal 1 artikel per hari** (Ronde A + B + Cadangan), hanya kebijakan nasional besar yang juga berdampak ke calon jemaah haji plus/umroh.
3. **Berita haji reguler tingkat daerah tidak diambil lagi** (Kemenhaj kabupaten/kota/Kanwil: manasik reguler, paspor/biometrik daerah, pelunasan reguler daerah, majelis taklim daerah, PLHUT daerah, sosialisasi/UMKM haji daerah, seremoni).
4. Sisa slot diisi berita Haji Plus dan Umroh; bila sumber sepi, boleh artikel edukasi/explainer haji plus & umroh yang faktanya terverifikasi (topik berbeda dari seri "Edukasi Haji Khusus 2027", tag 2115).
5. **Pemred** menahan (draft) artikel haji reguler daerah dan kelebihan artikel haji reguler di atas 1/hari. Seri "Edukasi Haji Khusus 2027" tetap berjalan sesuai jadwal.
6. **Tips Nusuk & HIMPUH** (perintah Juragan 19 Nov 2026 15:50: "isi saja tips-tips dari Nusuk dan HIMPUH") – sumber konten tips/panduan umroh & haji plus untuk mengisi slot Haji Plus & Umroh, terutama saat berita sepi.
   - **Nusuk** (platform resmi Kementerian Haji dan Umrah Arab Saudi): https://www.nusuk.sa (panduan layanan `/all-services`, `/service-details/<id>`), https://umrah.nusuk.sa, https://hajj.nusuk.sa, aplikasi Nusuk, Instagram @mynusuk, X Nusuk. www.nusuk.sa menolak bot (HTTP 406) – jangan diakali; pakai halaman yang terbaca atau liputan resmi (SPA, haj.gov.sa, Arab News).
   - **HIMPUH** (Himpunan Penyelenggara Umrah dan Haji Khusus): https://himpuh.or.id (artikel `https://himpuh.or.id/blog/detail/<id>/<slug>`). Ambil hanya tips/panduan & info regulasi; tanpa nama travel/anggota, kasus hukum, polemik, promosi.
   - Bentuk: artikel tips praktis (izin Raudhah via Nusuk, visa & aturan umrah terbaru, miqat, tawaf, kesehatan, perlengkapan, adab) **ditulis ulang dengan bahasa sendiri**, sebut sumber + **1 link keluar** ke halaman resmi. Fakta/aturan **wajib dicek tanggal berlakunya** (aturan Saudi sering berubah), tulis "per <bulan tahun>"; bila tanggal tidak jelas/bertentangan, gugurkan.
   - Topik tidak boleh dobel dengan artikel 14 hari terakhir, seri "Edukasi Haji Khusus 2027" (tag 2115), dan layanan Nusuk yang sudah ditulis.

### Sortir berita (perintah pemilik 2026-11-04)
Elharamain News adalah media milik travel, **bukan media bebas**, jadi setiap calon berita disortir dulu. Yang lolos hanya berita yang:
1. Bermanfaat dan relevan bagi jemaah/calon jemaah atau umat Islam Indonesia.
2. Bersumber resmi atau media kredibel, bukan rumor, unggahan viral tanpa konfirmasi, atau opini.
3. Membawa informasi baru, bukan pengulangan artikel 7 hari terakhir.
4. Aman bagi citra media: tanpa politik praktis, SARA, gosip, polemik antarormas/antartokoh, serangan kepada pemerintah Indonesia/Saudi, dan tanpa menyebut travel lain.
5. Bila negatif, punya nilai imbauan yang jelas bagi jemaah dan ditulis tenang.

Bila ragu, gugurkan. Laporan routine mencantumkan calon topik yang digugurkan beserta alasannya.

## Aturan gambar

### Gerbang gambar (ketat, perintah pemilik 2026-11-02)
Setiap gambar (foto utama dan sisipan) baru boleh dipasang bila lolos semua pemeriksaan ini. Bila satu gagal, gambar ditolak:
1. **Dilihat dulu**: tulis satu kalimat tentang apa yang benar-benar terlihat, bukan yang diharapkan dari nama file atau folder.
2. **Subjek sama dengan berita**: tokoh, masjid/tempat, objek, atau kegiatan yang diberitakan. "Masih satu kota" atau "nuansa Islami" tidak cukup.
3. **Identitas terbukti tertulis** di sumber foto (deskripsi Wikimedia, caption SPA/haji.go.id, nama subfolder Drive). Mirip saja tidak cukup.
4. **Nada sesuai**: berita negatif tanpa foto Elharamain, tanpa close-up wajah jemaah atau anak-anak.
5. **Mutu**: tidak buram, tanpa watermark media lain, crop rapi, dan bukan foto yang dipakai dalam 7 hari terakhir.
6. **Lisensi & kredit** sesuai aturan.

Bila ragu, anggap tidak cocok. Lebih baik tanpa gambar sisipan daripada gambar yang salah. **Audit akhir**: setelah semua artikel dibuat, setiap gambar diunduh ulang dari WordPress, dilihat, dan dicocokkan lagi dengan judul. Gambar yang tidak lolos diganti sebelum laporan, dan laporan mencantumkan hasil audit per gambar.

### Urutan pilihan gambar
1. Foto resmi haji.go.id (bila artikel dari rilisnya).
2. Foto asli Elharamain dari Google Drive – **hanya untuk berita positif/netral**.
3. Foto stok gratis: Pexels, Unsplash, Wikimedia CC0/Public Domain.
4. Gambar AI – hanya bila tidak ada foto asli yang cocok.

### Wajib
- **Utamakan foto asli.** AI hanya pilihan terakhir.
- **Artikel Media Arab memakai foto SPA dari sumber beritanya**, di-crop 16:9 (logo SPA di pojok kiri atas ikut dipotong) dan diberi tulisan kecil "Foto: SPA" di pojok kanan bawah gambar. Foto Arab News hanya boleh dipakai bila kreditnya (SPA); foto dari AFP/Reuters/staf Arab News tidak dipakai (contoh: post 16564 museum Sirah Nabi, 2 Nov 2026).
- **Topik objek spesifik wajib tampil di foto.** Artikel tentang merpati, Zamzam, kiswah, museum, kereta Haramain, dll. harus memakai foto objek itu – bukan foto rombongan jemaah atau suasana umum Masjidil Haram hanya karena lokasinya sama (contoh keliru: artikel merpati Tanah Haram, 1 Nov 2026).
- **Masjid, tempat ibadah, dan landmark** (Masjidil Haram, Nabawi, Quba, Al-Azhar, Hagia Sophia, Jabal Rahmah, dll.) **tidak boleh AI** – wajib foto asli.
- **Tokoh penting** (mis. Imam Besar Masjidil Haram Syekh Abdurrahman As-Sudais, Raja Saudi, menteri, pejabat, ulama) **wajib foto asli tokoh itu yang baru dan relevan** (utamakan foto dari acara yang diberitakan; bukan foto lama bertahun-tahun). Urutan: (1) foto tanpa kredit (Wikimedia CC0/PD, Pexels/Unsplash, haji.go.id); (2) **foto resmi lembaga** (SPA, Presidensi Haramain, Kementerian Haji Saudi, dll.) dengan **kredit kecil di pojok kanan bawah gambar**, mis. "Foto: SPA". (3) **Wikimedia CC BY/BY-SA boleh**, dengan **kredit sangat kecil** (mis. "Foto: Ahmad/CC BY-SA", 13 px, transparan, pojok kanan bawah, tidak menutupi wajah) agar estetika gambar tetap terjaga (aturan pemilik 2026-11-02). Tidak boleh AI, foto orang lain yang mirip, foto media swasta, atau Instagram. Bila tidak ada, pakai foto asli tempat/acara terkait, tetap bukan AI. Contoh: foto utama post 16592 (As-Sudais, khutbah 9/10/2026).
- **Foto masjid harus memperlihatkan bangunan masjidnya** (foto utama dan sisipan), bukan hanya bagian atas seperti kubah, menara, atau atap. Bila hasil crop hanya menyisakan bagian atas, ganti foto atau pasang foto utuh (aturan pemilik 2026-11-01, contoh: post 16629 Masjid Quba).
- **Foto masjid wajib masjid yang diberitakan itu sendiri** – tidak boleh foto masjid lain atau suasana kota. Bila tidak ada foto bebas kredit, boleh foto Wikimedia CC BY/BY-SA atau foto resmi lembaga dengan kredit kecil yang pendek di pojok kanan bawah gambar (mis. "Foto: SPA", "Foto: Ahmad/CC BY-SA").
- **Berita negatif** (gagal berangkat, tidak lolos kesehatan, sakit/wafat, penipuan, deportasi, sanksi, keluhan layanan, dll.) **tidak boleh memakai foto Elharamain dalam bentuk apa pun**, agar pembaca tidak mengira jemaah/layanan Elharamain yang bermasalah. Pakai gambar ilustrasi.
- **Gambar AI harus 99% seperti foto asli** (gaya foto dokumenter, kulit dan cahaya natural). Kalau terlihat buatan, buat ulang.
- **Caption gambar AI cukup "Ilustrasi"** – tanpa kata "AI".
- **Artikel internal (Kegiatan/tentang Elharamain): semua gambar hanya dari Google Drive Elharamain**. Tidak boleh gambar dari luar maupun ilustrasi AI (perintah pemilik 2026-11-05).
- **Artikel Kegiatan HANYA tentang KEGIATAN jemaah (ibadah, ziarah, tawaf, Raudhah, Jabal Rahmah, Quba, Uhud, wisata religi di lokasi), BUKAN keberangkatan** (perintah pemilik 2026-11-10): jangan pakai foto bandara/check-in/pesawat/pelepasan/manasik pra-berangkat/kopor, dan jangan sebut tanggal keberangkatan, bandara, maskapai, kepulangan, atau "berangkat dari ..." di judul maupun isi. Bila album didominasi foto keberangkatan, pilih album lain. **ATURAN PEMILIK 2026-11-11 (MENGGANTIKAN pengecualian spanduk 10 Nov & pola judul lama): TANGGAL KEBERANGKATAN DILARANG DITULIS di judul, isi, excerpt, caption, alt text, maupun teks link (termasuk link ke artikel Kegiatan lama). Sebut grup cukup dengan BULAN dan TAHUN keberangkatan, mis. "Group November 2026 Bronze" (bukan "Group 6 November"). Tanggal keberangkatan hanya boleh tampak di spanduk pada FOTO; jangan menyalin tulisan tanggal dari spanduk ke teks (tulis "spanduk bertuliskan nama grup"). Tanggal KEGIATAN (hari foto diambil) tetap boleh. Judul: "Group [Bulan Tahun] [Paket] [kegiatan utama]" atau "Jemaah Elharamain Wisata [kegiatan] ...".**
- **Ilustrasi AI harus sangat realistis dan sesuai artikel**: adegan menggambarkan tempat/kegiatan yang diberitakan, orangnya berwajah Indonesia/Melayu atau Arab sesuai latar. **Dilarang wajah bule/Barat** (perintah pemilik 2026-11-04).
- **Foto stok gratis dipasang tanpa kredit.** Foto yang lisensinya wajib kredit (Wikimedia CC BY / CC BY-SA) tidak dipakai, dan tidak boleh diedit untuk menghindari kredit.
- Foto Elharamain dari peristiwa/kegiatan yang diberitakan diberi caption "Foto: Dokumentasi Elharamain Wisata"; foto Elharamain yang hanya ilustrasi TANPA caption (tulisan "Foto ilustrasi: Dokumentasi Elharamain Wisata" dilarang, pemilik 2026-11-12); foto haji.go.id "Foto: Kementerian Haji dan Umrah RI".
- GAMBAR UTAMA ARTIKEL/SERI HAJI HARUS IDENTIK HAJI (pemilik 2026-11-26): Ka'bah/Masjidil Haram dengan jemaah berihram, tawaf/mataf, wukuf Arafah/Jabal Rahmah, tenda Mina, Muzdalifah, jamarat. JANGAN foto bandara, stasiun/kereta, hotel/lobi, penyambutan, makan bersama, selfie di masjid, atau Madinah — meski dari album haji. Pembaca harus langsung melihat "ini haji" dari gambar utama.
- GAMBAR UTAMA ARTIKEL HAJI = FOTO ROMBONGAN, MOMEN KHAS HAJI (ARMUZNA), SESUAI ISI ARTIKEL; BUKAN FOTO 1–2 ORANG/SELFIE (pemilik 2026-11-26 08:07). Urutan syarat: (1) rombongan/kelompok banyak orang; (2) momen yang tidak mungkin umroh — Arafah/wukuf, Jabal Rahmah, tenda Mina, Muzdalifah, jamarat, kawasan Masyair; foto rombongan di Masjidil Haram hanya bila tidak ada pilihan Masyair yang cocok dan alasannya dicatat; (3) cocok dengan isi (kesehatan/istithaah → rombongan lansia/perjalanan fisik; dokumen → rombongan berkartu identitas; rukun → wukuf/tawaf ifadah; khusus vs reguler → tenda berpendingin; kuota/cadangan → rombongan besar); (4) tajam, tanpa watermark, 16:9, tanpa caption, tidak dobel di seri maupun dengan gambar utama News 7 hari (bandingkan contact sheet `?w=240`; adegan sama dari sudut lain dihitung dobel). Foto album yang memuat spanduk/nama travel lain (mis. tenda bersebelahan) dilarang.

### Jumlah & potongan gambar
- **Bila memungkinkan, 1–2 gambar tambahan di dalam artikel** selain foto utama (artikel Kegiatan: 2–3 foto dari album grup). Tidak dipaksakan bila tidak ada yang cocok.
- **Foto boleh dipotong asal tetap enak dilihat**: foto utama 16:9, foto sisipan tegak 4:5.
- Jemaah tetap jadi fokus – kepala dan tangan tidak terpotong, latar ikonik (kubah, menara, Ka'bah) tetap masuk.
- **Dilarang memotong sampai jemaah hilang** dan hanya tersisa kubah, menara, atau langit. Bila potongan merusak komposisi, pasang foto utuh.
- Setiap gambar dilihat dulu sebelum dipasang.

## Gaya tulisan
- **Tulis seperti wartawan, bukan seperti AI** (perintah pemilik 2026-11-04). Sebelum menulis, baca 1–2 berita serupa di Kompas atau Detik dan tiru cara menulisnya (bukan menyalin isinya): lead langsung ke fakta inti, kalimat pendek, setiap paragraf membawa fakta, angka, nama, atau kutipan.
- **Dilarang ciri tulisan AI**: pembuka klise ("Di tengah...", "Dalam era..."), frasa pengisi ("Hal ini menunjukkan", "Perlu diketahui", "Tidak hanya... tetapi juga", "Secara keseluruhan", "Dengan demikian"), pertanyaan retoris, ajakan "mari", deretan tiga kata sifat, kata berlebihan ("luar biasa", "momen berharga", "langkah strategis"), paragraf yang mengulang atau ditutup petuah moral, dan tanda pisah panjang (—) di tengah kalimat.
- Draf dibaca ulang seperti redaktur Kompas/Detik sebelum dijadwalkan.
- Dibuka dengan **ELHARAMAIN NEWS –**, gaya berita lurus, Bahasa Indonesia baku.
- Tanpa subjudul dan bullet; 450–600 kata (Sejarah 250–450, Tanya Jawab s.d. 700).
- Ditutup dengan tips praktis bagi calon jemaah, lalu CTA WhatsApp 6281287292422.
- **Link keluar maksimal 1 per artikel** (perintah pemilik 2026-11-13): hanya satu link ke sumber utama; sumber lain disebut namanya tanpa link. Link internal news.elharamainwisata.com, CTA WhatsApp, dan situs utama elharamainwisata.com tidak dihitung.
- **Dilarang mengomentari travel lain** (perintah pemilik 2026-11-04): tidak menilai, mengkritik, menyindir, membandingkan, atau memuji biro travel umrah/haji lain. **Nama travel lain juga dilarang disebut sama sekali**, termasuk di berita penipuan atau pencabutan izin PPIU walau sumber resminya menyebut nama. Tulis "sebuah biro perjalanan" atau angkat imbauan umumnya saja; bila berita tidak bisa ditulis tanpa nama travel, jangan ditulis.
