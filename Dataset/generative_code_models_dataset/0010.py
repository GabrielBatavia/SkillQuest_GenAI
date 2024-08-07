print("Selamat datang di program Python panjang ini!")
print("Kami akan mengeksplorasi berbagai konsep dasar dalam Python.")

# Mendefinisikan beberapa variabel
a = 10
b = 20
c = 5
d = 15

print("Variabel yang didefinisikan:")
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)

# Operasi matematika dasar
print("\nMelakukan operasi matematika dasar:")
addition = a + b
print("Penjumlahan a dan b:", addition)

subtraction = b - c
print("Pengurangan b dan c:", subtraction)

multiplication = a * c
print("Perkalian a dan c:", multiplication)

division = b / a
print("Pembagian b dan a:", division)

modulus = b % c
print("Modulus b dan c:", modulus)

exponentiation = a ** 2
print("Pemangkatan a pangkat 2:", exponentiation)

# Menggabungkan string
string1 = "Python "
string2 = "adalah bahasa yang menyenangkan!"
combined_string = string1 + string2
print("\nGabungan string:", combined_string)

# Mengulang dengan for loop
print("\nMenggunakan perulangan for:")
for i in range(1, 11):
    print("Iterasi ke-", i)

# Mengulang dengan while loop
print("\nMenggunakan perulangan while:")
count = 0
while count < 5:
    print("Iterasi ke-", count + 1)
    count += 1

# Struktur kondisional
print("\nMenggunakan struktur kondisional:")
if a < b:
    print("a lebih kecil dari b")
else:
    print("a tidak lebih kecil dari b")

if d > c:
    print("d lebih besar dari c")
else:
    print("d tidak lebih besar dari c")

# Menggunakan input dari pengguna
print("\nSekarang, mari kita terima input dari pengguna.")
user_input = input("Masukkan angka: ")
print("Anda memasukkan:", user_input)

try:
    user_number = int(user_input)
    print("Hasil penjumlahan user_number dan a:", user_number + a)
except ValueError:
    print("Input bukan angka yang valid.")

# Menggunakan list dan perulangan
print("\nMenggunakan list dan perulangan:")
my_list = [1, 2, 3, 4, 5]
print("Isi list:", my_list)

for item in my_list:
    print("Item dalam list:", item)

# Menggunakan list comprehension
print("\nMenggunakan list comprehension:")
squared_list = [x ** 2 for x in my_list]
print("List hasil pemangkatan setiap item dalam list:", squared_list)

# Menggunakan dictionary
print("\nMenggunakan dictionary:")
my_dict = {"nama": "Alice", "umur": 30, "kota": "Jakarta"}
print("Isi dictionary:", my_dict)

print("Nama dalam dictionary:", my_dict["nama"])
print("Umur dalam dictionary:", my_dict["umur"])
print("Kota dalam dictionary:", my_dict["kota"])

# Menggunakan perulangan dan dictionary
print("\nMenggunakan perulangan dan dictionary:")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

print("Selesai!")
