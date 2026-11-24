# Posts-create Ronde A 25 Nov 2026 (subagen pengunggah)
Situs WordPress.com 257737206 (tool MCP wordpress-com, wpcom-mcp-posts-create). Status HANYA "future" (JANGAN publish). Kirim user_confirmed: true bila diminta.
Semua gambar SUDAH diunggah; final.html SUDAH jadi. ID foto utama di `media_ids.txt` (baris "<slot> 1 <id> <url>").

Untuk tiap folder slot (0700 0740 0800 0820 0940 1020 1040 1100 1140 1200 1220 1300 1320 1340 1420):
- title, excerpt, categories [category], tags (maks 5), date = field "slot" di `<folder>/article.json` (PERHATIAN: folder 1200 bertanggal 13:00 dan folder 1300 bertanggal 12:00 — pakai field slot, bukan nama folder).
- content = isi `<folder>/final.html` PERSIS (baca file, jangan diubah).
- featured_media = ID gambar 1 slot itu dari media_ids.txt.
- meta {"jetpack_publicize_feature_enabled": false}; status "future".
Periksa _content_warnings (meta_keys_dropped untuk jetpack itu normal; lapor bila markup dibuang).
Verifikasi: wpcom-mcp-posts-list status ["future"] after 2026-11-25T00:00:00 per_page 50 → harus ada 15 post baru 07:00–14:20 (+19028 09:00). Tulis `posts.txt`: "folder id date status title".
Jangan membuat post ganda: bila gagal di tengah, cek posts-list dulu sebelum mengulang.
Laporan: tabel folder→post id→date→featured id, masalah. Jangan tempel naskah.
