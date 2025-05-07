# misal
# data makanan
makanan = ["nasi","ikan","ayam"]

#Read
print(f"isi Data list : {makanan}")
#Read spesifik
print(f"isi dari index ke 2 : {makanan[2]}")
print(f"isi dari index ke -1 : {makanan[-3]}")

# append add
makanan.append("sayur")
print(f"isi Data list add sayur : {makanan}")

# update value
makanan[1] = "Buah"
print(f"isi Data list update ikan jadi buah : {makanan}")

try : # ini di gunakan kalau perkiraan kamu code akan rusak dan di paksa untuk mengeluarkan pesan yang tidak spesifik
    data_yang_mau_di_hilangkan = "Buah"
    for makan in makanan:
        if data_yang_mau_di_hilangkan == makan :
            print("data di temukan")
            makanan.remove(data_yang_mau_di_hilangkan) # ini untuk menghapus nilai
    print(f"isi Data list delete buah: {makanan}")
except:
    print("Data tidak di temukan")

# Menggabungkan nilai
buah = ["Pisang","semangka"]
makanan += buah # makanan = makanan + buah
print(f"isi Data ditambah dengan list buah: {makanan}")