# ===================================================
# Berkas: tugas2_nilai_mahasiswa.py
# Deskripsi: Pengelolaan data nilai mahasiswa
# Nilai Akhir = 30% UTS + 40% UAS + 30% Tugas
# ===================================================

BOBOT_UTS = 0.30
BOBOT_UAS = 0.40
BOBOT_TUGAS = 0.30

data_mahasiswa = [
    {"nama": "Ahmad Fadhilah", "nim": "121140001", "nilai_uts": 85, "nilai_uas": 90, "nilai_tugas": 88},
    {"nama": "Siti Nurhaliza", "nim": "121140002", "nilai_uts": 75, "nilai_uas": 70, "nilai_tugas": 80},
    {"nama": "Budi Santoso", "nim": "121140003", "nilai_uts": 65, "nilai_uas": 60, "nilai_tugas": 70},
    {"nama": "Dewi Lestari", "nim": "121140004", "nilai_uts": 55, "nilai_uas": 50, "nilai_tugas": 60},
    {"nama": "Andi Pratama", "nim": "121140005", "nilai_uts": 40, "nilai_uas": 45, "nilai_tugas": 35},
    {"nama": "Rian Hidayat", "nim": "121140006", "nilai_uts": 78, "nilai_uas": 82, "nilai_tugas": 75},
]


def hitung_nilai_akhir(uts: float, uas: float, tugas: float) -> float:
    """
    Menghitung nilai akhir berbobot.

    Parameter:
        uts   (float): nilai UTS.
        uas   (float): nilai UAS.
        tugas (float): nilai tugas.

    Return:
        float: nilai akhir = 30% UTS + 40% UAS + 30% Tugas.
    """
    return (BOBOT_UTS * uts) + (BOBOT_UAS * uas) + (BOBOT_TUGAS * tugas)


def tentukan_grade(nilai_akhir: float) -> str:
    """
    Menentukan grade huruf dari nilai akhir.

    Parameter:
        nilai_akhir (float): nilai akhir mahasiswa.

    Return:
        str: grade A, B, C, D, atau E.
    """
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"


def proses_data(daftar: list) -> None:
    """
    Menambahkan kunci 'nilai_akhir' dan 'grade' ke setiap dictionary mahasiswa.

    Parameter:
        daftar (list): list of dict data mahasiswa.

    Return:
        None (data diubah langsung).
    """
    for mhs in daftar:
        mhs["nilai_akhir"] = hitung_nilai_akhir(
            mhs["nilai_uts"], mhs["nilai_uas"], mhs["nilai_tugas"]
        )
        mhs["grade"] = tentukan_grade(mhs["nilai_akhir"])


def cetak_tabel(daftar: list) -> None:
    """
    Mencetak data mahasiswa dalam bentuk tabel rapi.

    Parameter:
        daftar (list): list of dict data mahasiswa yang sudah diproses.

    Return:
        None.
    """
    garis = "+" + "-" * 5 + "+" + "-" * 22 + "+" + "-" * 12 + "+" + "-" * 13 + "+" + "-" * 7 + "+"
    print(garis)
    print(f"| {'No':<3} | {'Nama':<20} | {'NIM':<10} | {'Nilai Akhir':>11} | {'Grade':^5} |")
    print(garis)
    for no, mhs in enumerate(daftar, start=1):
        print(
            f"| {no:<3} | {mhs['nama']:<20} | {mhs['nim']:<10} "
            f"| {mhs['nilai_akhir']:>11.2f} | {mhs['grade']:^5} |"
        )
    print(garis)


def cetak_detail(judul: str, mhs: dict) -> None:
    """
    Mencetak informasi lengkap satu mahasiswa.

    Parameter:
        judul (str): judul bagian yang ditampilkan.
        mhs   (dict): data mahasiswa.

    Return:
        None.
    """
    print(f"\n{judul}")
    print(f"  Nama        : {mhs['nama']}")
    print(f"  NIM         : {mhs['nim']}")
    print(f"  Nilai Akhir : {mhs['nilai_akhir']:.2f}")
    print(f"  Grade       : {mhs['grade']}")


def main():
    proses_data(data_mahasiswa)

    print("=== DAFTAR NILAI MAHASISWA ===")
    cetak_tabel(data_mahasiswa)

    tertinggi = max(data_mahasiswa, key=lambda m: m["nilai_akhir"])
    terendah = min(data_mahasiswa, key=lambda m: m["nilai_akhir"])

    cetak_detail(">> Mahasiswa dengan NILAI AKHIR TERTINGGI:", tertinggi)
    cetak_detail(">> Mahasiswa dengan NILAI AKHIR TERENDAH:", terendah)


if __name__ == "__main__":
    main()
