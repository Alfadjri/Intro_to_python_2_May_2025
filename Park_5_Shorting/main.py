import random #ini di sebut library

def random_number_generate(banyak_data):
    list_data = []
    for i in range(banyak_data):
        nilai_acak = random.randint(1,100)
        list_data.append(nilai_acak)
    return list_data


def short_bubble(data):
    panjang_list = len(data)
    for i in range(panjang_list):
        for j in range(0,panjang_list-i-1):
            if data[j] > data[j+1]:
                # temp = data[j]
                # data[j] = data[j+1]
                # data[j+1] = temp
                data[j],data[j+1] = data[j+1],data[j]

def selection_short(data):
    panjang_list = len(data)
    for i in range(panjang_list):
        min_index = i 
        for j in range(i+1,panjang_list):
            if data[j] < data[min_index]:
                min_index = j
        data[j],data[min_index] = data[min_index],data[j]



def main():
    banyak_data = int(input("Banyak data yang akan di shorting : "))
    list_data = random_number_generate(banyak_data)
    print("List data sebelum di acak :")
    print(list_data)
    input("Tekan Enter untuk lanjutkan tahapan")
    # short_bubble(list_data)
    selection_short(list_data)
    print("List data setelah di urutkan :")
    print(list_data)


if __name__ == "__main__":
    main()