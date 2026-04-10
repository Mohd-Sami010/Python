lst = list(map(int, input("Enter elements: ").split()))

maximum = lst[0]
minimum = lst[0]

for i in lst:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print("Maximum:", maximum)
print("Minimum:", minimum)