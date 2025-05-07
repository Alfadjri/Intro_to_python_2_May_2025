# format
# def nama_function(paramter):
#   apa yang akan kamu olah atau munculkan 

# keterangan
# def(definisi) atau code untuk function
# nama_function ini yang jadi icon atau yang akan di panggil nntinya
# paramter adalah syarat yang akan di terpakan saat memanggil nama_function


#function void 
#void adalah function yang sifatnya mati atau tidak ada pengelolahan lagi 
# def kata_sambutan(nama_user):
#     print(f"Hello {nama_user}\nPekernalakan nama saya Veronika")
#     print("Veronika adalah chat bot asissten dari Telkomsel")
#     print("Ada yang bisa di bantu oleh Veronika ? ")
    

# nama_user = input("Silahkan masukan nama anda :")
# kata_sambutan(nama_user)


# non void 
def menentukan_nilai_diskon(harga_awal,harga_akhir): # ini function nya 
    total_potongan = harga_awal - harga_akhir
    diskon = (total_potongan / harga_awal) * 100
    return int(diskon)

harga_awal = 5000000
harga_akhir= 4850000
diskon = menentukan_nilai_diskon(harga_awal,harga_akhir) # ini cara pangglinya
diskon = str(diskon) + "%"
print(diskon)
    