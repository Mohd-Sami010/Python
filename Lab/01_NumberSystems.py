# write a prog to take binary & ocatal & Hex and Convert to Decimal

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