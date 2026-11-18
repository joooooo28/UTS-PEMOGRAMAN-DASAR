import csv
import json
from pathlib import Path
from .crud import validasi_transaksi

COLUMNS = ["id", "tanggal", "pelanggan", "produk", "jumlah", "harga"]

def baca_csv(path):
    """Membaca CSV dan memvalidasi setiap baris; mengembalikan list dictionary."""
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"File tidak ditemukan: {path}")
    hasil = []
    with file_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames is None or not set(COLUMNS).issubset(reader.fieldnames):
            raise ValueError("Header CSV tidak sesuai format transaksi.")
        ids = set()
        for nomor, row in enumerate(reader, start=2):
            try:
                row["jumlah"] = int(row["jumlah"])
                row["harga"] = int(row["harga"])
                validasi_transaksi(row)
                if row["id"] in ids:
                    raise ValueError("ID duplikat.")
                ids.add(row["id"])
                hasil.append(row)
            except (ValueError, TypeError) as error:
                raise ValueError(f"Data tidak valid pada baris {nomor}: {error}") from error
    return hasil

def simpan_csv(path, data):
    """Menyimpan list transaksi ke CSV; mengembalikan path keluaran."""
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(data)
    return str(file_path)

def simpan_json(path, data):
    """Menyimpan data rekap ke JSON; mengembalikan path keluaran."""
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    return str(file_path)
