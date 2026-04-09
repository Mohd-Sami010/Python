s = {1, 2, 3}
fs = frozenset(s)

print("Set:", s)
print("Frozenset:", fs)

s.add(4)
s.remove(2)
s.update([5, 6])

print("Updated set:", s)