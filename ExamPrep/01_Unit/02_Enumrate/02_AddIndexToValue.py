myList = [1, 3, 4, 5, 6, 8, 8, 9, 100, 11]

for i in myList: print(i)

for i, num in enumerate(myList):
    myList[i] = num + i

print("After adding")
for i in myList: print(i)