
#   DAY 1: Intro to OOPs

# Creating a simple class
class person():
    def __init__(self, age, name): # age, name are attributes
        self.age = age
        self.name = name

    def greet(self): # This is a method in class 'person'
        print(f'Hello I am {self.name} and I am {self.age} years old.')

    # Using the class
person1 = person(17, 'xyx')
person2 = person(23, 'abc')

person1.greet()
person2.greet() 

print()

# Practicle Exercise
class bank_account():
    def __init__ (self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposite(self, amount):
        self.balance += amount
        print(f'Deposited {amount}Rs, new balance is {self.balance}Rs.')

    def withdraw(self, amount):
        if amount > self.balance :
            print(f'You have {self.balance}Rs only.')
        else :
            self.balance -= amount
            print(f'Successfull withdrawl of {amount}Rs, remaing balance is {self.balance}Rs.')

    # Using class
new_account = bank_account('Sami', 1000)

new_account.withdraw(1500)
new_account.deposite(1200)
new_account.withdraw(1500)

print()

# Home work: Bag class
class bag():
    def __init__ (self, capacity, objects):
        self.capacity = capacity
        self.objects = objects

    def insert_object(self, obj):
        if len(self.objects) == self.capacity:
            print(f'Bag is already full, cannot insert {obj}')

        else:
            self.objects.append(obj)
            print(f'{obj.capitalize()} has been inserted in bag.')

    def throw_object(self, obj):
        objFound = False
        for i, name in enumerate(self.objects):
            if name == obj:
                self.objects.pop(i)
                print(f'{obj.capitalize()} has been thrown out of the bag.')
                objFound = True
                break
        if not objFound:
            print(f'There is no {obj.capitalize()} in your bag. ')

    # Using class
newBag = bag(3,['pen', 'copy', 'pencil'])

newBag.throw_object('pen')
newBag.throw_object('phone')
newBag.insert_object('phone')
newBag.insert_object('laptop')