from student import Student
from instructor import Instructor
from course import Course

students = []

# instructor objects
ahmed = Instructor(
    "Ahmed Hassan",
    35,
    1001,
    major="Machine Learning",
    salary=30000
)

mohamed = Instructor(
    "Mohamed Ali",
    40,
    1002,
    major="Python Development",
    salary=10000
)

haneen = Instructor(
    "Haneen Ahmed",
    25,
    1003,
    major="Data Science",
    salary=20000
)
instructors = [ahmed, mohamed, haneen]  # List of instructor objects
# course objects
python_course = Course(
    "Python Development",
    500,
    "3 months",
    mohamed
)

ml_course = Course(
    "Machine Learning",
    700,
    "4 months",
    ahmed
)

ds_course = Course(
    "Data Science",
    600,
    "3 months",
    haneen
)
"""store lists for courses
"""
courses = [ml_course, python_course, ds_course]

"""Admin information
"""
def admin_login():
    ADMIN_NAME = "Eng.Mohamed"
    ADMIN_ID = 162007
    try:
     name = str(input("Enter admin name: "))
     admin_id = int(input("Enter admin id: "))
    except ValueError:
        print("Invalid input. Please enter valid data.")
        return False
    if name == ADMIN_NAME and admin_id == ADMIN_ID:
        print("Login successful")
        return True
    else:
        print("Access denied")
        return False
             
# ********************************************************
# menu functions 
# ********************************************************
#1. add student function 
def add_student():
    try:
     name = str(input("Enter student name: "))
     age = int(input("Enter student age: "))
     ID = int(input("Enter student ID: "))
    except ValueError:
        print("Invalid input. Please enter valid data.") 
        return

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
      
#2. display students function
def display_students():
    if not students:
        print("No students found.")
    else:
        for student in students:
            student.display()
            print("-" * 20)
            
#3. search for courses function
def search_courses():
    
    search_name = str(input("Enter course name: "))
    found = False

    for course in courses:
         if course.title.lower() == search_name.lower():

            print(f"Course: {course.title}")
            print(f"Price: {course.price}")
            print(f"Duration: {course.duration}")
            print(f"Instructor: {course.Instructor.name}")
            print(f"Major: {course.Instructor.major}")

            found = True
            break

    if not found:
          print("Course not found.")
                
#4. enroll student in courses function
def enroll_student_in_course():
    try:
     student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    selected_student = None

    for student in students:
        if student.ID == student_id:
            selected_student = student
            break

    if selected_student is None:
        print("Student not found.")
        return

    print("\nAvailable Courses:")
    for index, course in enumerate(courses, start=1):
        print(f"{index}. {course.title}")
    try:    
     course_number = int(input("Choose course number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if 1 <= course_number <= len(courses):
        selected_course = courses[course_number - 1]

        if selected_course not in selected_student.courses:
            selected_student.courses.append(selected_course)
            print("Course added successfully.")
        else:
            print("Student already enrolled in this course.")
    else:
        print("Invalid course number.")   
#5. display courses function
def display_courses():
    for course in courses:
        print(f"Title: {course.title}")
        print(f"Price: {course.price}")
        print(f"Instructor: {course.Instructor.name}")
        print("-" * 20)                
#6. Delete student function
def delete_student():
    try:
     student_id = int(input("Enter student ID to delete: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    found = False

    for student in students:
        if student.ID == student_id:
            students.remove(student)
            print("Student deleted successfully.")
            print("*" * 20)
            found = True
            break

    if not found:
        print("Student not found.") 
#7. Show Course Statistics function
def show_course_statistics():
        for course in courses:
          print("=" * 30)
          print(course.title)
          print()

          count = 0
          for student in students:
            if course in student.courses:
                print(f"- {student.name}")
                count += 1
          print(f"\nTotal Students: {count}") 
          print("*" * 20)
def admin_menu():
    while True:
        print("Welcome Admin, please choose an option:")
        print("1. Display Students")
        print("2. Search for Courses")
        print("3. Display Courses")
        print("4. Delete Student")
        print("5. Show Course Statistics")
        print("6. Exit")
        try:
            choice = input("Enter your choice: ")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == "1":
            display_students()
            print("*" * 20)
        elif choice == "2":
            search_courses()
            print("*" * 20)
        elif choice == "3":
            display_courses()
            print("*" * 20)
        elif choice == "4":
            delete_student()
            print("*" * 20)
        elif choice == "5":
            show_course_statistics()
            print("*" * 20)
        elif choice == "6":
            print("Thank you for using the system.")
            print("*" * 20)
            break
        else:
            print("Invalid choice. Please try again.")
# guest menu function
def guest_menu():
    while True:
        print("Welcome Guest, please choose an option:")
        print("1. add student")
        print("2. search for  courses")
        print("3. enroll student in course")
        print("4. display courses")
        print("5. Exit")
        try:
         choice = input("Enter your choice: ")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == "1":
            print("*" * 20)
            add_student()
            print("*" * 20)
        elif choice == "2":
            print("*" * 20)
            search_courses()
            print("*" * 20)
        elif choice == "3":
            print("*" * 20)
            enroll_student_in_course() 
            print("*" * 20)   
        elif choice == "4":
            print("*" * 20)
            display_courses()
            print("*" * 20)
        elif choice == "5":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Please try again.")              
                      
def main():                       
 while True:
    print("===== Welcome =====")
    print("1. Login as Admin")
    print("2. Continue as Guest")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":

        if admin_login():
            admin_menu()

    elif choice == "2":

        guest_menu()

    elif choice == "3":
        print("Thank you for using our system!")
        break
    
if __name__ == "__main__":
    main()          