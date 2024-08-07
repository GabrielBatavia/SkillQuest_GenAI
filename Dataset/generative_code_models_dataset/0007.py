import random

def print_welcome():
    print("Selamat datang di permainan Tebak Angka!")
    print("Saya telah memilih angka antara 1 hingga 100.")
    print("Cobalah untuk menebaknya dalam beberapa percobaan.")

def get_random_number():
    return random.randint(1, 100)

def get_user_guess():
    while True:
        try:
            guess = int(input("Masukkan tebakan Anda: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Angka harus antara 1 dan 100. Coba lagi.")
        except ValueError:
            print("Masukkan angka yang valid.")

def play_game():
    number = get_random_number()
    attempts = 0
    max_attempts = 10
    score = 100

    while attempts < max_attempts:
        guess = get_user_guess()
        attempts += 1
        if guess < number:
            print("Tebakan Anda terlalu rendah.")
        elif guess > number:
            print("Tebakan Anda terlalu tinggi.")
        else:
            print(f"Selamat! Anda menebak angka yang benar {number} dalam {attempts} percobaan.")
            score -= (attempts - 1) * 10
            print(f"Skor akhir Anda: {score}")
            return
    print(f"Anda telah mencapai batas percobaan. Angka yang benar adalah {number}.")
    print(f"Skor akhir Anda: {score - (max_attempts - attempts) * 10}")

def main():
    print_welcome()
    while True:
        play_game()
        play_again = input("Ingin bermain lagi? (ya/tidak): ").strip().lower()
        if play_again != 'ya':
            break
    print("Terima kasih telah bermain!")

if __name__ == "__main__":
    main()
