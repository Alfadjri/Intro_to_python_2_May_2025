# kasus ibu dan anak
class Ibu : 
    panggilan = "ini punya ibu"
    
    def memanggil (self):
        print("Iya , ada apa ?")
        
    def setSifat(self,sifat):
        self._sifat_ibu = sifat
    
    def getSifat(self):
        return self._sifat_ibu
    

class Anak(Ibu): #inheritance atau pewarisan sifat dari Ibu
    def memanggil (self): 
        print("Nanti dulu lagi main !!!!")


# Coba memanggil 
anak = Anak()
anak.panggilan = "budi"
anak.setSifat("Nakal")
print(f"Nama anak ini : {anak.panggilan}")
print(f"Sifat anak ini : {anak.getSifat()}")
anak.memanggil()

ibu = Ibu()
print(f"Nama ibu ini : {ibu.panggilan}")
ibu.memanggil()