# Bubble Sort
def bubble_sort(l):
    for i in range(len(l)):
        for j in range(0, len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return(l)

l= [2,7,8,3,7,19,2]
print(bubble_sort(l))

# Quick Sort
def Quick_Sort(l):
    if len(l) <= 1:
        return l
    pivot = l[len(l) // 2]
    left = [x for x in l if x < pivot]
    middle = [x for x in l if x == pivot]
    right = [x for x in l if x > pivot]

    return Quick_Sort(left) + middle + Quick_Sort(right)

print(Quick_Sort(l))