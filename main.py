# Dictionary to store student names and grades
student_grades = {}

# Add a new student
def add_student(name, grade):
    if name in student_grades:
        print(f"{name} already exists!")
    else:
        student_grades[name] = grade
        print(f"Added {name} with a grade of {grade}.")

# Update an existing student's grade
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name}'s grade has been updated to {grade}.")
    else:
        print(f"{name} not found!")

# Delete a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted.")
    else:
        print(f"{name} not found!")

# Display all students
def display_all_students():
    if student_grades:
        print("\nStudent Records:")
        print("-" * 25)
        for name, grade in student_grades.items():
            print(f"Name: {name} | Grade: {grade}")
        print("-" * 25)
    else:
        print("No student records found.")

# Main menu
def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            name = input("Enter student name: ").strip()
            try:
                grade = int(input("Enter student grade: "))
                add_student(name, grade)
            except ValueError:
                print("Grade must be a valid integer.")

        elif choice == 2:
            name = input("Enter student name: ").strip()
            try:
                grade = int(input("Enter new grade: "))
                update_student(name, grade)
            except ValueError:
                print("Grade must be a valid integer.")

        elif choice == 3:
            name = input("Enter student name to delete: ").strip()
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid choice! Please select a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()