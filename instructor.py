from person import Person
class Instructor(Person):
    def __init__(self,*args ,major, salary):
        super().__init__(*args)
        self.salary = salary
        self.major = major

    def display(self):
        super().display()
        print(f"Major: {self.major}")
        print(f"Salary: {self.salary}")
    