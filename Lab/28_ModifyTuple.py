t = tuple(map(int, input("Enter elements: ").split()))

lst = list(t)

pos = int(input("Enter position: "))
val = int(input("Enter new value: "))

lst[pos] = val

t = tuple(lst)

print("Modified tuple:", t)