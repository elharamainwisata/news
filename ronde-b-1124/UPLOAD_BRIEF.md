# Posting Ronde B 24 Nov 2026 (subagen pengunggah)
Situs WordPress.com 257737206 (tool MCP wordpress-com, mis. mcp__wordpress-com__wpcom-mcp-posts-create; muat dengan ToolSearch "select:mcp__wordpress-com__wpcom-mcp-posts-create,mcp__wordpress-com__wpcom-mcp-posts-list"). Status HANYA "future" (JANGAN publish). Kirim user_confirmed bila diminta tool.
Untuk tiap slot berurutan 1500 1540 1620 1700 1740 1820 1900 1940 2020 2100 2140 2220 di /home/khaeruddien/elharamain-news/ronde-b-1124/:
- baca <slot>/article.json (title, excerpt, slot, category, tags) dan <slot>/final.html (isi PERSIS, jangan diubah).
- posts-create: wpcom_site "257737206", title, excerpt, content = final.html, status "future", date = slot (WIB, mis. 2026-11-24T15:00:00), categories [category], tags (maks 5), featured_media = FEAT di bawah, meta {"jetpack_publicize_feature_enabled": false}. include_fields [id,status,date,link,title]. Periksa _content_warnings (meta_keys_dropped jetpack normal; laporkan peringatan lain).
FEAT: 1500=19512 1540=19501 1620=19502 1700=19503 1740=19505 1820=19506 1900=19510 1940=19514 2020=19518 2100=19515 2140=19520 2220=19511
Bila satu gagal, lanjut slot lain dan catat error. Jangan membuat post dobel: sebelum mulai & bila ragu, cek posts-list status future after 2026-11-24T14:30:00.
Verifikasi akhir: posts-list status ["future"] after 2026-11-24T14:30:00 per_page 50 include_fields [id,date,status,title,featured_media]. Tulis /home/khaeruddien/elharamain-news/ronde-b-1124/posts.txt: "slot id date status title" per baris.
Laporan ringkas ke induk: tabel slot→id→status→featured, error/peringatan. Jangan tempel naskah.
