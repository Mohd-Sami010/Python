class Book:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages
    def __gt__(self, other):
        return self.pages > other.pages
b1 = Book("Python", 300)
b2 = Book("Java", 250)
if b1 > b2:
    print(b1.name, "has more pages")
else:
    print(b2.name, "has more pages")