t = tuple(map(int, input("Enter elements: ").split()))
x = int(input("Enter element: "))

index = -1

for i in range(len(t)):
    if t[i] == x:
        index = i
        break

print("First occurrence index:", index)