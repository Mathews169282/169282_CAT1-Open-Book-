class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade

    def display_grades(self):
        print(f"{self.name}'s Grades:")
        for assignment, grade in self.assignments.items():
            print(f"- {assignment}: {grade}")

class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added to {self.course_name}")

    def assign_grade(self, student_id, assignment_name, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment(assignment_name, grade)
                print(f"Assigned {grade} to {student.name} for {assignment_name}")
                return
        print("Student not found.")

    def display_all_grades(self):
        for student in self.students:
            student.display_grades()

# Interactive test
if __name__ == "__main__":
    instructor = Instructor("Dr. Smith", "Python Programming")

    while True:
        print("\n1. Add Student\n2. Assign Grade\n3. Display Grades\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            name = input("Student Name: ")
            sid = input("Student ID: ")
            instructor.add_student(Student(name, sid))

        elif choice == "2":
            sid = input("Student ID: ")
            assignment = input("Assignment Name: ")
            grade = input("Grade: ")
            instructor.assign_grade(sid, assignment, grade)

        elif choice == "3":
            instructor.display_all_grades()

        elif choice == "4":
            break
