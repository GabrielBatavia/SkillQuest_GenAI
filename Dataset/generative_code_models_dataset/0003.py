import random

students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eva']
subjects = ['Matematika', 'Fisika', 'Biologi', 'Kimia', 'Sejarah']

def generate_grades():
    grades = {student: {subject: random.randint(60, 100) for subject in subjects} for student in students}
    return grades

def display_grades(grades):
    for student, subjects in grades.items():
        print(f"\n{student}'s Grades:")
        for subject, grade in subjects.items():
            print(f"{subject}: {grade}")
        print()

def calculate_average(grades):
    averages = {}
    for student, subjects in grades.items():
        average = sum(subjects.values()) / len(subjects)
        averages[student] = average
    return averages

def main():
    print("Sistem Penilaian Ujian")
    grades = generate_grades()
    display_grades(grades)
    averages = calculate_average(grades)
    print("\nRata-rata Nilai:")
    for student, average in averages.items():
        print(f"{student}: {average:.2f}")

if __name__ == "__main__":
    main()
