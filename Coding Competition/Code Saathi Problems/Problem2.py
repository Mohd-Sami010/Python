inputString = input("Enter String to check if its palindrome: ").lower()
reversedString = inputString[::-1]
print(inputString == reversedString)