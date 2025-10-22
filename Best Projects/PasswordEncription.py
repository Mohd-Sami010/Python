import random

SEPRATOR = ";0"

# Functions
def Encrypt(textToEncrypt):
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
    textToEncrypt = input("Enter the text to Encrypt: ")
    print("Encrypted text:", Encrypt(textToEncrypt))
elif task == "2":
    textToDecrypt = input("Enter the text to Decrypt: ")
    print("Actual text:", Decrypt(textToDecrypt))
