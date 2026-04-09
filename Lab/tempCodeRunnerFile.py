count_num = 0
count_upper = 0
count_lower = 0

while True:
    ch = input("Enter char (# to stop): ")

    if ch == '#':
        break
    
    if ch.isdigit():
        count_num += 1
    elif ch.isupper():
        count_upper += 1
    elif ch.islower():
        count_lower += 1

print("Numbers:", count_num)
print("Uppercase:", count_upper)
print("Lowercase:", count_lower)