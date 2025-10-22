# Linear Search
def linear_search(l,aim):
    for i in range(0,len(l)-1):
        if aim == l[i]:
            return f"{aim} found at index {i}"
    return f"{aim} is not present in this list"

l= [4,5,2,5,67]
print(linear_search(l,5))

# Binary Search
def binary_search(l,aim):
    left, right = 0, len(l)-1
    while left <= right:
        mid = left + (right - left) // 2
        if aim == l[mid]:
            return mid
        elif l[mid] < aim:
            left = mid + 1
        elif l[mid] > aim:
            right = mid - 1
    return "not found"
print(binary_search(l,67))