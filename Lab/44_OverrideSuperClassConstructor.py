class Parent:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(f"Parent Name: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def display(self):
        super().display()
        print(f"Child Age: {self.age}")

child = Child("Idk a name", 19)
child.display()