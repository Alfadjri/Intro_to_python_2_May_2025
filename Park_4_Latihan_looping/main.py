import os
import platform

def clear_terminal():
    os_name = platform.system()
    if(os_name == "Windows"):
        os.system("cls")
    else:
        os.system("clear")
        

def pause(pesan=None):
    if pesan is not None:
        print(pesan)
    print("Tekan apapun untuk melanjutkan program ......")
    input()

def rumus_persegi(header,sisi):
    print(header)
    for i in range(0,sisi + 1):
        for j in range(0,sisi + 1):
            print("*",end=" ")
        print()

def persegi():
    header = "========== Persegi ==========="
    print(header)
    sisi = input("Berapa panjang sisi yang ingin di buat ? => ")
    sisi = int(sisi) # ini belum di validasi (teknik untuk melakukan check pada inputan user)
    clear_terminal()
    rumus_persegi(header,sisi)
    print()
    pause()

def segita_siku_siku_kiri_bawah(header , baris):
    print(header)
    for i in range(1,baris + 1):
        for j in range(i):
            print("*",end=" ")
        print()
    print()
    pause()
    
def segita_siku_siku_kiri_atas(header,baris):
    print(header)
    for i in range(baris,0, -1):
        for j in range(i):
            print("*",end=" ")
        print()
    print()
    pause()

    
def segita_siku_siku_kanan_atas(header , baris):
    print(header)
    for i in range(baris,0,-1):
        for j in range(baris - i):
            print(" ",end=" ")
        for k in range(i):
            print("*",end=" ")
        print()
    print()
    pause()

def segita_siku_siku_kanan_bawah(header , baris):
    print(header)
    for i in range(1,baris+1):
        for j in range(baris - i):
            print(" ",end=" ")
        for k in range(i):
            print("*",end=" ")
        print()
    print()
    pause()
    

def rumus_ganji(nilai):
    if nilai % 2 == 0 : 
        return False
    return True

        
def menu_segitiga():
    header = "========== Segitiga ==========="
    print(header)
    banyak_baris = input("Berapa panjang baris yang ingin di buat ? => ")
    banyak_baris = int(banyak_baris)
    check_nilai = rumus_ganji(banyak_baris)
    if check_nilai == False :
        pause("Nilai harus ganjil")
        return
    clear_terminal()
    print(header)
    print("1.Kiri bawah")
    print("2.Kiri atas")
    print("3.kanan bawah")
    print("4.kanan atas")
    print("q.back")
    select = input("Select => ")
    match select:
        case "1":
            clear_terminal()
            segita_siku_siku_kiri_bawah(header,banyak_baris)
        case "2":
            clear_terminal()
            segita_siku_siku_kiri_atas(header,banyak_baris)
        case "3":
            clear_terminal()
            segita_siku_siku_kanan_bawah(header,banyak_baris)
        case "4":
            clear_terminal()
            segita_siku_siku_kanan_atas(header,banyak_baris)
        case "q":
            return
        case _:
            pause("Tombol yang anda ketikkan tidak sesuai")

def diamon_light(header,baris):
    print(header)
    for i in range(1,baris+1):
        for j in range(baris - i):
            print(" ",end=" ")
        for k in range(2 * i -1):
            print("*",end=" ")
        print()
        
    for i in range(baris-1,0, -1):
        for j in range(baris - i):
            print(" ",end=" ")
        for k in range(2 * i -1):
            print("*",end=" ")
        print()
        
    print()
    pause()

def diamon_dark(header,baris):
    print(header)
    for i in range(1,baris+1):
        for j in range(baris - i + 1):
            print("*",end=" ")
        for k in range(2 * i - 2):
            print(" ",end=" ")
        for l in range(baris - i + 1):
            print("*",end=" ")
        print()
        
    for i in range(baris-1 , 0 , -1):
        for j in range(baris - i + 1):
            print("*",end=" ")
        for k in range(2 * i -2):
            print(" ",end=" ")
        for l in range(baris - i + 1):
            print("*",end=" ")
        print()
        
    print()
    pause()
    
def menu_diamon():
    header = "===========Diamon==========="
    banyak_baris = 5
    print(header)
    print("1.light")
    print("2.dark")
    print("3.Black")
    select = input("Select => ")
    match select:
        case "1":
            clear_terminal()
            diamon_light(header,banyak_baris)
        case "2":
            clear_terminal()
            diamon_dark(header,banyak_baris)
        case _:
            pause("Tombol yang anda ketikkan tidak sesuai")

def fibonaci():
    header = "===========Fibonaci==========="
    data = int(input("Masukan jumlah fibonaci yang akan di print : "))
    if data <= 0 :
        pause("Masikan akan lebih dari 0")
        clear_terminal()
        fibonaci() #rekusif teknik 
    data += 1
    
    nilai_awal = [0,1]
    for i in range(2,data):
        next_bilangan = nilai_awal[-1] + nilai_awal[-2]
        nilai_awal.append(next_bilangan)
    print()
    print(f"Deret Bilangan fibonaci : {nilai_awal}")
    pause()
    
def main():
    while True:
        clear_terminal()
        print("========Menu utama============")
        print("1.Persegi")
        print("2.Segitiga siku-siku")
        print("3.Diamon")
        print("5.Fibonaci")
        print("q.exit")
        select = input("Select => ")
        match select :
            case "1" :
                clear_terminal()
                persegi()
            case "2":
                clear_terminal()
                menu_segitiga()
            case "3":
                clear_terminal()
                menu_diamon()
            case "5":
                clear_terminal()
                fibonaci()
            case "q":
                break
            case _ :
                pause("Tombol yang anda ketikkan tidak sesuai")

if __name__ == "__main__":
    main()