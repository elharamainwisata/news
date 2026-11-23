# Unggah Ronde A 24 Nov 2026 (subagen pengunggah)
Situs WordPress.com 257737206 (tool MCP wordpress-com). Status post HANYA "future" (JANGAN publish). user_confirmed bila diminta.

1. SEGERA (token kedaluwarsa 05:26 WIB): 10 berkas di `up1_res.txt` SUDAH terkirim ke storage. Untuk tiap baris (slot n upload_ref sha256): panggil wpcom-media-create {wpcom_site:"257737206", upload_ref, sha256, alt_text=images.n.alt, caption=images.n.caption (kosong bila "" ), title=nama file tanpa ekstensi} dari `<slot>/article.json`. Bila ref kedaluwarsa, ulangi lewat langkah 2.
2. 12 berkas di `b2.txt` (slot n file sha256): wpcom-media-upload count 10 lalu count 2; kirim tiap berkas: `curl -sS --fail-with-body -H "Authorization: Bearer <token>" -F "file=@<file>" https://public-api.wordpress.com/wpcom/v2/ai/asset/upload` (simpan token ke file sementara, jangan tempel ke laporan), lalu wpcom-media-create seperti di atas.
3. Catat `media_ids.txt`: "slot n media_id source_url" (source_url ukuran penuh dari respons).
4. Untuk tiap slot (0700 0740 0820 0940 1020 1040 1100 1140 1220 1300 1340 1420): jalankan `python3 fin.py <slot> '{"2":[ID,"URL"],...}'` (hanya gambar n>=2) → `<slot>/final.html`. Pastikan output: frasa [] , CTA ok, pembuka ok, tidak ada %%IMG tersisa.
5. posts-create per slot: title, excerpt, content = isi `<slot>/final.html` persis, status "future", date = article.json slot (WIB, mis. 2026-11-24T07:00:00), categories [category], tags (maks 5), featured_media = ID gambar 1, meta {"jetpack_publicize_feature_enabled": false}. Periksa _content_warnings (meta_keys_dropped untuk jetpack itu normal).
6. Verifikasi: wpcom-mcp-posts-list status future after 2026-11-24T00:00 → 12 post baru jam 07:00–14:20 (plus 19027 jam 09:00 yang sudah ada). Tulis `posts.txt`: "slot id date status title".
7. Audit gambar: unduh tiap gambar dari source_url (wp-content/uploads/2026/11/...; versi -768x... bila ada) ke /tmp/audit1124/, pastikan 200 & ukuran wajar; lapor bila ada yang gagal.
Laporan ke induk: tabel slot→post id→featured id, jumlah sisipan, masalah. Jangan tempel token/naskah.
