from personal import Person

class Employee(Person):
    def __init__(self, nama, umur,pekerjaan,gaji):
        super().__init__(nama, umur)
        self._pekerjaan = pekerjaan
        self._gaji = gaji
        
    def get_detail(self):
        return f"Employee : {self._name}\nAge : {self.getUmur()}\nPekerjaan : {self._pekerjaan}\nGaji : {self._gaji}"
    def work(self):
        return f"{self._name} dia bekerja sebagai {self._pekerjaan}"