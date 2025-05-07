a = 2
b = 2

hasil = (a > b) #ke akuratan nilai 
print(f"Apakah nilai dari {a} besar dari {b} adalah {hasil}")
hasil = (a >= b)
print(f"Apakah nilai dari {a} besar sama dengan dari {b} adalah {hasil}")
hasil = (a < b) 
print(f"Apakah nilai dari {a} kecil dari {b} adalah {hasil}")
hasil = (a <= b)
print(f"Apakah nilai dari {a} kecil sama dengan dari {b} adalah {hasil}")
a = 2
b = "2" # tipe data nya berbeda
hasil = (a == b) #=== ini yang memabandingkan dengan tipe data yang akurat
print(f"Apakah nilai dari {a} sama dengan dari {b} adalah {hasil}")

kondisi = False
hasil = ( kondisi != True) # Tidak (!) sama (=) apa pun yang ada tanda ! nilainya di tukar
print(f"Apa nilai dari kondisi : {hasil}")

hasil = (a != b) and ( kondisi == False) # sifat and itu harus kondisi 1 dan kondisi 2 nya sama
print(f"Apakah hasil kiri dan kanan sama : {hasil}")
hasil = (a != b) or ( kondisi != False)
print(f"Apakah hasil kiri dan kanan salah satunya benar : {hasil}")