str = input("Enter a string: ")
charsInStr = {}

for ch in str:
    if ch == " ": 
        continue
    if ch in charsInStr:
        charsInStr[ch] += 1
    else:
        charsInStr[ch] = 1

for ch in charsInStr:
    print(f"{ch} occured {charsInStr[ch]} times")