def calculate_age(byear):
    year = 2026
    return year - byear

birth = int(input("Enter birth year: "))
age = calculate_age(birth)

print("Age:", age)