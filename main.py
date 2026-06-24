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
admin_id = input("Enter admin id: ")

if name == ADMIN_NAME and admin_id == ADMIN_ID:
    print("Login successful")
else:
    print("Access denied")
    exit()
    
# menu
while True:
    print("1. Add student")
    print("2. Add instructor")
    print("3. Add course")
    print("4. Display students")
    print("5. Display instructors")
    print("6. Display courses")
    print("7. Exit")
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
        name = input("Enter instructor name: ")
        age = input("Enter instructor age: ")
        ID = int(input("Enter instructor ID: "))
        salary = float(input("Enter instructor salary: "))
        instructor = Instructor(name, age, ID, salary)
        instructors.append(instructor)
    elif choice == "3":
        title = input("Enter course title: ")
        price = float(input("Enter course price: "))
        course = Course(title, price)
        courses.append(course)
    elif choice == "4":
      if not students:
        print("No students found.")
      else:
        for student in students:
            student.display()
            print("-" * 20)
    elif choice == "5":
        for instructor in instructors:
            instructor.display()
    elif choice == "6":
        for course in courses:
            print(f"Title: {course.title}")
            print(f"Price: {course.price}")
    elif choice == "7":
        break 
    else:
        print("Invalid choice")