# ==============================================================================
# Berkas: member.py
# Deskripsi: Class Member (anggota perpustakaan) dengan encapsulation
# ==============================================================================
from library_item import LibraryItem


class Member:
    """Anggota perpustakaan yang dapat meminjam item."""
    MAKS_PINJAM = 3

    def __init__(self, member_id: str, nama: str):
        self._member_id = member_id
        self._nama = nama
        self.__daftar_pinjam = []   # PRIVATE: daftar item yang sedang dipinjam

    @property
    def member_id(self) -> str:
        return self._member_id

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def daftar_pinjam(self) -> list:
        """Mengembalikan salinan list agar data asli tidak bisa diubah dari luar."""
        return list(self.__daftar_pinjam)

    def pinjam_item(self, item: LibraryItem) -> bool:
        """Meminjam item jika kuota belum penuh dan item tersedia."""
        if len(self.__daftar_pinjam) >= self.MAKS_PINJAM:
            print(f"Gagal: {self._nama} sudah mencapai batas {self.MAKS_PINJAM} pinjaman.")
            return False
        if not item.pinjam():
            print(f"Gagal: '{item.judul}' sedang dipinjam.")
            return False
        self.__daftar_pinjam.append(item)
        print(f"Sukses: {self._nama} meminjam '{item.judul}'.")
        return True

    def kembalikan_item(self, item: LibraryItem, hari_terlambat: int = 0) -> float:
        """Mengembalikan item dan mengembalikan nilai denda (0 jika tepat waktu)."""
        if item not in self.__daftar_pinjam:
            print(f"Gagal: {self._nama} tidak meminjam '{item.judul}'.")
            return 0.0
        self.__daftar_pinjam.remove(item)
        item.kembalikan()
        denda = item.hitung_denda(hari_terlambat)   # POLYMORPHISM
        print(f"Sukses: {self._nama} mengembalikan '{item.judul}'. Denda: Rp {denda:,.0f}")
        return denda

    def __str__(self) -> str:
        return f"Member[{self._member_id}] {self._nama} - {len(self.__daftar_pinjam)} pinjaman aktif"
