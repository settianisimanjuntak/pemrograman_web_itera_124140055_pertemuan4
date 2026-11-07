# ===================================================
# Berkas: math_operations.py
# Deskripsi: Modul operasi matematika (geometri & konversi suhu)
# ===================================================

PI = 3.14159


# ---------- Geometri: Persegi ----------
def luas_persegi(sisi: float) -> float:
    """
    Menghitung luas persegi.

    Parameter:
        sisi (float): panjang sisi.

    Return:
        float: luas = sisi * sisi.
    """
    return sisi * sisi


def keliling_persegi(sisi: float) -> float:
    """
    Menghitung keliling persegi.

    Parameter:
        sisi (float): panjang sisi.

    Return:
        float: keliling = 4 * sisi.
    """
    return 4 * sisi


# ---------- Geometri: Persegi Panjang ----------
def luas_persegi_panjang(panjang: float, lebar: float) -> float:
    """
    Menghitung luas persegi panjang.

    Parameter:
        panjang (float): panjang.
        lebar   (float): lebar.

    Return:
        float: luas = panjang * lebar.
    """
    return panjang * lebar


def keliling_persegi_panjang(panjang: float, lebar: float) -> float:
    """
    Menghitung keliling persegi panjang.

    Parameter:
        panjang (float): panjang.
        lebar   (float): lebar.

    Return:
        float: keliling = 2 * (panjang + lebar).
    """
    return 2 * (panjang + lebar)


# ---------- Geometri: Lingkaran ----------
def luas_lingkaran(jari_jari: float) -> float:
    """
    Menghitung luas lingkaran.

    Parameter:
        jari_jari (float): jari-jari lingkaran.

    Return:
        float: luas = PI * r^2.
    """
    return PI * jari_jari ** 2


def keliling_lingkaran(jari_jari: float) -> float:
    """
    Menghitung keliling lingkaran.

    Parameter:
        jari_jari (float): jari-jari lingkaran.

    Return:
        float: keliling = 2 * PI * r.
    """
    return 2 * PI * jari_jari


# ---------- Konversi Suhu ----------
def celsius_ke_fahrenheit(celsius: float) -> float:
    """
    Mengonversi suhu Celsius ke Fahrenheit.

    Parameter:
        celsius (float): suhu dalam Celsius.

    Return:
        float: suhu dalam Fahrenheit (F = C * 9/5 + 32).
    """
    return celsius * 9 / 5 + 32


def celsius_ke_kelvin(celsius: float) -> float:
    """
    Mengonversi suhu Celsius ke Kelvin.

    Parameter:
        celsius (float): suhu dalam Celsius.

    Return:
        float: suhu dalam Kelvin (K = C + 273.15).
    """
    return celsius + 273.15


if __name__ == "__main__":
    print("[TEST MODUL] luas_persegi(4) =", luas_persegi(4))
    print("[TEST MODUL] celsius_ke_kelvin(0) =", celsius_ke_kelvin(0))
