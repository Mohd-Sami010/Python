# a) WAP to take binary, octal and hexadecimal numbers as input from the user
# and convert them into their equivalent decimal number.
# b) WAP to take an integer number as input from the user
# and convert it to its equivalent binary, octal, and hexadecimal string.

# Binary
bin = input("Enter a binary number: ")
print("Dec of", bin, "is", int(bin, 2))

# Octal
oct = input("Enter an octal number:")
print("Dec of", oct, "is", int(oct, 8))

# Hexadecimal
hex = input("Enter a Hexadecimal number:")
print("Dec of", hex, "is", int(hex, 16))


# Int to Other sys
num = int(input("Enter a number: "))

bin = bin(num)
oct = oct(num)
hex = hex(num)

print(f"The binary value of {num} is {bin}")
print(f"The octal value of {num} is {oct}")
print(f"The hexadecimal value of {num} is {hex}")