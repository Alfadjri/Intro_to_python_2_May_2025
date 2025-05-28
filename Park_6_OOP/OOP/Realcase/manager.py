from employee import Employee

class Manager(Employee):
    def __init__(self, nama, umur,pekerjaan,gaji,jumlah_tim):
        super().__init__(nama, umur,pekerjaan,gaji)
        self._jumlah_tim = jumlah_tim
    def get_detail(self):
        return f"Manager : {self._name}\nAge : {self.getUmur()}\nPekerjaan : {self._pekerjaan}\nGaji : {self._gaji}\nJumlah Tim : {self._jumlah_tim}"
    def work(self):
        return f"{self._name} dia bekerja sebagai Manager {self._pekerjaan} dengan jumlah tim {self._jumlah_tim}"