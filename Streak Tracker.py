from colorama import Fore as F
from colorama import Style as S

#    Remove Colour
def removeColor():
    print(F.RESET+'',end='')
    
#    Remove light
def removeLight():
    print(S.NORMAL+'',end='')
    
#    Add light
def addLight():
    print(S.BRIGHT+'',end='')
       
#    Remove light & colour
def removeLightAndColor():
    print(F.RESET+'',end='')
    print(S.NORMAL+'',end='')
    
#   Sepration
def line():
    addLight()
    print(F.LIGHTGREEN_EX+'_'*42,'\n')
    removeLightAndColor()

def searchStreak(name):
    f = open('Streaks.txt','r')
    data = (f.read()).split(',,')
    for streak in data:
        if name == streak:
            f.close()
            return True
    f.close()
    return False

# Intro
addLight()
print(F.YELLOW+"\n\tStreak Tracker\n")
removeLight()

# Main Loop
while True:
    
    print(F.CYAN+'Type Task no./name or anything for Menu:',end='')
    choice = ((input(F.WHITE+' ')).strip()).lower()

    # Add another Streak
    if choice == 'add' or choice == '4':
        line(); addLight()
        print(F.GREEN+'\tAdd Streak\n')
        removeLight()

        print(F.LIGHTCYAN_EX+'Name your streak you want to add:',end='')
        newStreakName = ((input(F.WHITE+' ')).strip()).capitalize()
        fileCreated = False

        while not fileCreated:
        # If streak does not already exist
            if newStreakName == 'Exit':
                line()
                break
        
            if not searchStreak(newStreakName):
                f = open(f'{newStreakName}.txt','w')
                g = open('Streaks.txt','a')
                g.write(f',,{newStreakName}')
                f.close(); g.close()

                addLight()
                print(F.LIGHTGREEN_EX+'\nStreak Created Succesfully')
                removeLight(); line()
                fileCreated = True
                break
            
            elif newStreakName == 'Streaks' or searchStreak(newStreakName):
                print(F.RED+'\nStreak already exist, try another name:',end='')
                newStreakName = ((input(F.WHITE+' ')).strip()).capitalize()
                continue

            

    
    # Exit
    elif choice == 'exit' or choice == '6':
        print(F.LIGHTRED_EX+'\n\nThank you using this program ;)\n')
        print(F.RED+'*'*42)
        exit()

    else:
        line(); addLight()
        print(F.GREEN+'\tMenu')
        removeLight()
        print(F.WHITE+'''
      1. View all streaks
      2. Mark Streak
      3. View an streak
      4. Add a streak
      5. Delete streak
      6. Exit \n''')
        line(); removeLightAndColor()
        continue