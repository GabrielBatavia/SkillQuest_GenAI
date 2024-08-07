print("Selamat datang di program belajar Python!")
print("Mari kita mulai dengan beberapa perhitungan sederhana.")

number1 = 5
number2 = 10
number3 = 15
number4 = 20

print("Angka pertama adalah:", number1)
print("Angka kedua adalah:", number2)
print("Angka ketiga adalah:", number3)
print("Angka keempat adalah:", number4)

print("Menjumlahkan angka pertama dan kedua...")
result1 = number1 + number2
print("Hasil penjumlahan:", result1)

print("Mengurangkan angka ketiga dari angka keempat...")
result2 = number4 - number3
print("Hasil pengurangan:", result2)

print("Mengalikan angka kedua dan ketiga...")
result3 = number2 * number3
print("Hasil perkalian:", result3)

print("Membagi angka keempat dengan angka pertama...")
result4 = number4 / number1
print("Hasil pembagian:", result4)

print("Menampilkan hasil dari beberapa operasi matematika lainnya...")
result5 = (number1 + number2) * (number3 - number4)
print("Hasil operasi matematika lainnya:", result5)

print("Sekarang, mari kita coba dengan beberapa string.")
string1 = "Halo, "
string2 = "dunia!"
print("Menggabungkan string pertama dan kedua...")
result6 = string1 + string2
print("Hasil penggabungan string:", result6)

print("Mari kita ulangi beberapa kali dengan perulangan for.")
for i in range(5):
    print("Ini adalah iterasi ke-", i + 1)

print("Sekarang, kita akan menggunakan perulangan while.")
count = 0
while count < 5:
    print("Ini adalah iterasi ke-", count + 1)
    count += 1

print("Terakhir, mari kita gunakan beberapa kondisional.")
if number1 < number2:
    print("Angka pertama lebih kecil dari angka kedua.")
else:
    print("Angka pertama tidak lebih kecil dari angka kedua.")

if number3 == 15:
    print("Angka ketiga adalah 15.")
else:
    print("Angka ketiga bukan 15.")

print("Terima kasih telah menjalankan program ini. Semoga bermanfaat!")
