#    Play Guy

#importing
from colorama import Fore as F
from colorama import Style as S
import random
from random import randint as rand

#    Remove Colour
def c():
    print(F.RESET+'')
    
    
#    Remove light
def lc():
    print(S.NORMAL+'')
    

#    Add light
def lo():
    print(S.BRIGHT+'')
    
    
#    Remove light & colour
def cl():
    print(F.RESET+'',end='')
    print(S.NORMAL+'')
    

#   Sepration
def line():
    lo()
    print(F.LIGHTGREEN_EX+'='*51)
    cl()
    
print('\n')
print(F.LIGHTMAGENTA_EX+'/\tWelcome To    \ '.center(40)) # type: ignore
print(S.BRIGHT+'',end='')
print(F.CYAN+'\    Play Guy     /'.center(40)) # type: ignore
cl()    
#    main Loop 
while True:
    
#    Game selection 
    lo()   
    inp=input('\nEnter name of game: ')
    
    if inp in ('guess num','guess no','gn'):
        
        gtn=input(F.LIGHTBLUE_EX+'\nEnter 1 for 1 player and 2 for 2 player:')
        cl()
        if gtn == '1':
                import random
                from colorama import Fore as F
                
                line()
                print('    WELCOME TO GUESS THE NUMBER GAME')
                range=int(input(F.LIGHTMAGENTA_EX+'\nEnter range:'))
                while True:
                
                    n=random.randint(1,range)
                    guess=None
                    score=0
                    while guess!=n:
                    	guess=int(input(F.CYAN+'\nGuess the number:'))
                        print(F.YELLOW+'')
                    	if guess>n:
                    		if n+3>guess:
                    		    print('Too Close!')
                    		    pass
                    		else:
                    		    print('Your guessed number is greater')
                    	elif guess<n:
                    		
                    		if n-3<guess:
                    		    print('Too Close!')
                    		    pass
                    		else:
                    		    print('Your guessed number is smaller')
                    	score+=1
                    print(F.GREEN+'You won')
                    if score<=3:
                    	print('You played like a pro ＼⁠(⁠°⁠o⁠°⁠)⁠／')
                    elif score<=6:
                    	print('You played nice ;⁠-⁠)')
                    elif score<=8:
                    	print('You played well')
                    elif score<=15:
                    	print('You played like noob :⁠-⁠[')
    
    else:
        print('menu')