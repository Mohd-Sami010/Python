from collections import Counter

# Input keys (space separated)
keys = input("Enter elements: ").split()

counter_dict = Counter(keys)

print("Count of each element:")
for key in counter_dict:
    print(f"{key} -> {counter_dict[key]}")