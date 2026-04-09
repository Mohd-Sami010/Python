num = float(input("Enter number: "))
name = input("Enter name: ")
salary = float(input("Enter salary: "))

print("Right align:", format(num, ">10"))
print("Left align:", format(num, "<10"))
print("5 decimal:", format(num, ".5f"))

print(f"Name: {name}, Salary: {salary}")