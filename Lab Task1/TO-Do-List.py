students = []

def add_student():
    try:
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        math = int(input("Enter Math Marks: "))
        science = int(input("Enter Science Marks: "))
        english = int(input("Enter English Marks: "))

        student = {
            "roll": roll,
            "name": name,
            "marks": {
                "Math": math,
                "Science": science,
                "English": english
            }
        }
        students.append(student)
        print("Student added successfully.\n")
    except ValueError:
        print("Invalid input. Please enter numeric values for roll and marks.\n")

def view_all_students():
    if not students:
        print("No students available.\n")
        return
    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}")
    print()

def search_student():
    try:
        roll = int(input("Enter Roll Number to search: "))
        for s in students:
            if s['roll'] == roll:
                print(f"Student found: {s}\n")
                return
        print("Student not found.\n")
    except ValueError:
        print("Invalid input.\n")

def update_student():
    try:
        roll = int(input("Enter Roll Number to update: "))
        for s in students:
            if s['roll'] == roll:
                print("Enter new details for the student:")
                s['name'] = input("New Name: ")
                s['marks']['Math'] = int(input("New Math Marks: "))
                s['marks']['Science'] = int(input("New Science Marks: "))
                s['marks']['English'] = int(input("New English Marks: "))
                print("Student updated successfully.\n")
                return
        print("Student not found.\n")
    except ValueError:
        print("Invalid input.\n")

def delete_student():
    try:
        roll = int(input("Enter Roll Number to delete: "))
        for i, s in enumerate(students):
            if s['roll'] == roll:
                del students[i]
                print("Student deleted successfully.\n")
                return
        print("Student not found.\n")
    except ValueError:
        print("Invalid input.\n")

def calculate_statistics():
    if not students:
        print("No students available for statistics.\n")
        return
    total = 0
    count = 0
    highest = -1
    lowest = 101
    for s in students:

        for mark in s['marks'].values():
            total += mark
            count += 1
            highest = max(highest, mark)
            lowest = min(lowest, mark)
    avg = total / count if count > 0 else 0
    print(f"Average Marks: {avg:.2f}")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}\n")

def main_menu():
    while True:
        print("===== Student Result Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Calculate Statistics")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_all_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            calculate_statistics()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select from 1 to 7.\n")

# Run the program
main_menu()
