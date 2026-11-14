# ==============================================================================
# Berkas: main.py
# Deskripsi: Program utama untuk menguji sistem manajemen perpustakaan
# ==============================================================================
from library_item import Book, Magazine, LibraryItem
from library import Library
from member import Member


def main():
    perpus = Library("Perpustakaan ITERA")

    print("--- 1. Menambahkan Item ---")
    perpus.tambah_item(Book("B001", "Pemrograman Python", "Guido van Rossum", 350))
    perpus.tambah_item(Book("B002", "Basis Data Lanjut", "Siti Rahma", 280))
    perpus.tambah_item(Magazine("M001", "Tech Today", "Edisi 45", "Media Teknologi"))
    perpus.tambah_item(Magazine("M002", "Sains Populer", "Edisi 12", "Ilmu Press"))
    perpus.tambah_item(Book("B001", "Duplikat ID", "Tidak Ada", 10))   # harus ditolak

    print("\n--- 2. Tampilkan Katalog ---")
    perpus.tampilkan_katalog()

    print("\n--- 3. Pencarian ---")
    hasil_id = perpus.cari_berdasarkan_id("M001")
    print("Cari ID 'M001'    :", hasil_id)
    hasil_judul = perpus.cari_berdasarkan_judul("python")
    print("Cari judul 'python':", [str(i) for i in hasil_judul])
    print("Cari ID 'X999'    :", perpus.cari_berdasarkan_id("X999"))

    print("\n--- 4. Peminjaman & Status Ketersediaan ---")
    andi = Member("A01", "Andi")
    budi = Member("A02", "Budi")
    buku = perpus.cari_berdasarkan_id("B001")
    majalah = perpus.cari_berdasarkan_id("M001")

    andi.pinjam_item(buku)
    budi.pinjam_item(buku)        # gagal: sudah dipinjam Andi
    andi.pinjam_item(majalah)
    print("Status buku B001 dipinjam?", buku.is_dipinjam)

    perpus.tampilkan_katalog()    # hanya yang tersedia
    perpus.tampilkan_katalog(hanya_tersedia=False)

    print("\n--- 5. Pengembalian & Denda (Polymorphism) ---")
    andi.kembalikan_item(buku, hari_terlambat=3)       # denda buku
    andi.kembalikan_item(majalah, hari_terlambat=3)    # denda majalah
    perpus.tampilkan_katalog()

    print("\n--- 6. Bukti Encapsulation & Abstract Class ---")
    try:
        buku.is_dipinjam = True
    except AttributeError:
        print("is_dipinjam read-only: tidak bisa diubah langsung (AttributeError)")
    try:
        LibraryItem("X", "Abstrak")
    except TypeError as err:
        print("Abstract class ditolak:", err)

    print("\nTotal item di perpustakaan:", len(perpus))


if __name__ == "__main__":
    main()
