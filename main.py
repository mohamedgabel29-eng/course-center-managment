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