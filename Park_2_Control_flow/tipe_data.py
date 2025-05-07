#int
#int (Integer) adalah bilangan bulat (0,1,2,3,4,5)
x = 32767
print("Contoh Tipe data Integer(int) : {0}".format(x))
#float atau bouble
# contoh float di tandai dengan f  : 3.14f
f = 10.5
print("Contoh Tipe data desimal(float) : {0}".format(f))
#kompleks
z = 2 + 3j
print("Contoh Tipe data desimal(kompleks) : {0}".format(z))


#sqyence type
a = [1,2,3,4] # list : sifat tipe data kalau bisa harus sama
print("Contoh Tipe data list : {0}".format(a))
b = (1,2,3,4) # truplet : sifat tipe data nya tidak bisa di ubah
# b[0] = 10
print("Contoh Tipe data truplet : {0}".format(b))
c = range(1,5)
print("Contoh Tipe data truplet : {0}".format(c))


#teks
#String
nama_lengkap = "Alfadjri Dwi Fadhilah"
print("Contoh Tipe data string : {0}".format(nama_lengkap))

#maping
#dic
profile = { "nama" : "alfadjri dwi Fadhilah" ,"age" : 24}
print("Contoh Tipe data dic : {age}".format( age = profile["age"]))

#set
f = {1,2,3}
print("Contoh Tipe data set : {0}".format(f))
g = frozenset({4,5,6})
print("Contoh Tipe data frozenset : {0}".format(g))

# boolean
# booealn ini nilainya hanya ada 2 : True(1) atau False(0)
kondisi = 1
kondisi_tampa_simbolik = False 
# bool itu di gunakan untuk merubah tipe data atau sebutanya casting atau conversi ke bilangan boolean
print("Contoh Tipe data boolean simbolik (1) : {0}".format(bool(kondisi)))


# binary type
i = 0b01000001
# desimal = int(i) # 64
# karakter = chr(desimal) # A
print(chr(int(i)))
j = bytearray(a)
print(j)
k = memoryview(j)
print(k)