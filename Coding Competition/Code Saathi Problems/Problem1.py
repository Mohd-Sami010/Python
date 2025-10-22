def FindLargestFromList(numbersList):
    largestNumber = 0
    for number in numbersList:
        if (number > largestNumber):
            largestNumber = number
    return largestNumber

# Example
list = [1,6,7, 10, 3]
print(FindLargestFromList(list))