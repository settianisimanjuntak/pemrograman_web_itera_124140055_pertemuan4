# ===================================================
# Berkas: tugas1_bmi.py
# Deskripsi: Program penghitung BMI (Body Mass Index) sederhana
# ===================================================


def hitung_bmi(berat: float, tinggi: float) -> float:
    """
    Menghitung nilai BMI.

    Parameter:
        berat  (float): berat badan dalam kilogram (kg).
        tinggi (float): tinggi badan dalam meter (m).

    Return:
        float: nilai BMI = berat / (tinggi * tinggi).
    """
    return berat / (tinggi * tinggi)


def tentukan_kategori(bmi: float) -> str:
    """
    Menentukan kategori berat badan berdasarkan nilai BMI.

    Parameter:
        bmi (float): nilai BMI.

    Return:
        str: kategori berat badan.
    """
    if bmi < 18.5:
        return "Berat badan kurang"
    elif bmi < 25:
        return "Berat badan normal"
    elif bmi < 30:
        return "Berat badan berlebih"
    else:
        return "Obesitas"


def minta_angka_positif(pesan: str) -> float:
    """
    Meminta input angka positif dari pengguna sampai valid.

    Parameter:
        pesan (str): teks prompt yang ditampilkan.

    Return:
        float: angka positif yang dimasukkan pengguna.
    """
    while True:
        try:
            nilai = float(input(pesan).replace(",", "."))
            if nilai > 0:
                return nilai
            print("Input harus lebih dari 0, coba lagi.")
        except ValueError:
            print("Input tidak valid, masukkan angka (contoh: 65.5).")


def main():
    print("=== PROGRAM PENGHITUNG BMI ===")
    berat = minta_angka_positif("Masukkan berat badan (kg)  : ")
    tinggi = minta_angka_positif("Masukkan tinggi badan (m)  : ")

    bmi = hitung_bmi(berat, tinggi)
    kategori = tentukan_kategori(bmi)

    print("\n--- HASIL PERHITUNGAN ---")
    print(f"Berat badan : {berat:.2f} kg")
    print(f"Tinggi badan: {tinggi:.2f} m")
    print(f"Nilai BMI   : {bmi:.2f}")
    print(f"Kategori    : {kategori}")


if __name__ == "__main__":
    main()
