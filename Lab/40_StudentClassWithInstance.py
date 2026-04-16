class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 75:
            return "A"
        elif self.marks >= 50:
            return "B"
        else:
            return "C"

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Grade:", self.grade())

n = int(input("Enter number of students: "))

students = []

for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students.append(Student(name, marks))

for s in students:
    s.display()