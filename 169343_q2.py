class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}#It shows an empty dictionary.

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade

    def display_grades(self):
        if not self.assignments:
            print(f"{self.name} has no assignments yet.")
        else:
            print(f"Grades for {self.name}:")
            for assignment, grade in self.assignments.items():
                print(f"{assignment}: {grade}")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def assign_grade(self, student_id, assignment_name, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment(assignment_name, grade)
                print(f"Grade {grade} assigned to {student.name} for assignment {assignment_name}.")
                return
        print("Student not found.")

    def display_all_students(self):
        print(f"Students in {self.course_name}:")
        for student in self.students:
            student.display_grades()


def interactive_management():
    instructor_name = input("Enter instructor's name: ")
    course_name = input("Enter course name: ")
    instructor = Instructor(instructor_name, course_name)

    while True:
        action = input("Choose an action - (1) Add Student, (2) Assign Grade, (3) Display Grades, (4) Exit: ")

        if action == '1':
            student_name = input("Enter student's name: ")
            student_id = input("Enter student ID: ")
            student = Student(student_name, student_id)
            instructor.add_student(student)
            print(f"Student {student_name} added.\n")

        elif action == '2':
            student_id = input("Enter student ID: ")
            assignment_name = input("Enter assignment name: ")
            grade = input("Enter grade: ")
            instructor.assign_grade(student_id, assignment_name, grade)

        elif action == '3':
            instructor.display_all_students()

        elif action == '4':
            print("Exiting...")
            break

        else:
            print("Invalid action. Please try again.")


# To run the interactive management system
interactive_management()