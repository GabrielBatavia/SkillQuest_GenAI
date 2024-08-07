import random

menu = {
    'Burger': 50,
    'Pizza': 80,
    'Pasta': 60,
    'Sushi': 90,
    'Salad': 40
}

def display_menu():
    print("Menu Makanan:")
    for item, price in menu.items():
        print(f"{item}: ${price}")
    print()

def take_order():
    order = {}
    while True:
        item = input("Masukkan nama makanan yang ingin dipesan (atau ketik 'selesai' untuk mengakhiri): ").title()
        if item.lower() == 'selesai':
            break
        elif item in menu:
            quantity = int(input(f"Berapa banyak {item} yang ingin Anda pesan? "))
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
        else:
            print("Makanan tidak ada di menu. Silakan pilih dari menu yang tersedia.")
    return order

def calculate_total(order):
    total = 0
    for item, quantity in order.items():
        total += menu[item] * quantity
    return total

def main():
    print("Selamat datang di Restoran Kami!")
    display_menu()
    order = take_order()
    if order:
        print("\nRingkasan Pesanan:")
        for item, quantity in order.items():
            print(f"{item}: {quantity} x ${menu[item]} = ${menu[item] * quantity}")
        total = calculate_total(order)
        print(f"\nTotal Harga: ${total}")
    else:
        print("Tidak ada pesanan.")
    
if __name__ == "__main__":
    main()
