l1 = list(map(int, input("List1: ").split()))
l2 = list(map(int, input("List2: ").split()))

common = []

for i in l1:
    if i in l2 and i not in common:
        common.append(i)

print("Common elements:", common)