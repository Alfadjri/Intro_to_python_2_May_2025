open_file = open("../Write/Contoh_write_text.txt","r")
read = open_file.read()
print("Value file Contoh_write_text.txt : ")
print(read)

# menulis 3 huruf
open_file.seek(0) #ini adalah teknik untuk merubah pointer atau nomer urut menjadi ke index 0
print("Ambil 3 kaerket di depan dari file Contoh_wirte_text.txt")
print(open_file.readline(3))

#realines 
open_file.seek(0)
print("Ambil 1 bari pertema dari file Contoh_wirte_text.txt :")
for line in open_file.readlines():
    print(line.strip())
    break

open_file.close()


