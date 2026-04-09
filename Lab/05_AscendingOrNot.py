lst = list(map(int, input("Enter elements: ").split()))

length = len(lst)
print("Length:", length)

if lst == sorted(lst):
    print("List is ascending")
else:
    print("List is not ascending")