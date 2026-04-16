class Demo:
    def __init__(self, a, b):
        self.public = a
        self.__private = b

    def display_private(self):
        print("Private variable:", self.__private)

obj = Demo(10, 20)

print("Public variable:", obj.public)

# Access private via method
obj.display_private()