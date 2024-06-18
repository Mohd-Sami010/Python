import random
print('\n\t   rock paper scissor game\n\n'.upper(),'\t       by Mohd Sami\n==========================================')
bot=0
player=0
draw=0
lim=int(input('Enter the number of rounds:'))
print()
limit=1
while limit<=lim:
	x=random.randint(1,3)
	play={1:'Rock',2:'Paper',3:'Scissor'}
	play2={'r':'Rock','p':'Paper','s':'Scissor'}
	print('	[',limit,']')
	user=input('Enter your choice[r,p,s]:')
	print('Your choice:',play2[user],'\nBot choice:',play[x],'\n')
	limit+=1
	if play[x]==play2[user]:
		print('\tDraw match (⁠-⁠_⁠-⁠;⁠)\n')
		draw+=1
	elif x==1 and user=='p':
		print('\tYou Won＼⁠(⁠°⁠o⁠°⁠)⁠／\n')
		player+=1
	elif x==2 and user=='s':
		print('\tYou Won＼⁠(⁠°⁠o⁠°⁠)⁠／\n')
		player+=1
	elif x==3 and user=='r':
		print('\tYou Won＼⁠(⁠°⁠o⁠°⁠)⁠／\n')
		player+=1
	else:
		print('\tBot Won (⁠~⁠‾⁠▿⁠‾⁠)⁠~\n')
		bot+=1
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n		Final result\n'.upper(),' Your score:',player,'\n Bot Score:',bot,'\n Draw match:',draw,'\n×××××××××××××××××××××××××××××××××××××××××××××××××××',sep='')