from random import randint as rand
from colorama import Fore as F

#    Taking Name
name1=input(F.LIGHTBLUE_EX+'Enter Name of 1st player: ')
name2=input(F.LIGHTCYAN_EX+'Enter Name of 2nd Player: ')

#    Checking Function
def checking(name,a,num):
    if a==num:
        print(F.GREEN+f'\nWinner is {name}')
        return True
        
    elif num<a:
        if num+3>a:
            print(F.YELLOW+'\nToo close!')
            return False
        
        print(F.LIGHTYELLOW_EX+'\nIt is Bigger number')
        return False
        
    elif num>a:
        if num-3<a:
            print(F.YELLOW+'\nToo close!')
            return False
        
        print(F.LIGHTYELLOW_EX+'\nIt is Smaller number')
        return False
        

#    game repeating loop
while True:   
#    Selection of number
    print(F.LIGHTMAGENTA_EX+'='*51,'\n\n')
    print(F.GREEN+'GAME  STARTED'.center(35))
    num=rand(0,100)
    print(F.RESET+'')
      
#    Main loop
    while True:
        
        print(F.RESET+'')
        try:
            pl1=int(input(f'\n{name1}, Enter the number: '))
        except:
            continue
        if checking(name1,pl1,num):
            break
        
        print(F.RESET+'')
        pl2=int(input(f'\n{name2}, Enter the number: '))
        if checking(name2,pl2,num):
            break