binary = input("Enter binary: ")
octal = input("Enter octal: ")
hexa = input("Enter hexadecimal: ")

dec1 = int(binary, 2)
dec2 = int(octal, 8)
dec3 = int(hexa, 16)

print("Decimal values:", dec1, dec2, dec3)

# Convert decimal to other number systems
num = int(input("Enter integer: "))

binary = bin(num)
octal = oct(num)
hexa = hex(num)

print("Binary:", binary)
print("Octal:", octal)
print("Hexadecimal:", hexa)