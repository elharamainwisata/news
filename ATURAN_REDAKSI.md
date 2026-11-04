# Aturan Redaksi Elharamain News

Ringkasan aturan dari pemilik untuk artikel news.elharamainwisata.com. Aturan lengkap yang dijalankan routine ada di `routine/prompt_ronde_a.md` dan `routine/prompt_ronde_b.md`.

## Jadwal & routine

| Routine | Jadwal (WIB) | Isi |
|---|---|---|
| Ronde A | 05:00, terbit 07:00–14:20 (jeda 40 menit) | 12 artikel: Umroh & Haji 3, Berita 3, Fiqih, Sejarah Islam, Tanya Jawab, Kegiatan, Dunia Islam, Media Arab |
| Ronde B | 11:00, terbit 15:00–22:20 (jeda 40 menit) | 12 artikel: Umroh & Haji 2, Berita 3, Sejarah Islam, Kegiatan, Dunia Islam, Media Arab, Hikmah, Wisata Halal, Lifestyle Muslim; topik berbeda dari Ronde A |
| Cadangan Ronde B | 14:00 | Cek slot sore; bila Ronde B gagal, isi slot yang kosong. Bila lengkap, langsung berhenti |
| Laporan WA | 07:00 | Judul + link artikel kemarin ke grup WA redaksi (OneSender) |
| Pemimpin Redaksi (QC) | 06:30 & 12:30 | Kroscek semua artikel terjadwal hasil Ronde A/B sebelum terbit: sortir, nama travel lain, fakta vs sumber, kalimat salinan, gaya AI, gambar. Memperbaiki yang salah, menahan (draft) yang tidak layak, lalu melapor. Prompt: `routine/prompt_pemred.md` |

- Artikel dijadwalkan (status *future*), tidak pernah langsung *publish*.
- Tidak ada lagi caption media sosial.

## Sumber berita

1. **haji.go.id** (Kementerian Haji dan Umrah RI) – sumber utama, minimal 5 dari 10 artikel kategori per ronde (di luar Kegiatan dan Media Arab). Termasuk ppid.haji.go.id dan **subdomain provinsi** (`dki.haji.go.id`, `jabar.haji.go.id`, `banten.haji.go.id`, dst.); prioritas DKI, Jabar, Banten, usahakan 1–2 artikel per ronde dari situs provinsi.
2. **BPKH** (bpkh.go.id) – dana haji, nilai manfaat, BPIH.
3. **Media Arab** (Arab News, SPA, haj.gov.sa, Nusuk, Saudi Gazette) – 2 artikel per hari (pagi 1, sore 1), kategori Umroh & Haji atau Dunia Islam sesuai isi.
4. **Instagram resmi**: @mediacenterhaji.ri (Media Center Haji) dan @gus.irfanyusuf (Menteri Haji dan Umrah).
5. Situs resmi lain: haj.gov.sa, spa.gov.sa, nusuk.sa, kemlu.go.id, moi.gov.sa, moh.gov.sa, kemkes.go.id.
6. Media: Antara, Republika, Kompas, Detik, NU Online, MUI, Muhammadiyah, dll.

Semua fakta, angka, dan kutipan harus dari sumber yang benar-benar dibaca. Tidak boleh mengarang.

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
- **Ilustrasi AI harus sangat realistis dan sesuai artikel**: adegan menggambarkan tempat/kegiatan yang diberitakan, orangnya berwajah Indonesia/Melayu atau Arab sesuai latar. **Dilarang wajah bule/Barat** (perintah pemilik 2026-11-04).
- **Foto stok gratis dipasang tanpa kredit.** Foto yang lisensinya wajib kredit (Wikimedia CC BY / CC BY-SA) tidak dipakai, dan tidak boleh diedit untuk menghindari kredit.
- Foto Elharamain diberi caption "Foto: Dokumentasi Elharamain Wisata"; foto haji.go.id "Foto: Kementerian Haji dan Umrah RI".

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
- **Dilarang mengomentari travel lain** (perintah pemilik 2026-11-04): tidak menilai, mengkritik, menyindir, membandingkan, atau memuji biro travel umrah/haji lain. **Nama travel lain juga dilarang disebut sama sekali**, termasuk di berita penipuan atau pencabutan izin PPIU walau sumber resminya menyebut nama. Tulis "sebuah biro perjalanan" atau angkat imbauan umumnya saja; bila berita tidak bisa ditulis tanpa nama travel, jangan ditulis.
