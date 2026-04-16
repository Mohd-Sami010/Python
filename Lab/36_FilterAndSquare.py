d = {}

n = int(input("Enter number of elements: "))

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value

print("Original dictionary:", d)

result = {k: v*v for k, v in d.items() if v % 2 == 0}

print("Even values squared:", result)