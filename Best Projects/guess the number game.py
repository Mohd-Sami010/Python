import random
from colorama import Fore as F
print('''==========================================

     WELCOME TO GUESS THE NUMBER GAME
	''')
range=int(input(F.LIGHTMAGENTA_EX+'\nEnter range:'))

while True:
	n=random.randint(1,range)
    guess=None
    score=0
    while guess != n:
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
    	print("You played like noob :⁠-⁠[")
	