import random

tasks = [
    'Menyapu lantai',
    'Mencuci piring',
    'Mengosongkan tempat sampah',
    'Menata tempat tidur',
    'Membersihkan debu'
]

members = ['John', 'Mary', 'Alice', 'Tom']

def assign_tasks():
    task_assignment = {member: random.choice(tasks) for member in members}
    return task_assignment

def display_assignments(assignments):
    print("Penugasan Tugas Rumah Tangga:")
    for member, task in assignments.items():
        print(f"{member}: {task}")
    print()

def main():
    print("Sistem Penugasan Tugas Rumah Tangga")
    assignments = assign_tasks()
    display_assignments(assignments)

if __name__ == "__main__":
    main()
