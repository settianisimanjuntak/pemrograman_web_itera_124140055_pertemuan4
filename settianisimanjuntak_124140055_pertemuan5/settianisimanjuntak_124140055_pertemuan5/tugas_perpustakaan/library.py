# ==============================================================================
# Berkas: library.py
# Deskripsi: Class Library untuk mengelola koleksi item perpustakaan
# ==============================================================================
from library_item import LibraryItem


class Library:
    """Mengelola koleksi LibraryItem. Koleksi disimpan di atribut private."""

    def __init__(self, nama: str):
        self.nama = nama
        self.__koleksi = []   # PRIVATE: hanya bisa diubah lewat method class ini

    def tambah_item(self, item: LibraryItem) -> bool:
        """Menambahkan item ke koleksi. Ditolak jika ID sudah ada."""
        if not isinstance(item, LibraryItem):
            print("Gagal: objek bukan LibraryItem.")
            return False
        if self.cari_berdasarkan_id(item.item_id) is not None:
            print(f"Gagal: ID '{item.item_id}' sudah terdaftar.")
            return False
        self.__koleksi.append(item)
        print(f"Item ditambahkan: {item.judul}")
        return True

    def tampilkan_katalog(self, hanya_tersedia: bool = True):
        """Menampilkan daftar item. Default hanya yang tersedia."""
        judul = "ITEM TERSEDIA" if hanya_tersedia else "SEMUA ITEM"
        print(f"\n=== KATALOG {judul} - {self.nama} ===")
        ditampilkan = 0
        for item in self.__koleksi:
            if hanya_tersedia and item.is_dipinjam:
                continue
            print(" -", item.get_detail())   # POLYMORPHISM
            ditampilkan += 1
        if ditampilkan == 0:
            print(" (tidak ada item)")

    def cari_berdasarkan_id(self, item_id: str):
        """Mencari item berdasarkan ID. Return None jika tidak ketemu."""
        for item in self.__koleksi:
            if item.item_id == item_id:
                return item
        return None

    def cari_berdasarkan_judul(self, kata_kunci: str) -> list:
        """Mencari item yang judulnya mengandung kata kunci (tidak case-sensitive)."""
        kata = kata_kunci.lower()
        return [item for item in self.__koleksi if kata in item.judul.lower()]

    def __len__(self) -> int:
        return len(self.__koleksi)
