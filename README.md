# Transaction Management System

Aplikasi CLI Python untuk mengelola transaksi penjualan toko. Dibuat menggunakan Python standard library tanpa dependency eksternal.

## Fitur
1. Tambah transaksi dengan validasi input dan ID unik.
2. Tampilkan seluruh transaksi.
3. Cari transaksi berdasarkan ID.
4. Filter transaksi berdasarkan tanggal.
5. Rekap jumlah transaksi, unit terjual, pendapatan, dan penjualan per produk.
6. Hapus transaksi berdasarkan ID.
7. Ekspor daftar transaksi ke CSV dan rekap ke JSON.

## Persyaratan
- Python 3.9 atau lebih baru.
- Tidak membutuhkan instalasi package tambahan.

## Struktur proyek
```text
transaction_management/
├── main.py
├── README.md
├── data/transaksi.csv
├── output/
└── transaksi/
    ├── __init__.py
    ├── crud.py
    ├── laporan.py
    └── file_handler.py
```

## Cara menjalankan
Jalankan dari direktori utama proyek:

```bash
python main.py
```

Pilih menu melalui terminal. Data awal dibaca dari `data/transaksi.csv`. Perubahan tambah/hapus disimpan kembali ke file tersebut.

## Format data CSV
Header wajib:
`id,tanggal,pelanggan,produk,jumlah,harga`

- tanggal: YYYY-MM-DD
- jumlah: bilangan bulat lebih dari 0
- harga: bilangan bulat rupiah, minimal 0
- id: harus unik

## Struktur data yang digunakan
- **List** menyimpan kumpulan transaksi dan memudahkan iterasi/filter.
- **Dictionary** menyimpan atribut satu transaksi sebagai pasangan kunci-nilai serta hasil rekap.
- **Set** menyimpan ID yang telah digunakan agar pemeriksaan duplikasi efisien.

## Control flow dan comprehension
Program memakai `if/elif/else` untuk menu, `while` untuk mengulang menu, `for` untuk memproses transaksi, list comprehension untuk filter/hapus, set comprehension untuk ID unik, dan dictionary comprehension dapat diterapkan untuk transformasi data. Implementasi set comprehension terdapat pada `tambah_transaksi`.

## Pembagian module dan alur dependensi
- `main.py`: antarmuka CLI dan pengendali alur program.
- `transaksi/crud.py`: validasi, tambah, tampil, cari, filter, dan hapus.
- `transaksi/laporan.py`: perhitungan dan tampilan rekap.
- `transaksi/file_handler.py`: baca/tulis CSV dan JSON.
- `transaksi/__init__.py`: menandai folder `transaksi` sebagai package buatan sendiri.

Alur: `main.py` memanggil `file_handler` untuk membaca/menulis data, `crud` untuk manipulasi transaksi, dan `laporan` untuk rekapitulasi. `file_handler` menggunakan validasi dari `crud`.

## Penanganan kesalahan
Program menangani file tidak ditemukan, header/isi CSV tidak valid, tanggal salah, nilai jumlah/harga tidak sesuai, ID duplikat, input angka bukan bilangan bulat, serta pilihan menu tidak dikenal. Contoh debugging: masukkan ID transaksi yang sudah ada; fungsi `tambah_transaksi` menolak data dengan `ValueError` dan data lama tidak berubah.

## Pengujian
Jalankan:
```bash
python -m unittest discover -s tests -v
```

## Referensi dan bantuan
- Python documentation: https://docs.python.org/3/library/
- Modul yang digunakan: `csv`, `json`, `pathlib`, `datetime`, `unittest` (standard library).
- Bantuan AI: ChatGPT (OpenAI), digunakan untuk membantu menyusun rancangan dan contoh implementasi; kode tetap perlu dipahami, diuji, dan disesuaikan oleh mahasiswa.
