lst = list(map(int, input("Enter elements: ").split()))
x = int(input("Enter element to count: "))
count = 0

for i in lst:
    if i == x:
        count += 1

print("Occurrences:", count)