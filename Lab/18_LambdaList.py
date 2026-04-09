l1 = list(map(int, input("List1: ").split()))
l2 = list(map(int, input("List2: ").split()))

result = list(map(lambda x, y: x + y, l1, l2))
filtered = list(filter(lambda x: x > 50, result))

print("Sums:", result)
print("Greater than 50:", filtered)