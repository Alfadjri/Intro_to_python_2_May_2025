siswa = {
    "kelas" : 12,
    "jurusan" : ["ipa","ips"], #java programming arry 2d 
    "nama_ketua_kelas" : "Budi",
    "Guru" :[
        {
            "id" : 2,
            "nama" : "siska",
        },
        {
            "id" : 3,
            "nama" : "Toni",
        },
        {
            "id" : 4,
            "nama" : {
                "nama_singkatan" : "Tong",
                "nama_lengkap" : "Tong mauli",
                "gelar" : ["S.pd","s.kom","CEH","CPEN"]
            }
        }
    ]

}

#read
print(f"Data metah : {siswa}")

# read spesifik
print(f"Kelas : {siswa["kelas"]}")
print(f"Jurusan siswa : {siswa["jurusan"][1]}")
# print(f"Guru yang mengjar : {siswa["Guru"]["nama"]}")
nama_lengkap = siswa["Guru"][2]["nama"]["nama_lengkap"]
gelar = siswa["Guru"][2]["nama"]["gelar"]
print(f"Guru pengganti yang mengjar : {nama_lengkap} {gelar}")