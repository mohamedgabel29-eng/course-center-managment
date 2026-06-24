from person import Person
class Student(Person):
    def __init__(self,*args ,course):
        super().__init__(*args)
        self.course = course

    def display(self):
        super().display()
        print(f"Course: {self.course}")