class Demo:
    count = 0

    def __init__(self):
        Demo.count += 1

    @staticmethod
    def show_count():
        print("Total objects created:", Demo.count)

n = int(input("Enter number of objects: "))

for i in range(n):
    obj = Demo()

Demo.show_count()