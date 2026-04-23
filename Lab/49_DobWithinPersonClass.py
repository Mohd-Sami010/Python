class Person:
    class DOB:
        def __init__(self, day, month, year):
            self.day = day
            self.month = month
            self.year = year
        def display_dob(self):
            print(f"DOB: {self.day}-{self.month}-{self.year}")
    def __init__(self, name, day, month, year):
        self.name = name
        self.dob = Person.DOB(day, month, year)
    def display(self):
        print("Name:", self.name)
        self.dob.display_dob()

# Input
name = input("Enter name: ")
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

p = Person(name, day, month, year)
p.display()