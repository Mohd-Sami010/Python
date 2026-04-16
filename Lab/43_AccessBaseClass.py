class Base:
    def __init__(self):
        print("Base constructor called")

    def show(self):
        print("This is base class method")

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Derived constructor called")

    def display(self):
        super().show()
        print("This is derived class method")

obj = Derived()
obj.display()