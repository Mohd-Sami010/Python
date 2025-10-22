
#   DAY 3: Advanced OOP Concepts and Design Patterns

# 1. Composition
'''
It is a design principle where a class is composed of one or more OBJs from other classes.
This is often reffered to as a "has-a" realtionship.
Ex: let's consider a "library" class that contains multiple "books" OBJs.
'''
class Book :
    def __init__ (self, title, author): 
        # The constructor method initializes the title and author attributes.
        self.title = title
        self.author = author

    def __str__ (self):
        # The __str__ method returns a string representation of the Book object.
        return f"'{self.title}' by {self.author}"
    
class Library:
    def __init__(self):
        # The constructor method initializes an empty list to store books.
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books in library.")
        
        for book in self.books:
            print(book)

    # Creating book
book1 = Book("Atomic Habits", "James Clear")
book2 = Book("Rich Dad Poor Dad", "Robert Kiyosaki")

    # Creating library and adding books
library = Library()
library.add_book(book1)
library.add_book(book2)

    # Display all books
library.display_books();    print()


# 2. Abstract Base Classes (ABCs)
'''
ABCs are a way to define abstract class in python. An Abstract class can't be instantiated
and typically includes one or more abstract methods that must be implemented by subclasses. 
'''
from abc import ABC, abstractmethod

class Animal(ABC):  # Animal is an abstract base class with an abstract method sound
    @abstractmethod
    # Abstract method that must be implemented by subclasses.
    def sound(self):
        pass

class Dog(Animal):  # Implementation of the abstract method in the Dog class.
    def sound(self):
        return "woof!"
    
class Cat(Animal):
    def sound(self):
        return "meow"

    # Creating instances
dog = Dog()
cat = Cat()

print(dog.sound())
print(cat.sound());     print()


# 3. Design Patterns
'''
Design patterns are typical solutions to common problems in software designs. They are templates
designed to help write code easier to understand and maintain.
Ex: Singleton pattern:
 The singleton pattern ensures that a class has only one instance and provides a global point of
 access to it.
'''
class singleton:
    _instance = None # Class variable to hold the single instance of the class.

    # The Singleton class ensures that only one instance of the class can be created.
    def __new__(cls):
        # The __new__ method is called before __init__ and is responsible for creating a new instance.
        
        if cls._instance is None:
            # If no instance exists, create one and assign it to _instance.
            cls._instance = super(singleton, cls).__new__(cls)
        return cls._instance

    # Testing the singleton pattern
s1 = singleton()
s2 = singleton()

print(s1 is s2,'\n')


# Homework : 

    # 1. Composition: Company and Employee
'''
* Create a Company class that contains multiple Employee objects.
* Implement methods to add employees and display all employees in the company.
'''
    # 1. Composition
class Employee:
    def __init__ (self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Emp name: {self.name}, Age: {self.age}, Salary: {self.salary}"
    
class Company:
    def __init__ (self):
        self.employees = []

    def add_Employee(self, employee):
        self.employees.append(employee)

    def display_Employees(self):
        if not self.employees:
            print("No employee in company.")

        for employee in self.employees:
            print(employee)

emp1 = Employee("Rahul", 21, 40000)
emp2 = Employee("Abdul", 23, 50000)
company = Company()
company.display_Employees()
company.add_Employee(emp1)
company.add_Employee(emp2)
company.display_Employees();        print()

    # 2. Abstract Base Class: Shape
'''
2. Abstract Base Classes:
* Create an abstract base class Shape with an abstract method area.
* Implement subclasses Circle and Rectangle that provide their own implementations of area method.
* Write a program that creates instances of Circle and Rectangle, and prints their areas.
'''
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def Area(self):
        pass

class Circle(Shape):
    def Area(self, radius):
        return 3.14 * radius * radius
    
class Rectangle(Shape):
    def Area(self, length, bredth):
        return length * bredth
    
coin = Circle()
paper = Rectangle()

print(coin.Area(2))
print(paper.Area(24, 15));      print()

    # 3. Design Patterns: Factory Method
'''
3. Design Patterns:
* Implement the Factory Method pattern. Create an abstract class Transport with a method deliver.
* Implement concrete classes Truck and Ship that inherit from Transport.
* Create a factory class that returns an instance of Truck or Ship based on input.
'''
from abc import ABC , abstractmethod

class Transport(ABC):
    def Deliver(self):
        pass

class Truck(Transport):
    def Deliver(self):
        return "delivering by land in a box."
    
class Ship(Transport):
    def Deliver(self):
        return "delivering by water in container."
    
class Transport_Factory:
    def get_transport(self, transport_type):
        if transport_type == "ship":
            return Ship()
        
        elif transport_type == "truck":
            return Truck()
        else:
            return None
        
factory = Transport_Factory()
truck = factory.get_transport("truck")
print(truck)
print(truck.Deliver()) # type: ignore