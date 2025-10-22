from colorama import Fore as F
from colorama import Style as S
import os

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
    print(F.LIGHTGREEN_EX+'_'*51,'\n')
    removeLightAndColor()

def searchStreak(name):
    try:
        f = open('Streaks.txt','r')
    except FileNotFoundError:
        f = open('Streaks.txt','w')
        f.close()
        f = open('Streaks.txt','r')
    data = (f.read()).split(',,')

    for streak in data:
        if name == streak:
            f.close()
            return True
        
    f.close()
    return False

# show all streaks
def showAllStreaks():
    try:
        f = open('Streaks.txt','r')
    
    except FileNotFoundError:
        print(F.RED+'\nNo streaks found, Go and Create new streak\n')
        return

    else:
        data = (f.read()).split(',,')
        if len(data) == 1:
                print(F.RED+'\nNo streaks found, Go and Create new streak\n')
                return
        data.pop(0)
        for i, streak in enumerate(data):
            print(F.WHITE+f'{i+1}. {streak}')
    print()

# Get sequence number streak
def giveIndexOf(name):
    try:
        streakNumber = int(name)
    except:
        return name
    else:
        try:
            f = open('Streaks.txt','r')
    
        except FileNotFoundError:
            print(F.RED+'\nNo streaks found.\n'); return name

        else:
            data = (f.read()).split(',,')
            if len(data) == 1:
                    print(F.RED+'\nNo streaks found.\n')
            data.pop(0)
            for i, streak in enumerate(data):
                if i+1 == streakNumber:
                    return streak
            return name



# Intro
addLight()
print(F.YELLOW+"\n\tStreak Tracker\n")
removeLight()

