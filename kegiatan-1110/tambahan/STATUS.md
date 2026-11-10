# Tambahan 4 Kegiatan 10 Nov 2026 (agen News, ditulis ~09:20 WIB)
STATUS: SELESAI 10 Nov ~09:50 WIB oleh Bos (sesi dashboard, MCP WordPress hidup): 4 post future dibuat. MCP wordpress-com di sesi agen News menolak otorisasi
("rejected the Authorization header"), cadangan REST backup/wp.py juga kosong (WP_NEWS_USER/PASS tidak diisi).

| key | jadwal (future) | album Drive | judul |
|---|---|---|---|
| a | 2026-11-10T11:20:00 | 1448 H/1.JUNI/14 JUNI 2026 PLATINUM (1UwpjSpBbDNv1PzuzX2cCZG-bh_Fwj5Tn) | lihat a.json |
| b | 2026-11-10T13:20:00 | 1448 H/1.JUNI/24 JUNI 2026 12HARI (1F8aq0YPSpqfrZWVFCVodOPk9N8CyEh0e) | lihat b.json |
| c | 2026-11-10T18:00:00 | 1448 H/2.JULI/12 JULI 2026 TURKI (1hThJtxg3RfoZ3L_KBXrcWMXqYqnafwHl) | lihat c.json |
| d | 2026-11-10T20:00:00 | 1448 H/2.JULI/29 JULI 2026 QATAR (1Boba7VLTkD4UOKisCtMBppVSAJZkzE9R) | lihat d.json |

Cara lanjut per artikel (sesi yang MCP wordpress-com-nya hidup, site 257737206):
1. Cek ulang post future (jangan bentrok menit, jeda >=20 menit, Ronde B pakai grid 15:00,15:40,...,22:20). Bila slot lewat/bentrok, geser ke menit tengah kosong berikutnya (<=22:50).
2. Unggah 4 foto <key> (images.* di <key>.json): wpcom-media-upload count=4 -> jalankan upload_command -> wpcom-media-create upload_ref + sha256 (lihat sha256.txt), alt_text = alt di json, caption "Foto: Dokumentasi Elharamain Wisata".
3. python3 isi.py <key> '{"2":[ID,"URL-large"],"3":[ID,"URL"],"4":[ID,"URL"]}'  -> <key>.final.html
4. posts.create: status future, date dari json, categories [24], tags [34] (tambah tag lain bila perlu), featured_media = ID gambar 1, title/excerpt dari json, content = <key>.final.html.
Semua foto dari Drive Elharamain, tanpa foto/teks keberangkatan (dicek). Makassar diganti 24 Juni 12 Hari.


## Hasil (Bos, 10 Nov 2026)
- a: post 17456, 2026-11-10 11:20, foto utama media 17440
- b: post 17457, 2026-11-10 13:20, foto utama media 17444
- c: post 17458, 2026-11-10 18:00, foto utama media 17448
- d: post 17459, 2026-11-10 20:00, foto utama media 17452
Media 17440-17455 (16 foto). Semua status future, kategori 24, tag 34.
