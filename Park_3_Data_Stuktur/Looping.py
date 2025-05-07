# while
# sifat di check terlebih dahulu tapi hanya mengetahui kapan harus berhenti
count = 1001
print("=========== While ==========")
while count <= 1000:
    print(f"{count}.maaf")
    count += 1
    
# for 
# range sifat kita tau kapan harus mulai dan kapan harus berhenti
print("=============== for ==========")
for index in range(1,1001):
    print(f"{index}.maaf")
# sebanyak data yang ada 
makanans =  ['nasi', 'ayam', 'sayur', 'Pisang', 'semangka']
for makanan in makanans:
    print(f"{makanan}")
    

x = 0
while x < 100:
    if x % 2 != 0 :
        x+=1
        continue # continue di pakai kalau kamu kamu skip 1 putaran
    x += 1
    print(x)
    if x > 40 :
        break # break di pakai untuk memaksa looping berhenti