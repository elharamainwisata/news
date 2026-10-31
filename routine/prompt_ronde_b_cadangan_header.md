== MODE CADANGAN RONDE B (routine 14:00 WIB) - BACA DULU ==
Routine ini adalah CADANGAN bila Ronde B (11:00 WIB) gagal, mis. karena batas pemakaian akun. LANGKAH PERTAMA, sebelum apa pun (sebelum venv, riset, atau membaca bagian lain):
1. posts.list status future, publish, dan draft, after = hari ini 14:25 WIB, before = besok 00:00 WIB, per_page 50, include_fields [id,title,date,status,categories]. Bila tanggal hari ini ragu, jalankan date di Bash (zona WIB = UTC+7).
2. Cocokkan dengan 12 slot Ronde B di bawah (15:00 sampai 22:20). Bila sudah ada 10 post atau lebih di rentang itu (artinya Ronde B sudah berjalan), BERHENTI: tulis satu baris "Ronde B hari ini sudah lengkap, cadangan tidak bekerja." lalu selesai. Jangan riset atau membuat apa pun.
3. Bila ada slot yang kosong, kerjakan HANYA slot yang kosong itu dengan seluruh aturan RONDE B di bawah. Topik wajib berbeda dari semua post yang sudah ada hari ini. Slot yang waktunya sudah lewat digeser sesuai aturan geser slot. Di laporan, sebut bahwa ini run cadangan dan slot mana saja yang diisi.

