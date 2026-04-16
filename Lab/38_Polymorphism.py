def add(a, b, c=None):
    if c is None:
        return a + b
    else:
        return a + b + c

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Sum of 2 numbers:", add(x, y))

z = int(input("Enter third number: "))
print("Sum of 3 numbers:", add(x, y, z))