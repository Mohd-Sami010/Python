lst = list(map(int, input("Enter elements: ").split()))
n = len(lst)

for i in range(n):
    for j in range(0, n-i-1):
        if lst[j] > lst[j+1]:
            temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = temp

print("Sorted list:", lst)