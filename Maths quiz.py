# Maths quiz
import random
from colorama import Fore
total=0
score=0

print('	Welcome to Maths quiz\n\n'.upper())
while True:
	x=random.randint(1,50)
	y=random.randint(1,50)
	operator={1:'+',2:'-',3:'*'}
	oper=operator[random.randint(1,3)]
	
	# calculating correct answer
	if oper=='+':
		correct=x+y
		
	elif oper=='-':
		if y>x:
			continue
		else:
			correct=x-y
			
	else:
		if x>12 or y>12:
			continue
		else:
			correct=x*y
	
	#  checking
	print('what is: ',x,oper,y)
	ans=eval(input(Fore.CYAN+'your ans: '))
	
	if ans==101:
		print(score,'out of',total)
	elif ans==202:
		break
	elif ans!=101:
		total+=1
		if ans== correct:
			print(Fore.GREEN+'correct ans')
			score+=1
		else:
			print(Fore.RED+'try another')
	print(Fore.WHITE+'')