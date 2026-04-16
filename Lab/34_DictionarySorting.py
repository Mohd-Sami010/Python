d = {}
n = int(input("Enter number of elements: "))
for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value
print("Original dictionary:", d)

# Convert to list of tuples
items = list(d.items())

# Bubble sort based on values
for i in range(len(items)):
    for j in range(0, len(items) - i - 1):
        if items[j][1] > items[j+1][1]:
            temp = items[j]
            items[j] = items[j+1]
            items[j+1] = temp

print("Sorted by values:", items)

# Bubble sort based on keys
for i in range(len(items)):
    for j in range(0, len(items) - i - 1):
        if items[j][0] > items[j+1][0]:
            temp = items[j]
            items[j] = items[j+1]
            items[j+1] = temp

print("Sorted by keys:", items)