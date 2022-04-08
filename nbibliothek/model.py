class BooksDTO:
    def __init__(self, judul, pengarang, penerbit, no_klasifikasi, no_barcode, jumlah_eksemplar):
        self.__judul = judul
        self.__pengarang = pengarang
        self.__penerbit = penerbit
        self.__no_klasifikasi = no_klasifikasi
        self.__no_barcode = no_barcode
        self.__jumlah_eksemplar = jumlah_eksemplar

    @property
    def judul(self):
        return self.__judul

    @property
    def pengarang(self):
        return self.__pengarang

    @property
    def penerbit(self):
        return self.__penerbit

    @property
    def no_klasifikasi(self):
        return self.__no_klasifikasi

    @property
    def no_barcode(self):
        return self.__no_barcode

    @property
    def jumlah_eksemplar(self):
        return self.__jumlah_eksemplar


class AnggotaDTO:
    def __init__(self, nim, nama, tanggal_kembali):
        self.__nomor_induk_mahasiswa = nim
        self.__nama = nama
        self.__tanggal_kembali = tanggal_kembali

    @property
    def nim(self):
        return self.__nomor_induk_mahasiswa

    @property
    def nama(self):
        return self.__nama

    @property
    def tanggal_kembali(self):
        return self.__tanggal_kembali


class PeminjamanDTO:
    def __init__(self, nim, peminjaman1, peminjaman2, peminjaman3):
        self.__nomor_induk_mahasiswa = nim
        self.__peminjaman1 = peminjaman1
        self.__peminjaman2 = peminjaman2
        self.__peminjaman3 = peminjaman3

    @property
    def nim(self):
        return self.__nomor_induk_mahasiswa

    @property
    def peminjaman1(self):
        return self.__peminjaman1

    @property
    def peminjaman2(self):
        return self.__peminjaman2

    @property
    def peminjaman3(self):
        return self.__peminjaman3
