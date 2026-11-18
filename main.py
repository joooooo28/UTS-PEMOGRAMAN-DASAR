from transaksi.crud import tambah_transaksi, tampilkan_transaksi, cari_transaksi, filter_tanggal, hapus_transaksi
from transaksi.laporan import buat_rekap, tampilkan_rekap
from transaksi.file_handler import baca_csv, simpan_csv, simpan_json

DATA_FILE = "data/transaksi.csv"

def tampilkan_menu():
    print("\n" + "=" * 43)
    print("       TRANSACTION MANAGEMENT SYSTEM")
    print("=" * 43)
    print("1. Tambah transaksi")
    print("2. Tampilkan transaksi")
    print("3. Cari transaksi berdasarkan ID")
    print("4. Filter transaksi berdasarkan tanggal")
    print("5. Rekap penjualan")
    print("6. Hapus transaksi")
    print("7. Export laporan (CSV dan JSON)")
    print("0. Keluar")
    print("=" * 43)

def main():
    try:
        transaksi = baca_csv(DATA_FILE)
    except (OSError, ValueError) as error:
        print(f"Gagal membaca data awal: {error}")
        transaksi = []

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            try:
                item = {
                    "id": input("ID transaksi: ").strip(),
                    "tanggal": input("Tanggal (YYYY-MM-DD): ").strip(),
                    "pelanggan": input("Nama pelanggan: ").strip(),
                    "produk": input("Nama produk: ").strip(),
                    "jumlah": int(input("Jumlah barang: ")),
                    "harga": int(input("Harga satuan (rupiah): "))
                }
                transaksi = tambah_transaksi(transaksi, item)
                simpan_csv(DATA_FILE, transaksi)
                print("Transaksi berhasil ditambahkan.")
            except ValueError as error:
                print(f"Input tidak valid: {error}")
            except OSError as error:
                print(f"Gagal menyimpan data: {error}")

        elif pilihan == "2":
            tampilkan_transaksi(transaksi)

        elif pilihan == "3":
            id_cari = input("Masukkan ID transaksi: ").strip()
            hasil = cari_transaksi(transaksi, id_cari)
            tampilkan_transaksi([hasil] if hasil else [])
            if hasil is None:
                print("Transaksi tidak ditemukan.")

        elif pilihan == "4":
            tanggal = input("Tanggal (YYYY-MM-DD): ").strip()
            try:
                hasil = filter_tanggal(transaksi, tanggal)
                tampilkan_transaksi(hasil)
                print(f"Jumlah hasil: {len(hasil)}")
            except ValueError as error:
                print(f"Format tanggal salah: {error}")

        elif pilihan == "5":
            rekap = buat_rekap(transaksi)
            tampilkan_rekap(rekap)

        elif pilihan == "6":
            id_hapus = input("ID transaksi yang dihapus: ").strip()
            transaksi, berhasil = hapus_transaksi(transaksi, id_hapus)
            if berhasil:
                try:
                    simpan_csv(DATA_FILE, transaksi)
                    print("Transaksi berhasil dihapus.")
                except OSError as error:
                    print(f"Gagal menyimpan perubahan: {error}")
            else:
                print("ID transaksi tidak ditemukan.")

        elif pilihan == "7":
            try:
                rekap = buat_rekap(transaksi)
                simpan_csv("output/laporan_transaksi.csv", transaksi)
                simpan_json("output/rekap_transaksi.json", rekap)
                print("Laporan tersimpan di folder output/.")
            except OSError as error:
                print(f"Gagal mengekspor laporan: {error}")

        elif pilihan == "0":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak tersedia. Masukkan angka 0 sampai 7.")

if __name__ == "__main__":
    main()
