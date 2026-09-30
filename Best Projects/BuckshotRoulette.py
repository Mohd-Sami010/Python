import random
print("Welcome to Buckshot Roulette")

numOfBullets: int = random.randint(1, 5);
gunMag = []
for i in range(6):
    bulletsFilled = gunMag.count(True)
    if bulletsFilled == numOfBullets:
        gunMag.append(False)
        continue
    if bulletsFilled < numOfBullets and 6 - i == numOfBullets -  bulletsFilled:
        gunMag.append(True)
        continue

    isBullet = random.randint(0,1)
    if isBullet:
        gunMag.append(True)
    else:
        gunMag.append(False)
print(numOfBullets, " full,", 6 - numOfBullets, " empty")
print(gunMag)

playerHealth: int = 5
aiHealth: int = 5

turn = random.randint(0, 1)
skipChance = False
while playerHealth > 0 and aiHealth > 0 and len(gunMag) > 0:
    print("Your health:", "|" * playerHealth, "AI health:", "|"* aiHealth)
    if turn == 0: # Player turn
        choice = int(input("1. Shoot yourself\n2. Shoot Ai\nEnter option:"))
        if choice == 1: # Shoot self
            if gunMag.pop():
                print("!! BANG !!")
                playerHealth -= 1
            else:
                print("[Empty]")
                skipChance = True
                continue
        else:
            if gunMag.pop():
                print("!! BANG !!")
                aiHealth -= 1
            else:
                print("[Empty]")
    else:
        choice = random.randint(1, 2)
        if choice == 1: # Shoot self
            print("Ai chose to shoot himself")
            if gunMag.pop():
                print("!! BANG !!")
                aiHealth -= 1
            else:
                print("[Empty]")
                skipChance = True
                continue
        else:
            print("Ai chose to shoot You")
            if gunMag.pop():
                print("!! BANG !!")
                playerHealth -= 1
            else:
                print("[Empty]")
    if not skipChance:
        turn = 0 if turn == 1 else 1
    
if aiHealth == 0:
    print("You Won")
elif playerHealth == 0:
    print("You Lose")
elif len(gunMag) == 0:
    print("Tie")