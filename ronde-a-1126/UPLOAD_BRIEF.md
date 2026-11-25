# Unggah & posts-create Ronde A 26 Nov 2026 (subagen pengunggah)
Situs WordPress.com 257737206 (tool MCP wordpress-com). Status post HANYA "future" (JANGAN publish). Kirim user_confirmed: true bila diminta. Folder: /home/khaeruddien/elharamain-news/ronde-a-1126
Semua gambar sudah lolos gerbang gambar oleh induk; JANGAN ganti gambar/teks.

LANGKAH 1 — unggah 22 gambar (daftar `up_list.txt`: "slot n file sha256 | caption | alt"):
- wpcom-media-upload count 10, count 10, count 2 → untuk tiap file jalankan curl dari upload_command (`curl -sS --fail-with-body -H 'Authorization: Bearer <token>' -F 'file=@<file>' '<upload_url>'`) — simpan token ke file sementara di /tmp/ra26 lewat skrip, jangan cetak ulang token di laporan.
- wpcom-media-create upload_ref + sha256 + filename (basename file) + alt_text (= alt) + caption (= caption; kosong bila kosong).
- Tambahkan baris "slot n id source_url" ke `media_ids.txt` (format sama dengan baris 0700 yang sudah ada). Total harus 23 baris.
LANGKAH 2 — final.html: untuk tiap slot (0700 0740 0800 0820 0940 1020 1040 1100 1140 1200 1220 1300 1320 1340 1420) jalankan
`python3 fin.py <slot> '<json>'` dengan json = {"2":[id,"url"],"3":[...]} untuk gambar n≥2 slot itu (url = source_url). Slot tanpa sisipan: `python3 fin.py <slot> '{}'`. Pastikan tidak ada "%%IMG" tersisa di final.html.
LANGKAH 3 — posts-create untuk tiap slot: title, excerpt, categories [category], tags (maks 5), date = field "slot" di article.json (PERHATIAN: folder 1200 bertanggal 13:00 dan folder 1300 bertanggal 12:00 — pakai field slot, bukan nama folder), content = isi final.html PERSIS (baca file, jangan diubah), featured_media = id gambar 1 slot itu, meta {"jetpack_publicize_feature_enabled": false}, status "future". Periksa _content_warnings (meta_keys_dropped jetpack normal; lapor bila markup dibuang). Bila future ditolak izin → draft dan lapor.
Jangan membuat post ganda: bila gagal di tengah, cek wpcom-mcp-posts-list status future after 2026-11-26T06:00:00 dulu.
Verifikasi: posts-list status ["future"] after 2026-11-26T06:00:00 per_page 50 → 15 post baru 07:00–14:20 (+19029 09:00). Tulis `posts.txt`: "folder id date status title".
Laporan: tabel slot→post id→date→featured id, masalah. Jangan tempel naskah/token.
