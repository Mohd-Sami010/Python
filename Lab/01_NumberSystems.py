# a) WAP to take binary, octal and hexadecimal numbers as input from the user
# and convert them into their equivalent decimal number.
# b) WAP to take an integer number as input from the user
# and convert it to its equivalent binary, octal, and hexadecimal string.

# Binary
binNum = input("Enter a binary number: ")
print("Dec of", binNum, "is", int(binNum, 2))

# Octal
octNum = input("Enter an octal number:")
print("Dec of", octNum, "is", int(octNum, 8))

# Hexadecimal
hexNum = input("Enter a Hexadecimal number:")
print("Dec of", hexNum, "is", int(hexNum, 16))


# Int to Other sys
num = int(input("Enter a number: "))

binNum = bin(num)
octNum = oct(num)
hexNum = hex(num)

print(f"The binary value of {num} is {binNum}")
print(f"The octal value of {num} is {octNum}")
print(f"The hexadecimal value of {num} is {hexNum}")