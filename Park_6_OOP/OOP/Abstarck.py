from abc import ABC, abstractclassmethod

class Kendaraan(ABC): # abstrak kelas jika bentuk nya belum jelas atau kalau c namapnya chp
    @abstractclassmethod
    def menyalakan(self):
        pass
    

class Mobil(Kendaraan):
    def menyalakan(self):
        return "Start"


class Motor(Kendaraan):
    def menyalakan(self):
        return "Motor mogok"
    
    
# kendaraan = Kendaraan()
# print(kendaraan.menyalakan())

motor= Motor()
print(motor.menyalakan())