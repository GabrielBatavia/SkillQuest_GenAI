import random

fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
colors = ['Red', 'Yellow', 'Purple', 'Green', 'Orange']

def generate_combinations():
    return {fruit: random.choice(colors) for fruit in fruits}

def display_combinations(combinations):
    print("Fruit Color Combinations:")
    for fruit, color in combinations.items():
        print(f"{fruit}: {color}")
    print()

def main():
    print("Fruit Color Combinations System")
    combinations = generate_combinations()
    display_combinations(combinations)

if __name__ == "__main__":
    main()
