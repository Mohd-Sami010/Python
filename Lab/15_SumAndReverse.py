num = int(input("Enter number: "))

sum = 0
rev = 0
while num > 0:
    d = num % 10
    sum += d
    rev = rev * 10 + d
    num //= 10

print("Sum:", sum)
print("Reverse:", rev)