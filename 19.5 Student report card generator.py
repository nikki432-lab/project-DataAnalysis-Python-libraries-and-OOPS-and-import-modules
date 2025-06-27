#Step1. Defining the student class(Encapsulating marks within the student object)

class Student:
    def __init__(self, name , roll_no):
        self.name = name
        self.roll_no = roll_no
        self.__marks = {} #.__ private attribute encapsulation

    def add_marks(self, subject, score):
        self.__marks[subject] = score

    def get_marks(self):
        return self.__marks

#Step2. Abstract report card class(Defining a abstract method blueprint for grading systems)

from abc import ABC, abstractmethod

class  Reportcard(ABC):
    @abstractmethod
    def calculate_grade(self):
        pass

    @abstractmethod
    def generate_report(self):
        pass


#Step3. Implement grading logic(Inheritance and polymorphism) apply a grade calculation and pass/fail criteria

class Finalreportcard(Reportcard):
    def __init__(self, student):
        self.student = student

    def calculate_grade(self):
        marks = self.student.get_marks()
        average_score = sum(marks.values()) / len(marks) if marks else 0

        if average_score >= 80:
            return "A"
        elif average_score >= 60:
            return "B"
        elif average_score >= 50:
            return "C"
        elif average_score >= 35:
            return "D"
        else:
            return "F"

    def generate_report(self):
        grade = self.calculate_grade()
        overall_status = "Pass" if grade != "F" else "Fail"
        marks = self.student.get_marks()
        
        report = f"\nStudent Report Card\n"
        report += f"Name: {self.student.name}\nRoll.No: {self.student.roll_no}\n"
        report += f"\nSubjects and Marks:\n"

        for subject, score in marks.items():
            subject_status = "Pass" if score >= 35 else "Fail"
            report += f"{subject}: {score} ({subject_status})\n"

        report += f"\nOverall Grade: {grade}\nOverall Result: {overall_status}\n"
        return report

#Step.4 Defining the classroom class(Managing multiple students)

class Classroom:
    def __init__(self):
        self.students = {}

    def add_student(self, name, roll_no):
        if roll_no in self.students:
            print("Student with this roll number already exists.")
            return
        self.students[roll_no] = Student(name, roll_no)
        print(f"student{name} added successfully.")

    def add_marks(self, roll_no, subject, score):
        if roll_no in self.students:
            self.students[roll_no].add_marks(subject, score)
            print(f"Marks added for {subject}.")
        else:
            print("Student not found.")
        

    def generate_report_card(self, roll_no):
        if roll_no in self.students:
            report_card = Finalreportcard(self.students[roll_no])
            print(report_card.generate_report())
        else:
            print("Student not found.")
    
    def list_students(self):
        if not self.students:
            print("No students enrolled.")
        else:
            print("\n List of students.")
        for roll_no, student in self.students.items():
            print(f"Name: {student.name}, Roll No: {roll_no}")







#Step5. Creating the Menu-Driven-Interface(Interactive command line interface(CLI) based system for user input)

# Step 5. Creating the Menu-Driven Interface (Interactive command line interface)

def main():
    classroom = Classroom()  # Correctly initialize Classroom

    while True:
        print("\nStudent Report Card System.")
        print("1. Add student")
        print("2. Add marks")
        print("3. Generate Report Card")
        print("4. List All Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            roll_no = input("Enter roll number: ")
            classroom.add_student(name, roll_no)  # Properly add student

        elif choice == '2':
            roll_no = input("Enter roll number: ")
            if roll_no in classroom.students:  # Check if student exists in Classroom
                subject = input("Enter subject name: ")
                score = float(input(f"Enter marks for {subject}: "))
                classroom.add_marks(roll_no, subject, score)  # Add marks using Classroom method
            else:
                print("Student not found.")

        elif choice == '3':
            roll_no = input("Enter roll number: ")
            classroom.generate_report_card(roll_no)  # Generate report card

        elif choice == '4':
            classroom.list_students()  # List all students

        elif choice == '5':
            print("Exiting....")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
