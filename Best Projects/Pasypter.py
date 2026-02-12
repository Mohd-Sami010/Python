# Every Time diffrent encryption, even for the same word
# Github.com --> [1H;01j;02v;06n;04y;01c;075;05h;04s;08u;0]
# Github.com --> [6M;04m;02v;08p;06{;05g;053;07j;09x;05r;0]

import random

SEPRATOR = ";0"

# Functions
def Encrypt(textToEncrypt):
    if len(textToEncrypt) > 20:
        textToEncrypt = textToEncrypt[0:20]
        print(f"Too long password, only {textToEncrypt} will be encypted.")
    encryptedText = ""
    for c in textToEncrypt:
        numberToAdd = random.randint(0, 9)
        newChar = f"{numberToAdd}" + chr(ord(c) + numberToAdd)
        while "0" in newChar or ";" in newChar:
            numberToAdd = random.randint(0, 9)
            newChar = f"{numberToAdd}" + chr(ord(c) + numberToAdd)
        newChar += SEPRATOR
        encryptedText += newChar
    return "[" + encryptedText + "]"

def Decrypt(encryptedText):
    encryptedText= encryptedText.strip()
    if encryptedText[0] != "[" or encryptedText[-1] != "]":
        print("Enter a valid Encryted Text with []")
        return
    encryptedText = encryptedText[1:-2]
    actualText = ""
    for i in encryptedText.split(SEPRATOR):
        if len(i) < 2:
            break
        numToSubtract = int(i[0])
        actualChar = chr((ord(i[1]) - numToSubtract))
        actualText += actualChar
    return actualText

# Main Program
print("\n\nWELCOME to PASYPTER\n")
print("-----------------------------------------------------------------")

print("What do you want to do?\n1. Encrypt\n2. Decrypt")

task = input("Enter the option number: ")
if task == "1":
    textToEncrypt = input("Enter the text to Encrypt (20 characters or short): ")
    print("Encrypted text:", Encrypt(textToEncrypt))
elif task == "2":
    textToDecrypt = input("Enter the text to Decrypt: ")
    print("Actual text:", Decrypt(textToDecrypt))
