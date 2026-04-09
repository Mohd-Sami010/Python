lst = [1, 2, 3]
tup = (4, 5, 6)
string = "hello"
rng = range(5)
b = bytes([1, 2, 3])
ba = bytearray([4, 5, 6])

print(lst[1], tup[1], string[1])
print(lst[0:2], tup[0:2], string[0:2])

lst[0] = 10
ba[0] = 10

print("Modified list:", lst)
print("Modified bytearray:", ba)