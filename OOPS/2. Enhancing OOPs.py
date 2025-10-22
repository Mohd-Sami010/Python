
#   DAY 2: Enhancing OOPs

# Inheritance:
'''
Inheritance allows a class to inherit attributes and methods from another class,
promoting code reuse and logical hierarchy.
Ex: A Vehicle class, from which we can derive more specific classes like Car and Truck.
'''
class vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def showInfo(self):
        print(f'Vehicle: {self.year} {self.make} {self.model}')

class Car(vehicle):
    def __init__(self, make, model, year, no_doors):
        super().__init__(make, model, year)
        self.no_doors = no_doors

    def showInfo(self):
        super().showInfo()
        print(f'Number of doors: {self.no_doors}')

class Truck(vehicle):
    def __init__ (self, make, model, year, payload_capacity):
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity

    def showInfo(self):
        super().showInfo()
        print(f"Payload capacity: {self.payload_capacity}")

    # Creating OBJs
car = Car("Ford", "Mustang GT", 2006, 2)
truck = Truck("Ford", "F-150", 2022, 3)

car.showInfo()
truck.showInfo();       print()


# Polymorphism:
'''
Polymorphism allows objects of different classes to be treated as objects of a common superclass,
and for methods to be used interchangeably.
Ex: Different animals make different sounds, but they all implement the make_sound method.
'''
class Animal:
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        return "Meow"
    
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
def animal_sound(animal):
    print(animal.make_sound())

    # Using Polymorphism
dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat);      print()


# Encapsulation:
'''
Encapsulation bundles the data and methods that operate on the data into a single unit 
and restricts access to some of the object's components.
Ex: A bank account class should hide its balance attribute to prevent unauthorized access.
'''
class BankAccount:
    def __init__ (self, account_number, balance = 0):
        self.account_number = account_number
        self.__balance = balance # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Insufficient funds or invalid amount!")

    def get_balance(self):
        return self.__balance
    
    # Creating bank account OBJ
account = BankAccount(123456, 1000)
account.deposit(500)
account.withdraw(300)
print(account.get_balance())

'Attempting to access private data directly'
try: print(account.__balance) # Attribute error
except Exception as e: print(e, '\n')


# Homework
'''
 Create a class Employee with attributes name, age, and salary.
 Include a method display_info to print these attributes.
 Create a subclass Manager that inherits from Employee.
 Add an additional attribute department.
 Override the display_info method to include department.
'''
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def displayInfo(self):
        print(f"{self.name} is {self.age} years old and his salary is {self.salary}")

class Manager(Employee):
    def __init__ (self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def displayInfo(self):
        super().displayInfo()
        print(f"He works in {self.department} department.")

abdul = Employee("Abdul", 21, 30000)
Sami = Manager("Sami", 22, 60000, "Computer Science")

abdul.displayInfo()
Sami.displayInfo()