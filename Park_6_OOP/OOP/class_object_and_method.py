# kasus Hewan

class Hewan : # ini di sebut nama kelas
    nama_hewan = "default" # nama_hewan ini di sebut object dengan propery public
    # propery public makasudnya sifat dari object yang kita inisialasisai 
    # public itu sifatnya bisa di ubah" oleh orglain di luar kelas yang ada
    jenis_hewan = "default"
    _umur_hewan = 10 # umur_hewan ini di sebut object dengan propery private
    #private itu sifatnya tidak bisa di ganti sembarangan dari luar kelas tapi boleh di ganti nilainya
    
    def __init__(self,nama = None,jenis = None): #construktor
        self.nama_hewan = nama
        self.jenis_hewan = jenis
    
    
    def makan(self): # ini di sebut metode atau function 
        print("Hewan sedang makan")
        
# Cara memanggil
# object atau variabel = namaClass
kucing = Hewan()
print(f"Nama hewan saat ini : {kucing.nama_hewan}")
print(f"Jenis hewan saat ini : {kucing.jenis_hewan}")
# print(f"Umur hewan saat ini : {kucing.umur_hewan}") # ini error 'Hewan' object has no attribute 'umur_hewan' 
# alasan karna umur_hewan sifatnya private
#  ganti nama hewan 
kucing.nama_hewan = "Tom"
print(f"Nama hewan setelah di ganti : {kucing.nama_hewan}")
# panggil method
kucing.makan()

print("====== Penggunaan Contstruktor =====")
#  Menggunakan Construktor
spike = Hewan("Spike","anjing")
print(f"Nama hewan saat ini : {spike.nama_hewan}")
print(f"Jenis hewan saat ini : {spike.jenis_hewan}")




    