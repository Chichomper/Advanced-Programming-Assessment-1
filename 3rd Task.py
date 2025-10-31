# Student Management System with Comments
import os

# ---------------------------
# Student Class
# ---------------------------
class Student:
    # Constructor to initialize student data
    def __init__(self, code, name, cw1, cw2, cw3, exam):
        self.code = code
        self.name = name
        self.cw1 = int(cw1)
        self.cw2 = int(cw2)
        self.cw3 = int(cw3)
        self.exam = int(exam)

    # Calculate total coursework score out of 60
    def total_coursework(self):
        return self.cw1 + self.cw2 + self.cw3

    # Calculate final percentage (coursework + exam)
    def overall_percentage(self):
        total = self.total_coursework() + self.exam
        return (total / 160) * 100

    # Determine grade based on percentage
    def grade(self):
        perc = self.overall_percentage()
        if perc >= 70:
            return 'A'
        elif perc >= 60:
            return 'B'
        elif perc >= 50:
            return 'C'
        elif perc >= 40:
            return 'D'
        else:
            return 'F'

    # Display individual student details
    def display(self):
        print(f"\n{'='*60}")
        print(f"Student Name: {self.name}")
        print(f"Student Number: {self.code}")
        print(f"Total Coursework Mark: {self.total_coursework()}/60")
        print(f"Exam Mark: {self.exam}/100")
        print(f"Overall Percentage: {self.overall_percentage():.2f}%")
        print(f"Grade: {self.grade()}")
        print(f"{'='*60}")

