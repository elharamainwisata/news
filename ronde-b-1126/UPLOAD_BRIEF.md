# Unggah & posts-create Ronde B 26 Nov 2026 (subagen pengunggah)
Situs WordPress.com 257737206 (tool MCP wordpress-com). Status post HANYA "future" (JANGAN publish). Kirim user_confirmed: true bila diminta. Folder: /home/khaeruddien/elharamain-news/ronde-b-1126
Semua gambar sudah lolos gerbang gambar oleh induk; JANGAN ganti gambar/teks.

LANGKAH 1 — unggah 15 gambar sisa (daftar `up_list2.txt`: "slot n file sha256 | caption | alt"):
- wpcom-media-upload count 10 lalu count 5 → untuk tiap file jalankan curl dari upload_command (`curl -sS --fail-with-body -H 'Authorization: Bearer <token>' -F 'file=@<file>' '<upload_url>'`) — simpan token ke file sementara di /tmp/rb lewat skrip, jangan cetak ulang token di laporan.
- wpcom-media-create upload_ref + sha256 + filename (basename file) + alt_text (= alt) + caption (= caption; kosong bila kosong).
- Tambahkan baris "slot n id source_url" ke `media_ids.txt` (format sama dengan baris yang ada). Total harus 27 baris.
LANGKAH 2 — final.html: untuk tiap slot (1500 1540 1600 1620 1700 1740 1820 1840 1900 1940 2020 2100 2120 2140 2220) jalankan
`python3 fin.py <slot> '<json>'` dengan json = {"2":[id,"url"],"3":[...],...} untuk gambar n≥2 slot itu (url = source_url versi besar, mis. -1024x... boleh source_url penuh). Slot tanpa sisipan: `python3 fin.py <slot> '{}'`. Pastikan tidak ada "%%IMG" tersisa di final.html.
LANGKAH 3 — posts-create untuk tiap slot: title, excerpt, categories [category], tags (maks 5, potong bila lebih), date = field "slot" di article.json, content = isi final.html PERSIS, featured_media = id gambar 1 slot itu, meta {"jetpack_publicize_feature_enabled": false}, status "future". Periksa _content_warnings (meta_keys_dropped jetpack normal; lapor bila markup dibuang). Bila future ditolak izin → draft dan lapor.
Jangan membuat post ganda: bila gagal di tengah, cek wpcom-mcp-posts-list status future after 2026-11-26T14:30:00 dulu.
Verifikasi: posts-list status ["future"] after 2026-11-26T14:30:00 per_page 50 → 15 post 15:00–22:20. Tulis `posts.txt`: "folder id date status title".
Laporan: tabel slot→post id→date→featured id, masalah. Jangan tempel naskah/token.
