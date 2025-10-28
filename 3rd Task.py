import os

class Student:
    def __init__(self, code, name, cw1, cw2, cw3, exam):
        self.code = code
        self.name = name
        self.cw1 = int(cw1)
        self.cw2 = int(cw2)
        self.cw3 = int(cw3)
        self.exam = int(exam)
    
    def total_coursework(self):
        return self.cw1 + self.cw2 + self.cw3
    
    def overall_percentage(self):
        total = self.total_coursework() + self.exam
        return (total / 160) * 100
    
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
    
    def display(self):
        print(f"\n{'='*60}")
        print(f"Student Name: {self.name}")
        print(f"Student Number: {self.code}")
        print(f"Total Coursework Mark: {self.total_coursework()}/60")
        print(f"Exam Mark: {self.exam}/100")
        print(f"Overall Percentage: {self.overall_percentage():.2f}%")
        print(f"Grade: {self.grade()}")
        print(f"{'='*60}")

class StudentManager:
    def __init__(self, filename='studentMarks.txt'):
        self.filename = filename
        self.students = []
        self.load_students()
    
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
    
    def save_students(self):
        with open(self.filename, 'w') as f:
            f.write(f"{len(self.students)}\n")
            for s in self.students:
                f.write(f"{s.code},{s.name},{s.cw1},{s.cw2},{s.cw3},{s.exam}\n")
    
    def view_all_students(self):
        if not self.students:
            print("\nNo students found!")
            return
        
        print("\n" + "="*60)
        print("ALL STUDENT RECORDS".center(60))
        print("="*60)
        
        for student in self.students:
            student.display()
        
        avg_perc = sum(s.overall_percentage() for s in self.students) / len(self.students)
        print(f"\n{'='*60}")
        print(f"Total Students: {len(self.students)}")
        print(f"Average Percentage: {avg_perc:.2f}%")
        print(f"{'='*60}\n")
    
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
                found = False
                for s in self.students:
                    if s.name.lower() == name.lower():
                        s.display()
                        found = True
                        break
                if not found:
                    print("\nStudent not found!")
            elif choice_num == len(self.students) + 2:
                code = input("Enter student code: ")
                found = False
                for s in self.students:
                    if s.code == code:
                        s.display()
                        found = True
                        break
                if not found:
                    print("\nStudent not found!")
        except ValueError:
            print("\nInvalid input!")
    
    def show_highest_score(self):
        if not self.students:
            print("\nNo students found!")
            return
        
        highest = max(self.students, key=lambda s: s.overall_percentage())
        print("\n" + "="*60)
        print("STUDENT WITH HIGHEST SCORE".center(60))
        print("="*60)
        highest.display()
    
    def show_lowest_score(self):
        if not self.students:
            print("\nNo students found!")
            return
        
        lowest = min(self.students, key=lambda s: s.overall_percentage())
        print("\n" + "="*60)
        print("STUDENT WITH LOWEST SCORE".center(60))
        print("="*60)
        lowest.display()
    
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
            print("\nSorted in ascending order by percentage!")
        elif choice == '2':
            self.students.sort(key=lambda s: s.overall_percentage(), reverse=True)
            print("\nSorted in descending order by percentage!")
        elif choice == '3':
            self.students.sort(key=lambda s: s.name.lower())
            print("\nSorted alphabetically (A-Z)!")
        elif choice == '4':
            self.students.sort(key=lambda s: s.name.lower(), reverse=True)
            print("\nSorted alphabetically (Z-A)!")
        else:
            print("\nInvalid choice!")
            return
        
        self.view_all_students()
    
    def add_student(self):
        print("\n" + "="*60)
        print("ADD NEW STUDENT".center(60))
        print("="*60)
        
        code = input("Enter student code (1000-9999): ")
        if not (code.isdigit() and 1000 <= int(code) <= 9999):
            print("\nInvalid student code!")
            return
        
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
                print("\nInvalid marks entered!")
                return
            
            new_student = Student(code, name, cw1, cw2, cw3, exam)
            self.students.append(new_student)
            self.save_students()
            print("\nStudent added successfully!")
            new_student.display()
        except ValueError:
            print("\nInvalid input!")
    
    def delete_student(self):
        if not self.students:
            print("\nNo students found!")
            return
        
        print("\n" + "="*60)
        print("DELETE STUDENT".center(60))
        print("="*60)
        print("1. Delete by name")
        print("2. Delete by student code")
        
        choice = input("\nEnter your choice: ")
        found = False
        
        if choice == '1':
            name = input("Enter student name: ")
            for i, s in enumerate(self.students):
                if s.name.lower() == name.lower():
                    confirm = input(f"\nAre you sure you want to delete {s.name}? (yes/no): ")
                    if confirm.lower() == 'yes':
                        del self.students[i]
                        self.save_students()
                        print("\nStudent deleted successfully!")
                    found = True
                    break
        elif choice == '2':
            code = input("Enter student code: ")
            for i, s in enumerate(self.students):
                if s.code == code:
                    confirm = input(f"\nAre you sure you want to delete {s.name}? (yes/no): ")
                    if confirm.lower() == 'yes':
                        del self.students[i]
                        self.save_students()
                        print("\nStudent deleted successfully!")
                    found = True
                    break
        else:
            print("\nInvalid choice!")
            return
        
        if not found:
            print("\nStudent not found!")
    
    def update_student(self):
        if not self.students:
            print("\nNo students found!")
            return
        
        print("\n" + "="*60)
        print("UPDATE STUDENT RECORD".center(60))
        print("="*60)
        print("1. Update by name")
        print("2. Update by student code")
        
        choice = input("\nEnter your choice: ")
        student = None
        
        if choice == '1':
            name = input("Enter student name: ")
            for s in self.students:
                if s.name.lower() == name.lower():
                    student = s
                    break
        elif choice == '2':
            code = input("Enter student code: ")
            for s in self.students:
                if s.code == code:
                    student = s
                    break
        else:
            print("\nInvalid choice!")
            return
        
        if not student:
            print("\nStudent not found!")
            return
        
        print(f"\nUpdating record for: {student.name}")
        print("\n1. Update name")
        print("2. Update coursework 1 mark")
        print("3. Update coursework 2 mark")
        print("4. Update coursework 3 mark")
        print("5. Update exam mark")
        print("6. Update all marks")
        
        update_choice = input("\nEnter your choice: ")
        try:
            if update_choice == '1':
                student.name = input("Enter new name: ")
            elif update_choice == '2':
                student.cw1 = int(input("Enter new coursework 1 mark (out of 20): "))
            elif update_choice == '3':
                student.cw2 = int(input("Enter new coursework 2 mark (out of 20): "))
            elif update_choice == '4':
                student.cw3 = int(input("Enter new coursework 3 mark (out of 20): "))
            elif update_choice == '5':
                student.exam = int(input("Enter new exam mark (out of 100): "))
            elif update_choice == '6':
                student.cw1 = int(input("Enter coursework 1 mark (out of 20): "))
                student.cw2 = int(input("Enter coursework 2 mark (out of 20): "))
                student.cw3 = int(input("Enter coursework 3 mark (out of 20): "))
                student.exam = int(input("Enter exam mark (out of 100): "))
            else:
                print("\nInvalid choice!")
                return
            
            self.save_students()
            print("\nStudent record updated successfully!")
            student.display()
        except ValueError:
            print("\nInvalid input!")

def main():
    manager = StudentManager()
    
    while True:
        print("\n" + "="*60)
        print("STUDENT MANAGEMENT SYSTEM".center(60))
        print("="*60)
        print("1. View all student records")
        print("2. View individual student record")
        print("3. Show student with highest total score")
        print("4. Show student with lowest total score")
        print("5. Sort student records")
        print("6. Add a student record")
        print("7. Delete a student record")
        print("8. Update a student's record")
        print("9. Exit")
        print("="*60)
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            manager.view_all_students()
        elif choice == '2':
            manager.view_individual_student()
        elif choice == '3':
            manager.show_highest_score()
        elif choice == '4':
            manager.show_lowest_score()
        elif choice == '5':
            manager.sort_students()
        elif choice == '6':
            manager.add_student()
        elif choice == '7':
            manager.delete_student()
        elif choice == '8':
            manager.update_student()
        elif choice == '9':
            print("\nThank you for using Student Management System!")
            break
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()