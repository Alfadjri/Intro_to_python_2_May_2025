from abc import ABC , abstractclassmethod
class Person :
    def __init__(self,nama,umur):
        self._name = nama
        self.__umur = umur
    
    @abstractclassmethod
    def get_detail(self):
        pass
    
    def getUmur(self):
        return self.__umur
    
    def setUmur(self,umur):
        if umur > 0:
            self.__umur = umur
        else:
            return ValueError("umur harus bernilai positif")