# Main Loop
while True:
    
    print(F.CYAN+'Type Task no./name or anything for Menu:',end='')
    choice = ((input(F.WHITE+' ')).strip()).lower()

    # View all streaks
    if choice in ('view all streaks', 'vas', 'view all', 'va', '1'):
        line(); addLight()
        print(F.CYAN+'\tAll Streaks'); removeLight()

        # Showing names of streaks
        try:
            f = open('Streaks.txt', 'r')

        except FileNotFoundError:
            print(F.RED+'\nNo streaks found, To Create new streak press 4\n')
            continue

        else:
            # Showing data
            data = (f.read()).split(',,')

            if len(data) == 1:
                print(F.RED+'\nNo streaks found, To Create new streak press 4\n')
                continue

            for streak in data:

                try:
                    g = open(f'{streak}.txt','r')
                    print(F.LIGHTYELLOW_EX+f'\n\n{streak}\n ')

                except FileNotFoundError:
                    continue

                else:
                    missed = 0
                    done = 0
                    totalDays = 0

                    streakData = g.read()

                    for day in streakData:
                        if day == '0':
                            missed += 1
                        elif day == '1':
                            done += 1
                        totalDays += 1

                    print(F.WHITE+f'Total Days: {totalDays}')
                    print(F.LIGHTGREEN_EX+'Days Streak maintained: ',end='')
                    print(F.WHITE+f'{done}')
                    print(F.RED+'Days Streak missed: ',end='')
                    print(F.WHITE+f'{missed}',end='\n'); g.close()

            line(); f.close(); removeLightAndColor()

  
    # Marking a streak done or missed
    elif choice in ('mark streak', 'ms', '2'):
        line(); addLight()
        print(F.CYAN+'\tMark Streak'); removeLight()

        choice2 = ''
        while True:
            taskDone = False
            print(F.LIGHTMAGENTA_EX+'\nMark all streaks or a single one:',end='')
            choice2 = ((input(F.WHITE+' ')).strip()).lower()

            if choice2 in ('a', 'all'):
                f = open('Streaks.txt','r')
                streaksName = (f.read()).split(',,')
                addLight()
                print(F.LIGHTBLUE_EX+'\nAnswer in yes or no according to question or type "skip" to go on next streak and "exit" to go previous step.'); removeLight()

                for streak in streaksName:
                    if streak == '':
                        continue
                    g = open(f'{streak}.txt', 'a')
                    print(F.WHITE+f'\nHave you completed task of "{streak}":',end='')
                    mark = ((input(F.GREEN+' ')).strip()).lower()

                    if mark in ('yes', 'y', '0'):
                        g.write('1')
                        addLight()
                        print(F.GREEN+f'{streak} task has been marked as done.'); removeLight()
                        taskDone = True
                        g.close(); continue
                    
                    elif mark in ('no', 'n', '1'):
                        g.write('0')
                        addLight()
                        print(F.GREEN+f'{streak} task has been marked as missed.'); removeLight()
                        taskDone = True
                        g.close(); continue
                    
                    else:
                        print(F.YELLOW+'Streak skipped and moved on next one.')
                        continue

            elif choice2 in ('one', 'b', 'o'):

                showAllStreaks()

                while True:
                    print(F.CYAN+'\nEnter Streak no./ name of streak:',end='')
                    streak = ((input(F.WHITE+' ')).strip()).lower()

                    streak = giveIndexOf(streak)
                    if streak == 'exit':
                        break

                    if searchStreak(streak.capitalize()) and streak != '': 
                        
                        g = open(f'{streak.capitalize()}.txt', 'a') 
                        print(F.WHITE+f'\nHave you completed task of {streak}:',end='')
                        mark = ((input(F.GREEN+' ')).strip()).lower()

                        if mark in ('yes', 'y', '0'):
                            g.write('1')
                            addLight()
                            print(F.GREEN+f'{streak} task has been marked as done.'); removeLight()
                            taskDone = True
                            g.close(); break
                        
                        elif mark in ('no', 'n', '1'):
                            g.write('0')
                            addLight()
                            print(F.GREEN+f'{streak} task has been marked as missed.'); removeLight()
                            taskDone = True
                            g.close(); break
                        
                    else:
                        print(F.RED+f'\nNo streak found with name/ no. "{streak}", try another name or type "exit".\n')
                        continue
            
            if taskDone:
                line(); break
            else:
                line(); break


    # View a streak patten
    elif choice in ('view a streak', '3', 'vs', 'vas'):
        line()
        print(F.GREEN+'\tView a streak using pattern\n')
        showAllStreaks()

        while True:
            
            print(F.CYAN+'\nEnter Streak no./ name of streak:',end='')
            streak = ((input(F.WHITE+' ')).strip()).lower()
            streak = giveIndexOf(streak)
            if streak == 'exit':
                line(); break
            
            if searchStreak(streak.capitalize()) and streak != '':
                f = open(f'{streak.capitalize()}.txt','r')
                data = f.read()

                print()
                for i, day in enumerate(data):
                    
                    if i == 0:
                        print(F.WHITE+' '*9,'|',end='')
                        
                    elif i % 28 == 0:
                        print('\n', ' '*10, end='')
                            

                    if day == '1':
                        addLight()
                        print(F.GREEN+'*',end=''); removeLight()

                    elif day == '0':
                        print(' ',end='')

                print(F.WHITE+f'''|\n\nIn this pattern,
'*': Days on which task of '{streak}' is done.
Spaces between '*': Days on which task is missed.
'|': Start and End of the pattern.''')

                print(); line();f.close(); break
            
            else :
                print(F.RED+f'\nNo streak found with name/ no. "{streak}", try another name or type "exit".\n')
                continue



    # Add another Streak
    elif choice == 'add' or choice == '4':
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


    # Delete streak
    elif choice in ('delete streak', 'del streak', '5', 'ds'):
        line(); addLight()
        print(F.GREEN+'\tDelete Streak\n'); removeLight()
        showAllStreaks()
        while True:
            print(F.CYAN+'\nEnter Streak no./ name of streak:',end='')
            streak = ((input(F.WHITE+' ')).strip()).lower()
            streak = giveIndexOf(streak)

            if streak == 'exit':
                line(); break
            
            if searchStreak(streak.capitalize()):
                os.remove(f'{streak.capitalize()}.txt')
                f = open('Streaks.txt', 'r')
                data = list((f.read()).split(',,'))
                newData = ''
                for name in data:
                    if name != streak.capitalize() and name != '':
                        newData += f',,{name}'
                f.close()
                f = open('Streaks.txt','w')
                f.write(newData)
                addLight()
                print(F.GREEN+f'\n"{streak}" has been deleted successfully'); removeLight(); f.close(); line(); break

            else :
                print(F.RED+f'\nNo streak found with name/ no. "{streak}", try another name or type "exit".\n')
                continue

            

    
    # Exit
    elif choice == 'exit' or choice == '6':
        print(F.LIGHTRED_EX+'\n\nThank you for using this program ;)\n')
        print(F.RED+'*'*51)
        exit()


    # Print Menu
    else:
        line(); addLight()
        print(F.GREEN+'\tMenu')
        removeLight()
        print(F.WHITE+'''
      1. View all streaks
      2. Mark Streak
      3. View an streak in pattern
      4. Add a streak
      5. Delete streak
      6. Exit \n''')
        line(); removeLightAndColor()
        continue