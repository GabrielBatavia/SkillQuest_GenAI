import random

products = {
    'Laptop': 10,
    'Smartphone': 25,
    'Headphones': 50,
    'Keyboard': 30,
    'Mouse': 40
}

def display_inventory():
    print("Daftar Inventaris:")
    for product, quantity in products.items():
        print(f"{product}: {quantity} unit")
    print()

def update_inventory():
    while True:
        product = input("Masukkan nama produk yang ingin diperbarui (atau ketik 'selesai' untuk mengakhiri): ").title()
        if product.lower() == 'selesai':
            break
        elif product in products:
            quantity = int(input(f"Masukkan jumlah yang akan ditambahkan untuk {product}: "))
            products[product] += quantity
        else:
            print("Produk tidak ditemukan di inventaris. Silakan pilih dari daftar yang tersedia.")
    return

def main():
    print("Selamat datang di Sistem Manajemen Inventaris!")
    display_inventory()
    update_inventory()
    print("\nInventaris Setelah Pembaruan:")
    display_inventory()

if __name__ == "__main__":
    main()
