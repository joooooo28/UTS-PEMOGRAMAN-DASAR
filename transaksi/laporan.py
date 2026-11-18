def buat_rekap(data):
    """Menghitung ringkasan penjualan dan total per produk; mengembalikan dictionary."""
    total_transaksi = len(data)
    total_item = sum(int(row["jumlah"]) for row in data)
    pendapatan = sum(int(row["jumlah"]) * int(row["harga"]) for row in data)
    per_produk = {}
    for row in data:
        per_produk[row["produk"]] = per_produk.get(row["produk"], 0) + int(row["jumlah"])
    return {
        "total_transaksi": total_transaksi,
        "total_produk_terjual": total_item,
        "total_pendapatan": pendapatan,
        "penjualan_per_produk": per_produk
    }

def tampilkan_rekap(rekap):
    """Menampilkan dictionary rekapitulasi ke terminal; mengembalikan None."""
    print("\n========== REKAP PENJUALAN ==========")
    print(f"Total transaksi   : {rekap['total_transaksi']}")
    print(f"Produk terjual    : {rekap['total_produk_terjual']}")
    print(f"Total pendapatan  : Rp{rekap['total_pendapatan']:,}")
    print("Penjualan per produk:")
    if not rekap["penjualan_per_produk"]:
        print("  Belum ada penjualan.")
    for produk, jumlah in rekap["penjualan_per_produk"].items():
        print(f"  - {produk}: {jumlah} unit")
    print("=====================================")
