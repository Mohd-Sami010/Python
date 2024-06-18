# Guess the Avenger

#	importing
import random
from colorama import Fore

#	Introduction
print(Fore.GREEN+'	  Welcome To '.center(28))
print(Fore.YELLOW+'	guess the avenger name\n\n'.upper().center(30))

#	list
list=['ironman','thor','falcon','captain amarica','black widow','doctor strange','hawkeye','hulk','black panther','antman','winter soldier','wanda','spiderman']
while True:
    
#	random name selection
	name=list[random.randint(0,len(list)-1)]

	#	beginning
	print('='*42)
	print(Fore.CYAN+'\n\nThe word has',len(name),'letters in it')
	n=0
	for i in name:
		n+=1
		while True:
			print(Fore.WHITE+'\nGuess the',n,'letter of name: ',end='')
			ans=input()
			if ans==i:
				print(Fore.GREEN+'Thats correct')
				break
			else:
				print(Fore.RED+'Try again')