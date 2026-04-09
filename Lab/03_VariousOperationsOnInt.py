a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Assignment result:", a)
print("Comparison:", a == b, a > b, a < b)
print("Logical:", a and b, a or b)
print("Bitwise:", a & b, a | b, a ^ b)

a += 5
print("After assignment:", a)