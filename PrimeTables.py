def IsPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input("Enter the number of Tabels: "))
for i in range(2, num+1):
    if IsPrime(i):
        for j in range(1, 11):
            print(f"{i} * {j} = {i*j}")
        print()