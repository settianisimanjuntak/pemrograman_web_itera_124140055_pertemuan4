# ===================================================
# Berkas: main.py
# Deskripsi: Program utama yang menggunakan modul math_operations
# Cara impor 1: import math_operations (alias: mo)
# Cara impor 2: from math_operations import ... (fungsi & konstanta)
# ===================================================

import math_operations as mo
from math_operations import (
    PI,
    luas_lingkaran,
    keliling_lingkaran,
    celsius_ke_fahrenheit,
    celsius_ke_kelvin,
)


def judul(teks: str) -> None:
    """Mencetak judul bagian dengan garis pembatas."""
    print(f"\n{'=' * 44}\n{teks.center(44)}\n{'=' * 44}")


def main():
    print(f"Konstanta PI dari modul: {PI}")

    judul("PERSEGI")
    for sisi in (4, 7.5, 10):
        print(f"Sisi {sisi:>5} -> Luas: {mo.luas_persegi(sisi):>8.2f} | "
              f"Keliling: {mo.keliling_persegi(sisi):>7.2f}")

    judul("PERSEGI PANJANG")
    for p, l in ((5, 3), (10, 4.5), (12, 8)):
        print(f"{p:>4} x {l:<4} -> Luas: {mo.luas_persegi_panjang(p, l):>8.2f} | "
              f"Keliling: {mo.keliling_persegi_panjang(p, l):>7.2f}")

    judul("LINGKARAN")
    for r in (3, 7, 10.5):
        print(f"r = {r:>5} -> Luas: {luas_lingkaran(r):>8.2f} | "
              f"Keliling: {keliling_lingkaran(r):>7.2f}")

    judul("KONVERSI SUHU")
    for c in (-10, 0, 37, 100):
        print(f"{c:>5} C -> {celsius_ke_fahrenheit(c):>7.2f} F | "
              f"{celsius_ke_kelvin(c):>7.2f} K")


if __name__ == "__main__":
    main()