# ---------------------------
# Student Manager Class
# ---------------------------
class StudentManager:
    def __init__(self, filename='studentMarks.txt'):
        self.filename = filename
        self.students = []
        self.load_students()  # Load data on startup

    # Load student records from file
    def load_students(self):
        try:
            with open(self.filename, 'r') as f:
                lines = f.readlines()
                count = int(lines[0].strip())
                self.students = []
                for i in range(1, count + 1):
                    parts = lines[i].strip().split(',')
                    student = Student(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
                    self.students.append(student)
        except FileNotFoundError:
            print(f"Error: {self.filename} not found!")
            self.students = []

    # Save student data back to file
    def save_students(self):
        with open(self.filename, 'w') as f:
            f.write(f"{len(self.students)}\n")
            for s in self.students:
                f.write(f"{s.code},{s.name},{s.cw1},{s.cw2},{s.cw3},{s.exam}\n")

    # Display all student records
    def view_all_students(self):
        if not self.students:
            print("\nNo students found!")
            return

        print("\n" + "="*60)
        print("ALL STUDENT RECORDS".center(60))
        print("="*60)

        for student in self.students:
            student.display()

        # Calculate average percentage
        avg_perc = sum(s.overall_percentage() for s in self.students) / len(self.students)
        print(f"\n{'='*60}")
        print(f"Total Students: {len(self.students)}")
        print(f"Average Percentage: {avg_perc:.2f}%")
        print(f"{'='*60}\n")

    # View individual student record
    def view_individual_student(self):
        if not self.students:
            print("\nNo students found!")
            return

        print("\n" + "="*60)
        print("SELECT A STUDENT".center(60))
        print("="*60)
        for i, s in enumerate(self.students, 1):
            print(f"{i}. {s.name} (Student Code: {s.code})")
        print(f"{len(self.students) + 1}. Search by name")
        print(f"{len(self.students) + 2}. Search by student code")

        choice = input("\nEnter your choice: ")
        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(self.students):
                self.students[choice_num - 1].display()
            elif choice_num == len(self.students) + 1:
                name = input("Enter student name: ")
                for s in self.students:
                    if s.name.lower() == name.lower():
                        s.display()
                        return
                print("\nStudent not found!")
            elif choice_num == len(self.students) + 2:
                code = input("Enter student code: ")
                for s in self.students:
                    if s.code == code:
                        s.display()
                        return
                print("\nStudent not found!")
        except ValueError:
            print("\nInvalid input!")

    # Show highest scorer
    def show_highest_score(self):
        if not self.students:
            print("\nNo students found!")
            return
        highest = max(self.students, key=lambda s: s.overall_percentage())
        print("\n" + "="*60)
        print("STUDENT WITH HIGHEST SCORE".center(60))
        print("="*60)
        highest.display()

    # Show lowest scorer
    def show_lowest_score(self):
        if not self.students:
            print("\nNo students found!")
            return
        lowest = min(self.students, key=lambda s: s.overall_percentage())
        print("\n" + "="*60)
        print("STUDENT WITH LOWEST SCORE".center(60))
        print("="*60)
        lowest.display()

    # Sort student records
    def sort_students(self):
        print("\n" + "="*60)
        print("SORT OPTIONS".center(60))
        print("="*60)
        print("1. Sort by overall percentage (Ascending)")
        print("2. Sort by overall percentage (Descending)")
        print("3. Sort by name (A-Z)")
        print("4. Sort by name (Z-A)")

        choice = input("\nEnter your choice: ")
        if choice == '1':
            self.students.sort(key=lambda s: s.overall_percentage())
        elif choice == '2':
            self.students.sort(key=lambda s: s.overall_percentage(), reverse=True)
        elif choice == '3':
            self.students.sort(key=lambda s: s.name.lower())
        elif choice == '4':
            self.students.sort(key=lambda s: s.name.lower(), reverse=True)
        else:
            print("\nInvalid choice!")
            return

        self.view_all_students()

    # Add new student
    def add_student(self):
        print("\n" + "="*60)
        print("ADD NEW STUDENT".center(60))
        print("="*60)

        code = input("Enter student code (1000-9999): ")
        if not (code.isdigit() and 1000 <= int(code) <= 9999):
            print("\nInvalid student code!")
            return

        # Check duplicate student code
        for s in self.students:
            if s.code == code:
                print("\nStudent code already exists!")
                return

        name = input("Enter student name: ")
        try:
            cw1 = int(input("Enter coursework 1 mark (out of 20): "))
            cw2 = int(input("Enter coursework 2 mark (out of 20): "))
            cw3 = int(input("Enter coursework 3 mark (out of 20): "))
            exam = int(input("Enter exam mark (out of 100): "))

            if not (0 <= cw1 <= 20 and 0 <= cw2 <= 20 and 0 <= cw3 <= 20 and 0 <= exam <= 100):
                print("\nInvalid mark!")
                return

            new_student = Student(code, name, cw1, cw2, cw3, exam)
            self.students.append(new_student)
            self.save_students()
            print("\nStudent added successfully!")
            new_student.display()
        except ValueError:
            print("\nInvalid input!")

    # Delete student record
    def delete_student(self):
        if not self.students:
            print("\nNo students found!")
            return

        print("\n1. Delete by name")
        print("2. Delete by student code")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter name: ")
            for i, s in enumerate(self.students):
                if s.name.lower() == name.lower():
                    confirm = input(f"Delete {s.name}? (yes/no): ")
                    if confirm.lower() == 'yes':
                        del self.students[i]
                        self.save_students()
                        print("Deleted!")
                    return
            print("Student not found!")

        elif choice == '2':
            code = input("Enter code: ")
            for i, s in enumerate(self.students):
                if s.code == code:
                    confirm = input(f"Delete {s.name}? (yes/no): ")
                    if confirm.lower() == 'yes':
                        del self.students[i]
                        self.save_students()
                        print("Deleted!")
                    return
            print("Student not found!")

    # Update student records
    def update_student(self):
        if not self.students:
            print("\nNo students found!")
            return

        print("\n1. Update by name")
        print("2. Update by student code")
        choice = input("Enter choice: ")

        student = None
        if choice == '1':
            name = input("Enter name: ")
            for s in self.students:
                if s.name.lower() == name.lower():
                    student = s
                    break
        elif choice == '2':
            code = input("Enter code: ")
            for s in self.students:
                if s.code == code:
                    student = s
                    break

        if not student:
            print("Student not found!")
            return

        print(f"\nUpdating: {student.name}")
        print("1. Update name")
        print("2. Update CW1")
        print("3. Update CW2")
        print("4. Update CW3")
        print("5. Update exam")
        print("6. Update all marks")

        try:
            c = input("Select option: ")
            if c == '1':
                student.name = input("New name: ")
            elif c == '2': student.cw1 = int(input("New CW1: "))
            elif c == '3': student.cw2 = int(input("New CW2: "))
            elif c == '4': student.cw3 = int(input("New CW3: "))
            elif c == '5': student.exam = int(input("New exam mark: "))
            elif c == '6':
                student.cw1 = int(input("CW1: "))
                student.cw2 = int(input("CW2: "))
                student.cw3 = int(input("CW3: "))
                student.exam = int(input("Exam: "))
            else:
                print("Invalid choice!")
                return

            self.save_students()
            print("Updated successfully!")
            student.display()
        except ValueError:
            print("Invalid input!")

# ---------------------------
# Main program menu
# ---------------------------
def main():
    manager = StudentManager()

    while True:
        print("\n" + "="*60)
        print("STUDENT MANAGEMENT SYSTEM".center(60))
        print("="*60)
        print("1. View all student records")
        print("2. View individual student record")
        print("3. Show student with highest score")
        print("4. Show student with lowest score")
        print("5. Sort records")
        print("6. Add student")
        print("7. Delete student")
        print("8. Update student record")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == '1': manager.view_all_students()
        elif choice == '2': manager.view_individual_student()
        elif choice == '3': manager.show_highest_score()
        elif choice == '4': manager.show_lowest_score()
        elif choice == '5': manager.sort_students()
        elif choice == '6': manager.add_student()
        elif choice == '7': manager.delete_student()
        elif choice == '8': manager.update_student()
        elif choice == '9':
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again!")

# Run program
if __name__ == "__main__":
    main()
