from datetime import datetime

FIELD_NAMES = {"id", "tanggal", "pelanggan", "produk", "jumlah", "harga"}

def validasi_transaksi(item):
    """Memvalidasi kolom, tanggal, dan nilai transaksi; mengembalikan True jika valid."""
    if not isinstance(item, dict) or not FIELD_NAMES.issubset(item):
        raise ValueError("Data transaksi harus berisi id, tanggal, pelanggan, produk, jumlah, dan harga.")
    for key in ("id", "pelanggan", "produk"):
        if not str(item[key]).strip():
            raise ValueError(f"{key} tidak boleh kosong.")
    try:
        datetime.strptime(item["tanggal"], "%Y-%m-%d")
    except (TypeError, ValueError):
        raise ValueError("Tanggal harus menggunakan format YYYY-MM-DD.")
    if int(item["jumlah"]) <= 0 or int(item["harga"]) < 0:
        raise ValueError("Jumlah harus lebih dari 0 dan harga tidak boleh negatif.")
    return True

def tambah_transaksi(data, item):
    """Menambahkan transaksi baru; mengembalikan list transaksi yang telah diperbarui."""
    validasi_transaksi(item)
    id_tersedia = {row["id"] for row in data}
    if item["id"] in id_tersedia:
        raise ValueError(f"ID transaksi {item['id']} sudah digunakan.")
    baru = dict(item)
    baru["jumlah"] = int(baru["jumlah"])
    baru["harga"] = int(baru["harga"])
    return data + [baru]

def tampilkan_transaksi(data):
    """Menampilkan daftar transaksi ke terminal; mengembalikan jumlah baris."""
    if not data:
        print("Belum ada data transaksi.")
        return 0
    print("-" * 88)
    print(f"{'ID':<10} {'Tanggal':<12} {'Pelanggan':<16} {'Produk':<18} {'Qty':>5} {'Harga':>12} {'Total':>14}")
    print("-" * 88)
    for row in data:
        total = int(row["jumlah"]) * int(row["harga"])
        print(f"{row['id']:<10} {row['tanggal']:<12} {row['pelanggan']:<16} {row['produk']:<18} {row['jumlah']:>5} {row['harga']:>12,} {total:>14,}")
    print("-" * 88)
    return len(data)

def cari_transaksi(data, transaction_id):
    """Mencari satu transaksi berdasarkan ID; mengembalikan dictionary atau None."""
    return next((row for row in data if row["id"] == transaction_id), None)

def filter_tanggal(data, tanggal):
    """Memfilter transaksi pada tanggal tertentu; mengembalikan list hasil."""
    from datetime import datetime
    datetime.strptime(tanggal, "%Y-%m-%d")
    return [row for row in data if row["tanggal"] == tanggal]

def hapus_transaksi(data, transaction_id):
    """Menghapus transaksi berdasarkan ID; mengembalikan (data_baru, status)."""
    hasil = [row for row in data if row["id"] != transaction_id]
    return hasil, len(hasil) != len(data)
