class stok_mobil:
    def __init__(self, ID_mobil, Model, Warna, Jumlah_Unit):
        self.ID_mobil = ID_mobil
        self.Model = Model
        self.Warna = Warna
        self.Jumlah_Unit = Jumlah_Unit

    def detail(self):
        print(f"ID Mobil     : {self.ID_mobil}")
        print(f"Model        : {self.Model}")
        print(f"Warna        : {self.Warna}")
        print(f"Jumlah Unit  : {self.Jumlah_Unit}")
        print("-" * 30)

class karyawan:
    def __init__(self, ID_Karyawan, Nama, Tgl_Lahir, Jenis_Kelamin):
        self.ID_Karyawan = ID_Karyawan
        self.Nama = Nama
        self.Tgl_Lahir = Tgl_Lahir
        self.Jenis_Kelamin = Jenis_Kelamin

    def detail(self):
        print(f"ID Karyawan   : {self.ID_Karyawan}")
        print(f"Nama          : {self.Nama}")
        print(f"Tanggal Lahir : {self.Tgl_Lahir}")
        print(f"Jenis Kelamin : {self.Jenis_Kelamin}")
        print("-" * 30)

class pelanggan:
    def __init__(self, ID_Pelanggan, Nama_Pelanggan, Tgl_Lahir):
        self.ID_Pelanggan = ID_Pelanggan
        self.Nama_Pelanggan = Nama_Pelanggan
        self.Tgl_Lahir = Tgl_Lahir

    def detail(self):
        print(f"ID Pelanggan   : {self.ID_Pelanggan}")
        print(f"Nama Pelanggan : {self.Nama_Pelanggan}")
        print(f"Tanggal Lahir  : {self.Tgl_Lahir}")
        print("-" * 30)

class Showroom:
    def __init__(self):
        self.stok_mobil_list = [
            stok_mobil("M001", "Toyota Avanza", "Putih", 10),
            stok_mobil("M002", "Honda Civic", "Hitam", 5)
        ]
        
        self.karyawan_list = [
            karyawan("K001", "Andi", "1990-01-01", "Laki-laki"),
            karyawan("K002", "Budi", "1985-03-22", "Laki-laki")
        ]
        
        self.pelanggan_list = [
            pelanggan("P001", "Citra", "1995-05-12"),
            pelanggan("P002", "Dewi", "1992-08-30")
        ]

    def daftarStokMobil(self):
        print("\n=== Daftar Stok Mobil ===")
        for mobil in self.stok_mobil_list:
            mobil.detail()

    def daftarKaryawan(self):
        print("\n=== Daftar Karyawan ===")
        for k in self.karyawan_list:
            k.detail()

    def daftarPelanggan(self):
        print("\n=== Daftar Pelanggan ===")
        for p in self.pelanggan_list:
            p.detail()
        
    def tambahKaryawan(self):
        print("\n=== Tambah Karyawan Baru ===")
        ID_Karyawan = input("Masukkan ID Karyawan      : ")
        Nama = input("Masukkan Nama Karyawan           : ")
        Tgl_Lahir = input("Masukkan Tanggal Lahir      : ")
        Jenis_Kelamin = input("Masukkan Jenis Kelamin  : ")
        
        new_karyawan = karyawan(ID_Karyawan, Nama, Tgl_Lahir, Jenis_Kelamin)
        self.karyawan_list.append(new_karyawan)
        print("\nKaryawan berhasil ditambahkan!")
        print("-" * 30)

    def tambahStokMobil(self):
        print("\n=== Tambah Stok Mobil ---")
        ID_mobil = input("Masukkan ID Mobil            : ")
        Model = input("Masukkan Model Mobil            : ")
        Warna = input("Masukkan Warna Mobil            : ")
        Jumlah_Unit = int(input("Masukkan Jumlah Unit  : "))

        new_mobil = stok_mobil(ID_mobil, Model, Warna, Jumlah_Unit)
        self.stok_mobil_list.append(new_mobil)
        print("\nStok Mobil berhasil ditambahkan!")
        print("-" * 30)
