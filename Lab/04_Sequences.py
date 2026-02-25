# Demonstration of Python Built-in Sequence Types
# list, tuple, string, range, bytes, bytearray

print("=== A. Creating Sequences ===")

# 1. List
myList = [10, 20, 30, 40, 50]
print("List:", myList)

# 2. Tuple
myTuple = (1, 2, 3, 4, 5)
print("Tuple:", myTuple)

# 3. String 
myString = "Python"
print("String:", myString)

# 4. Range
myRange = range(1, 11)  # 1 to 10
print("Range:", list(myRange))

# 5. Bytes
myBytes = bytes([65, 66, 67, 68])  # ASCII values
print("Bytes:", myBytes)

# 6. Bytearray
myByteArray = bytearray([65, 66, 67, 68])
print("Bytearray:", myByteArray)


print("\n=== B. Indexing ===")

print("myList[2]:", myList[2])
print("myTuple[1]:", myTuple[1])
print("myString[3]:", myString[3])
print("myRange[4]:", myRange[4])
print("myBytes[0]:", myBytes[0])
print("myByteArray[1]:", myByteArray[1])


print("\n=== C. Slicing ===")

print("myList[1:4]:", myList[1:4])
print("myTuple[0:3]:", myTuple[0:3])
print("myString[1:5]:", myString[1:5])
print("myRange[2:7]:", list(myRange[2:7]))
print("myBytes[1:3]:", myBytes[1:3])
print("myByteArray[1:3]:", myByteArray[1:3])


print("\n=== D. Modifying Mutable Sequences ===")

# Modify list
myList[0] = 100
myList.append(60)
print("Modified myList:", myList)

# Modify bytearray
myByteArray[0] = 90
myByteArray.append(69)
print("Modified myByteArray:", myByteArray)