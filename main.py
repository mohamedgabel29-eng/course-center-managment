from student import Student
from instructor import Instructor
from course import Course
"""store lists for students, instructors, and courses
"""
students = []
instructors = []
courses = []

"""Admin information
"""
ADMIN_NAME = "Eng.Mohamed"
ADMIN_ID = "162007"
name = input("Enter admin name: ")
admin_id = int(input("Enter admin id: "))

if name == ADMIN_NAME and admin_id == ADMIN_ID:
    print("Login successful")
else:
    print("Access denied")
    exit()
    
# menu
while True:
    print("1. Add student")
    print("2. Display students")
    print("3. Display instructors")
    print("4. Display courses")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":

        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        ID = int(input("Enter student ID: "))

        found = False

        for student in students:

            if student.ID == ID:
                print("Student with this ID already exists.")
                found = True
                break

            if student.name == name:
                 print("Student with this name already exists.")
                 found = True
                 break

        if not found:
            student = Student(name, age, ID)
            students.append(student)
            print("Student added successfully.")
    
    elif choice == "2":
      if not students:
        print("No students found.")
      else:
        for student in students:
            student.display()
            print("-" * 20)
    elif choice == "3":
        for instructor in instructors:
            instructor.display()
    elif choice == "4":
        for course in courses:
            print(f"Title: {course.title}")
            print(f"Price: {course.price}")
    elif choice == "5":
        break 
    else:
        print("Invalid choice")