from person import Person
class Student(Person):
    def __init__(self,*args):
        super().__init__(*args)
        self.courses= []

    def display(self):
        super().display()
        print("Courses: ")
        if not self.courses:
            print("No courses enrolled.")
        else:
            for course in self.courses:
                print(f"- {course.title}")    
        