# ==============================================================================
# Berkas: library_item.py
# Deskripsi: Abstract class LibraryItem beserta subclass Book dan Magazine
# ==============================================================================
from abc import ABC, abstractmethod


class LibraryItem(ABC):
    """Abstract base class untuk seluruh item perpustakaan.

    Atribut:
        _item_id (protected)  : ID unik item.
        _judul   (protected)  : Judul item (diakses lewat property `judul`).
        __dipinjam (private)  : Status peminjaman, dilindungi name mangling.
    """

    def __init__(self, item_id: str, judul: str):
        self._item_id = item_id
        self._judul = None
        self.judul = judul          # lewat setter agar tervalidasi
        self.__dipinjam = False     # PRIVATE: tidak boleh diubah langsung dari luar

    # --------------------------- PROPERTY ---------------------------
    @property
    def item_id(self) -> str:
        """Getter ID item (read-only)."""
        return self._item_id

    @property
    def judul(self) -> str:
        """Getter judul item."""
        return self._judul

    @judul.setter
    def judul(self, nilai: str):
        """Setter judul dengan validasi: tidak boleh kosong."""
        if not isinstance(nilai, str) or not nilai.strip():
            raise ValueError("Judul tidak boleh kosong!")
        self._judul = nilai.strip()

    @property
    def is_dipinjam(self) -> bool:
        """Getter status peminjaman (read-only dari luar class)."""
        return self.__dipinjam

    # ------------------------ METHOD KONKRIT ------------------------
    def pinjam(self) -> bool:
        """Mengubah status item menjadi dipinjam. Return False jika sudah dipinjam."""
        if self.__dipinjam:
            return False
        self.__dipinjam = True
        return True

    def kembalikan(self) -> bool:
        """Mengubah status item menjadi tersedia. Return False jika memang tidak dipinjam."""
        if not self.__dipinjam:
            return False
        self.__dipinjam = False
        return True

    def __str__(self) -> str:
        status = "Dipinjam" if self.__dipinjam else "Tersedia"
        return f"[{self._item_id}] {self._judul} ({status})"

    # ------------------------ METHOD ABSTRACT -----------------------
    @abstractmethod
    def get_detail(self) -> str:
        """Mengembalikan detail lengkap item (wajib di-override subclass)."""
        pass

    @abstractmethod
    def hitung_denda(self, hari_terlambat: int) -> float:
        """Menghitung denda keterlambatan (wajib di-override subclass)."""
        pass


class Book(LibraryItem):
    """Buku: denda Rp 2.000 per hari keterlambatan."""
    DENDA_PER_HARI = 2000

    def __init__(self, item_id: str, judul: str, penulis: str, jumlah_halaman: int):
        super().__init__(item_id, judul)
        self.penulis = penulis
        self.jumlah_halaman = jumlah_halaman

    def get_detail(self) -> str:
        status = "Dipinjam" if self.is_dipinjam else "Tersedia"
        return (f"[BUKU] ID: {self.item_id} | Judul: {self.judul} | Penulis: {self.penulis} "
                f"| {self.jumlah_halaman} halaman | Status: {status}")

    def hitung_denda(self, hari_terlambat: int) -> float:
        return max(0, hari_terlambat) * self.DENDA_PER_HARI


class Magazine(LibraryItem):
    """Majalah: denda Rp 1.000 per hari keterlambatan."""
    DENDA_PER_HARI = 1000

    def __init__(self, item_id: str, judul: str, edisi: str, penerbit: str):
        super().__init__(item_id, judul)
        self.edisi = edisi
        self.penerbit = penerbit

    def get_detail(self) -> str:
        status = "Dipinjam" if self.is_dipinjam else "Tersedia"
        return (f"[MAJALAH] ID: {self.item_id} | Judul: {self.judul} | Edisi: {self.edisi} "
                f"| Penerbit: {self.penerbit} | Status: {status}")

    def hitung_denda(self, hari_terlambat: int) -> float:
        return max(0, hari_terlambat) * self.DENDA_PER_HARI
