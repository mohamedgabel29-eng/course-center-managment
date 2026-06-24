from person import Person
class Instructor(Person):
    def __init__(self,*args ,salary):
        super().__init__(*args)
        self.salary = salary

    def display(self):
        super().display()
        print(f"Salary: {self.salary}")
    