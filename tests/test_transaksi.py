import unittest
from transaksi.crud import tambah_transaksi, cari_transaksi, filter_tanggal, hapus_transaksi
from transaksi.laporan import buat_rekap

SAMPLE = {"id":"T100","tanggal":"2026-11-01","pelanggan":"Ayu","produk":"Mouse","jumlah":2,"harga":50000}

class TestTransaksi(unittest.TestCase):
    def test_tambah_dan_cari(self):
        data = tambah_transaksi([], SAMPLE)
        self.assertEqual(cari_transaksi(data, "T100")["produk"], "Mouse")

    def test_duplikat_ditolak(self):
        data = tambah_transaksi([], SAMPLE)
        with self.assertRaises(ValueError):
            tambah_transaksi(data, SAMPLE)

    def test_filter_tanggal(self):
        data = tambah_transaksi([], SAMPLE)
        self.assertEqual(len(filter_tanggal(data, "2026-11-01")), 1)

    def test_rekap(self):
        rekap = buat_rekap([SAMPLE])
        self.assertEqual(rekap["total_pendapatan"], 100000)

    def test_hapus(self):
        data = tambah_transaksi([], SAMPLE)
        baru, status = hapus_transaksi(data, "T100")
        self.assertTrue(status)
        self.assertEqual(baru, [])

if __name__ == "__main__":
    unittest.main()
