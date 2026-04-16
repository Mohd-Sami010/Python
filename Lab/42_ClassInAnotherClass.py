class Emp:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class MyClass(Emp):
    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)

name = input("Enter name: ")
salary = int(input("Enter salary: "))

obj = MyClass(name, salary)
obj.display()