import random
SEPRATOR = ";1"
def Encrypt(textToEncrypt):
    encryptedText = ""
    for c in textToEncrypt:
        # encryptedText+= c.
        numberToAdd = random.randint(0, 9)
        newChar = f"{numberToAdd}" + chr(ord(c) + numberToAdd) + SEPRATOR
        encryptedText += newChar
    return "[" + encryptedText + "]"
def Decrypt(encryptedText):
    encryptedText = encryptedText[1:-2]
    actualText = ""
    for i in encryptedText.split(SEPRATOR):
        if len(i) < 2:
            break
        numToSubtract = int(i[0])
        actualChar = chr((ord(i[1]) - numToSubtract))
        actualText += actualChar
    return actualText
print("\n\nWELCOME to PASYPTER\n")
print("-----------------------------------------------------------------")

print('''What do you want to do?
1. Encrypt
2. Decrypt''')
task = input("Enter the option number: ")
if task == "q":
    exit()
# textToEncrypt = "MohdSami" #2O10y0h3g2U0a7t6o
# print(Encrypt(textToEncrypt))

if task == "1":
    textToEncrypt = input("Enter the text to Encrypt: ")
    print("Encrypted text:", Encrypt(textToEncrypt))
elif task == "2":
    textToDecrypt = input("Enter the text to Decrypt: ")
    print("Actual text:", Decrypt(textToDecrypt))

