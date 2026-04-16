n = int(input("Enter number of elements: "))

keys = []
values = []

print("Enter keys:")
for i in range(n):
    k = input()
    keys.append(k)

print("Enter values:")
for i in range(n):
    v = int(input())
    values.append(v)

d = {}

for i in range(n):
    d[keys[i]] = values[i]

print("Resulting dictionary:", d)