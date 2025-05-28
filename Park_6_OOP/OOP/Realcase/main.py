from employee import Employee
from manager import Manager


def main():
    listEmploye = [
        {
            "nama" : "Tika",
            "umur" : 24,
            "pekerjaan" : "Grafik Desing",
            "gaji" : 300000
        },
        {
            "nama" : "Toni",
            "umur" : 24,
            "pekerjaan" : "Grafik Desing",
            "gaji" : 300000
        },
    ]
    
    for value in listEmploye:
        employee = Employee(value['nama'],value["umur"],value["pekerjaan"],value['gaji'])
        print("=========Employe===========")
        print(employee.get_detail())
        print(employee.work())

    print()
    
    print("=========Manager===========")
    manager = Manager("Budi",40,"Grafik Desing","8000000",10)
    print(manager.get_detail())
    print(manager.work())

if __name__ == "__main__":
    main()