from student import Student
from instructor import Instructor
from course import Course

students = []


# instructor defnition
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
# course defnition
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

    name = str(input("Enter admin name: "))
    admin_id = int(input("Enter admin id: "))
    if name == ADMIN_NAME and admin_id == ADMIN_ID:
        print("Login successful")
    else:
        print("Access denied")
        exit()
        


# menu function
def show_menu():
    print("welcome to Ai_Hero course center... please choose an option:")
    print("1. Add student")
    print("2. Display students")
    print("3. search for courses")
    print("4. enroll student in courses")
    print("5. display courses")
    print("6. Delete student")
    print("7. Show Course Statistics")
    print("8. Exit")
# add student function 
def add_student():
    name = str(input("Enter student name: "))
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
      
# display students function
def display_students():
    if not students:
        print("No students found.")
    else:
        for student in students:
            student.display()
            print("-" * 20)
            
# search for courses function
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
                
#enroll student in courses function
def enroll_student_in_course():
    student_id = int(input("Enter student ID: "))
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

    course_number = int(input("Choose course number: "))

    if 1 <= course_number <= len(courses):
        selected_course = courses[course_number - 1]

        if selected_course not in selected_student.courses:
            selected_student.courses.append(selected_course)
            print("Course added successfully.")
        else:
            print("Student already enrolled in this course.")
    else:
        print("Invalid course number.")   
# display courses function
def display_courses():
    for course in courses:
        print(f"Title: {course.title}")
        print(f"Price: {course.price}")
        print(f"Instructor: {course.Instructor.name}")
        print("-" * 20)                
# Delete student function
def delete_student():
    student_id = int(input("Enter student ID to delete: "))
    found = False

    for student in students:
        if student.ID == student_id:
            students.remove(student)
            print("Student deleted successfully.")
            found = True
            break

    if not found:
        print("Student not found.") 
#Show Course Statistics function
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
                        
admin_login()

while True:
    show_menu()
    try:
     choice = input("Enter your choice: ")
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    if choice == "1":
        add_student()
    
    elif choice == "2":  
     display_students()

    elif choice == "3":

        search_courses()
        
    elif choice == "4":
        enroll_student_in_course()
        
    elif choice == "5":
        display_courses()
   
    elif choice == "6":
        delete_student()
        
    elif choice == "7":
     show_course_statistics()
                  
    elif choice == "8":
        break 
    else:
        print("Invalid choice")
         