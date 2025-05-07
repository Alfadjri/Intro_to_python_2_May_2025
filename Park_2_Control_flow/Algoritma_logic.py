#case input nilai siswa 


print("===========if==========")
nilai = 70 
# kkm (Kriteria Ketuntasan Minimal)
# 40
if nilai > 40 : 
    print("Kamu lulus ujian ini !!!")
    
    
print("==========else if==========")
nilai = 100
# kkm (Kriteria Ketuntasan Minimal)
# 80
if nilai > 80 and nilai < 90: 
    print("Kamu lulus ujian ini !!!")
else :
    print("Kamu tidak lulus")

print("==========if elif else ==========")
nilai = 80
# kkm (Kriteria Ketuntasan Minimal)
# A = 100
# B = 90
# C = 80 (KKM)
# D = 70
if nilai > 90 :
    print("Nilai kamu sempurna")
elif nilai > 80 and nilai <= 90 :
    print("Nilai kamu lulus")
elif nilai > 70 and nilai <= 80:
    # ini contoh penggunaan dari if else (bersarang)
    if nilai >= 70 : #tidak baik 
        if nilai >= 75:
            print("nilai di bawah standar kelulusan")
    else :
        print("Nilai kamu lulus kkm")
else :
    print("Kamu tidak lulus")
# Tips dalam programming jangan mikiri yang benar kalau syaratnya banyak


#Swith case
print("=============== Swich Case =========")
print("=============== Selamat datang =========")
print("1. Start")
print("2. End")
selection = input("Select Menu : ")
match selection:
    case "1":
        print("Staring")
    case "2":
        print("Selamat tinggal")
    case _ :
        print("inputan tidak valid silahkan pilih 1 atau 2 saja yang di input !")
