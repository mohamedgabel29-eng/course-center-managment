class Person:
    def __init__(self, name, age,ID):
        self.name = name
        self.age = age
        self.ID = ID

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID: {self.ID}")