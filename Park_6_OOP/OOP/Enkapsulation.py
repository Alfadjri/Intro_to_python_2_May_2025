
class Hewan :
    nama_hewan = "default" 
    jenis_hewan = "default"
    _umur_hewan = 10  # ini encapsulation nya 
    
    def __init__(self,nama = None,jenis = None): 
        self.nama_hewan = nama
        self.jenis_hewan = jenis
        
    def makan(self): 
        print("Hewan sedang makan")
    
    #  Set and Get
    # Get itu di gunakan untuk mengambil nilai private
    def get_umur_hewan(self):
        return self._umur_hewan
    # set itu di gunakan untuk mengatur nilai private
    def set_umur_hewan(self,umur):
        self._umur_hewan = umur
        
kucing = Hewan("Tom","Kucing")
print(f"Nama hewan saat ini : {kucing.nama_hewan}")
print(f"Jenis hewan saat ini : {kucing.jenis_hewan}")
kucing.set_umur_hewan(2)
print(f"Umur hewan saat ini : {kucing.get_umur_hewan()}")