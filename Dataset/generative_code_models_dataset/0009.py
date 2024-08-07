print("Selamat datang di program belajar Python!")
print("Kami akan melakukan berbagai operasi dasar dalam program ini.")

# Mendefinisikan beberapa variabel
num1 = 8
num2 = 12
num3 = 20
num4 = 25

print("Variabel yang didefinisikan:")
print("Num1 =", num1)
print("Num2 =", num2)
print("Num3 =", num3)
print("Num4 =", num4)

# Operasi matematika dasar
print("\nMelakukan operasi matematika dasar:")
sum_result = num1 + num2
print("Hasil penjumlahan num1 dan num2:", sum_result)

diff_result = num4 - num3
print("Hasil pengurangan num4 dan num3:", diff_result)

prod_result = num2 * num3
print("Hasil perkalian num2 dan num3:", prod_result)

div_result = num4 / num1
print("Hasil pembagian num4 dan num1:", div_result)

# Menggunakan operator modulus
mod_result = num4 % num3
print("Hasil modulus num4 dan num3:", mod_result)

# Menggunakan operator pemangkatan
pow_result = num1 ** 2
print("Hasil pemangkatan num1 pangkat 2:", pow_result)

# Perulangan dengan for
print("\nMenggunakan perulangan for:")
for i in range(1, 6):
    print("Iterasi ke-", i)

# Menggunakan perulangan while
print("\nMenggunakan perulangan while:")
counter = 0
while counter < 5:
    print("Iterasi ke-", counter + 1)
    counter += 1

# Struktur kondisional
print("\nMenggunakan struktur kondisional:")
if num1 < num2:
    print("Num1 lebih kecil dari num2")
else:
    print("Num1 tidak lebih kecil dari num2")

if num3 > num4:
    print("Num3 lebih besar dari num4")
else:
    print("Num3 tidak lebih besar dari num4")

# Menggunakan nested if
print("\nMenggunakan nested if:")
if num1 < num2:
    if num2 < num3:
        print("Num1 lebih kecil dari num2, dan num2 lebih kecil dari num3")
    else:
        print("Num1 lebih kecil dari num2, tetapi num2 tidak lebih kecil dari num3")
else:
    print("Num1 tidak lebih kecil dari num2")

# Menggabungkan string
print("\nMenggabungkan string:")
string1 = "Halo, "
string2 = "selamat belajar Python!"
combined_string = string1 + string2
print("Hasil penggabungan string:", combined_string)

# String formatting
print("\nMenggunakan string formatting:")
formatted_string = f"Num1 adalah {num1}, Num2 adalah {num2}, Num3 adalah {num3}, dan Num4 adalah {num4}."
print(formatted_string)

# Menggunakan list
print("\nMenggunakan list:")
my_list = [num1, num2, num3, num4]
print("Isi list:", my_list)
print("Elemen pertama dari list:", my_list[0])
print("Elemen kedua dari list:", my_list[1])

# Menggunakan list perulangan
print("\nMenggunakan list dengan perulangan:")
for number in my_list:
    print("Elemen dalam list:", number)

# Menggunakan dictionary
print("\nMenggunakan dictionary:")
my_dict = {"satu": num1, "dua": num2, "tiga": num3, "empat": num4}
print("Isi dictionary:", my_dict)
print("Nilai untuk kunci 'dua':", my_dict["dua"])

# Menggunakan dictionary perulangan
print("\nMenggunakan dictionary dengan perulangan:")
for key, value in my_dict.items():
    print(f"Kunci: {key}, Nilai: {value}")

print("\nTerima kasih telah menjalankan program ini!")
print("Semoga Anda belajar banyak hal tentang Python.")
