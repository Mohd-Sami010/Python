# list = [2, 3, 45, 7, 8, 9, 10, 1]
list = [2, 3, 4, 5, 7, 8, 9, 10, 11]

print(list)
print("Length of list is", len(list))

isAscending = True
for i in range(1, len(list)):
    if list[i] < list[i-1]:
        isAscending = False
        break

if isAscending:
    print("List is Ascending")
else:
    print("List is not in Ascending")