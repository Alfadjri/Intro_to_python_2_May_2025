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
        

def memanggil(Ibu): #polymophisme di makan kamu tau nama funciton nya gak tau kelasnya 
    Ibu.memanggil()

anak = Anak()
ibu = Ibu()


memanggil(anak)