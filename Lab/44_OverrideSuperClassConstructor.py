# WAP to override super class constructor and method in the sub class.
class Parent:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Parent Name: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call the parent constructor
        self.age = age

    def display(self):
        super().display()  # Call the parent display method
        print(f"Child Age: {self.age}")

# Create an instance of the Child class
child = Child("Idk a name", 19)
child.display()