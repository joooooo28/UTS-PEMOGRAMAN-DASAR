# Lembar Jawaban UTS – Pemrograman Dasar (TK091)

## Judul
Transaction Management System (Sistem Pengolahan Data Transaksi Penjualan)

## 1. Permasalahan, tujuan, pengguna, input, output, fitur
Permasalahan yang dipilih adalah pencatatan dan rekapitulasi transaksi penjualan toko. Jika pencatatan dilakukan secara manual, pencarian transaksi dan perhitungan pendapatan membutuhkan waktu serta berisiko salah hitung.

Tujuan aplikasi adalah membantu kasir/admin mencatat, mencari, menyaring, menghapus, dan merekap transaksi. Target pengguna adalah kasir, admin, dan pemilik toko.

Input berupa ID transaksi, tanggal (YYYY-MM-DD), nama pelanggan, produk, jumlah, dan harga satuan dalam rupiah. Output berupa tabel transaksi, hasil pencarian/filter, rekap penjualan, file CSV transaksi, dan file JSON rekap.

Fitur utama: tambah transaksi, tampilkan transaksi, pencarian ID, filter tanggal, rekap pendapatan dan produk, hapus transaksi, serta ekspor laporan.

## 2. Struktur data dan manipulasi
List digunakan untuk menampung banyak dictionary transaksi karena mudah diiterasi dan difilter. Dictionary digunakan untuk merepresentasikan satu transaksi dengan pasangan kunci-nilai sehingga atribut dapat diakses melalui nama kolom. Set digunakan untuk menyimpan ID transaksi yang sudah ada dan memeriksa duplikasi tanpa mengulang seluruh proses pencarian secara manual.

Fitur pencarian diimplementasikan oleh `cari_transaksi`, filtering oleh `filter_tanggal`, penghapusan oleh `hapus_transaksi`, dan rekapitulasi oleh `buat_rekap`.

## 3. Control flow dan Pythonic programming
Percabangan `if/elif/else` mengarahkan pilihan menu. Perulangan `while` menjaga menu tetap berjalan sampai pengguna memilih keluar, sedangkan `for` memproses setiap transaksi. List comprehension digunakan untuk filter dan penghapusan data. Set comprehension digunakan untuk membentuk kumpulan ID yang sudah terpakai.

Edge case yang ditangani antara lain data kosong, ID duplikat, tanggal tidak valid, jumlah nol/negatif, harga negatif, serta input jumlah/harga yang bukan angka.

## 4. Function, module, dan package
Package buatan sendiri adalah `transaksi`. Module `crud.py` menangani validasi dan manipulasi data, `laporan.py` menghitung rekap, dan `file_handler.py` menangani file. `main.py` bertanggung jawab atas interaksi CLI dan menghubungkan module.

Setiap function memiliki tanggung jawab terpisah, parameter yang jelas, dan nilai kembali. Docstring singkat tersedia pada function utama. Alur dependensi: `main.py` memanggil fungsi dari ketiga module; `file_handler.py` menggunakan `validasi_transaksi` dari `crud.py`.

## 5. Pemrosesan CSV/JSON
Aplikasi membaca data transaksi dari `data/transaksi.csv` menggunakan `csv.DictReader`. Data divalidasi, ditransformasi ke tipe integer untuk jumlah dan harga, lalu disimpan kembali dengan `csv.DictWriter`. Rekap hasil analisis disimpan ke `output/rekap_transaksi.json` menggunakan `json.dump`. Contoh input dan output disertakan dalam proyek.

## 6. Exception handling, defensive programming, debugging, README
Program menangani `FileNotFoundError`/`OSError`, `ValueError`, format tanggal salah, header CSV tidak sesuai, ID duplikat, serta input numerik yang tidak valid. Validasi dilakukan sebelum data ditambahkan. Jika ID duplikat ditemukan, operasi dibatalkan dan data lama tetap utuh.

Skenario debugging: ketika pengguna memasukkan jumlah barang berupa teks, konversi `int()` memunculkan `ValueError`; exception ditangkap di menu tambah transaksi dan program kembali ke menu tanpa menghentikan aplikasi. README berisi struktur folder, cara menjalankan, format data, module, dependency, dan pengujian.

## Pengujian yang disediakan
File `tests/test_transaksi.py` menguji penambahan/pencarian, penolakan ID duplikat, filter tanggal, rekap pendapatan, dan penghapusan. Jalankan `python -m unittest discover -s tests -v`.

## Referensi dan bantuan
- Python Standard Library Documentation: https://docs.python.org/3/library/
- Library: `csv`, `json`, `pathlib`, `datetime`, `unittest` (seluruhnya standard library).
- Bantuan AI: ChatGPT (OpenAI), digunakan untuk membantu penyusunan rancangan dan contoh kode.
