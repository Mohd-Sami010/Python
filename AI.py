print('''  •Hey i am an incomplete AI project•

		(⁠◔⁠‿⁠◔⁠)
\n    And i can do the following works.
vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv'''.upper())
while True:
	menu=input('''

1.caculator
2.Quiz game
3.Check a number is prime or not
4.factorial finder
5.second to minute
6.How many number contains n
7.guess the number game
8.rock paper scissor game
	
enter the option number:'''.upper())
	if menu=='1':
		A=eval(input('===================================================\n\n 	  	    CALCULATOR\n\nCalculate:'))
		print('=',A)
			
		stop=input('\n Want to use more options?\n'.upper())
		if stop=='no':
			print(' 	thanks for using me :)'.upper())
			break
		else:
			print('\n\n')
	elif menu=='2':
		x=input('===================================================\n\n	   >>Welcome to python quiz<<\n\n•••••••••••••••••••••••••••••••••••••••••••••••••••\n Press Enter to start round one\n    basic knowledge:')
		i=0
		if x=='':
			a=input('\n1. In which year python is developed.\n a.1947		b.1990\n c.1956		d.1980\n=')
			if a=='b':
				print('	[Correct]')
				i+=1
			else:
				print('	Wrong, correct ans is b')
			a=input('''\n2. who developed python.
 a. Nikola testla	b.Charles babbage
 c.Guido van rossum	d.None of these\n=''')
			if a=='c':
				print('	[Correct]')
				i+=1
			else:
				print('	Wrong, correct ans is c')
			a=input('''\n3. Where python is created?
 a. New york	b.Los angeles
 c.nether land	d.Tokyo\n=''')
			if a=='c':
				print('	[Correct]')
				i+=1
			else:
				print('	Wrong, correct ans is c')
			a=input('''\n4. while can be used as a variable.
a. No		b.yes
c.may be yes	d.may be no\n=''')
			if a=='a':
				print('	[Correct]')
				i+=1
			else:
				print('	Wrong, correct ans is a')
			a=input('''\n5. * is.
 a.Exponent operator	b.Used for decoration
 c.addition operator	d.multiply operator\n=''')
			if a=='d':
				print('	[Correct]')
				i+=1
			else:
				print('	Wrong, correct ans is d')
			print('your score:',i,' out of 5')
		x=input('\n\n Press enter to start round 2\n  Fill the blanks')
		j=0
		if x=='':
			a=input('''		×Round 2×\n
1.____('hello')
a.while	  b.if
c.print	  d.none of these\n=''')
			if a=='c':
				print('	[Correct]')
				j+=1
			else:
				print('	Wrong, correct ans is c')
			a=input('''\n2.For __ in range(1,5,-1):
a.any variable	  b.true
c.True	  	  d.i
=''')
			if a=='a':
				print('	[Correct]')
				j+=1
			else:
				print('	Wrong, correct ans is a')
			a=input('''\n3.x=5
  b=__*2
  print(b)
a.x	  	  b.any number
c.both a&b	  d.none of these
=''')
			if a=='c':
				print('	[Correct]')
				j+=1
			else:
				print('	Wrong, correct ans is c')
			a=input('''\n4.String is collection of ____.
a.sets	  b.alpha num
c.numbers	  d.characters\n=''')
			if a=='d':
				print('	[Correct]')
				j+=1
			else:
				print('	Wrong, correct ans is d')
			a=input('''\n5.if a==n_
	print(a)
a.=	  b.:
c.;	  d.>\n=''')
			if a=='b':
				print('	[Correct]')
				j+=1
			else:
				print('	Wrong, correct ans is b')
			print('\n Your score:',j,'out of 5\n Total score',i+j,'out of 10')
		stop=input('\n Want to use more options?\n'.upper())
		if stop=='no':
			print(' 	thanks for using me :)'.upper())
			break
		else:
			print('\n\n')
	if menu=='3':
		n=int(input('===================================================\n\n 	      PRIME NUMBER CHECKER\n\n Enter a number= '))
		s=0
		print(' It can be divisible by=',end=' ')
		for i in range(2,n): # type: ignore
			if n%i ==0:
				print(i,end=',')
				s=i
		if s==0:
			print('only 1 &',n,'\n   ∆•Hence it is a prime number•∆')
		else:
			print('\n   ∆•Not a prime number•∆')
		stop=input('\n Want to use more options?\n'.upper())
		if stop=='no':
			print(' 	thanks for using me :)'.upper())
			break
		else:
			print('\n\n')
	elif menu=='4':
		n=int(input('===================================================\n\n           FACTORIAL(!) FINDER\n	       by Mohd Sami\n\n Enter a number: '))
		x=n-1
		a=n
		if n==1:
			print(' ',a,'!= 1',sep='') 
		elif x>2:
			while x>0:
				n=n*x
				x=x-1
			print(' ',a,'!= ',n,sep='')
		stop=input('\n Want to use more options?\n'.upper())
		if stop=='no':
			print(' 	thanks for using me :)'.upper())
			break
	elif menu=='5':
		t=int(input('===================================================\n\n\t  Convert Second to Minutes\n\nEnter time in seconds:'))
		m=t//60
		s=t%60
		print(' Time in minutes:',m,' minutes ',s,' seconds ',sep='')
		stop=input('\n Want to use more options?\n'.upper())
		if stop=='no':
			print(' 	thanks for using me :)'.upper())
			break
	elif menu=='6':
		print('===================================================\n\n    HOW MANY NUMBERS CONTAINS ENTERED NUMBER\n')
		c=int(input('Enter the range: 1 to '))
		n=input('Enter number:')
		apr=0
		for i in range(1,c+1): # type: ignore
			b=str(i)
			if n in b:
				apr+=1
		print('Number of appearance=',apr)
		stop=input('\n Want to use more options?\n'.upper())
		if stop=='no':
			print(' 	thanks for using me :)'.upper())
			break

	elif menu=='7':
		import random
		print('''===================================================

	WELCOME TO GUESS THE NUMBER GAME
	''')
		range=int(input('Enter range:'))
		n=random.randint(1,range)
		guess=None
		score=0
		while guess!=n:
			guess=int(input('\nGuess the number:'))
			if guess>n:
				print('Your guessed number is greater.')
			elif guess<n:
				print('Your guessed number is smaller')
			score+=1
		print('You won')
		if score<=4:
			print('You played like a pro ＼⁠(⁠°⁠o⁠°⁠)⁠／')
		elif score<=6:
			print('You played nice ;⁠-⁠)')
		elif score<=8:
			print('You played well')
		elif score<=15:
			print('You played like noob :⁠-⁠[')	
		stop=input('\n Want to use more options?\n'.upper())
		if stop=='no':
			print(' 	thanks for using me :)'.upper())
			break			
	elif menu=='8':
		import random
		print('===================================================\n\t   rock paper scissor game\n\n'.upper(),sep='')
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
		stop=input('\n Want to use more options?\n'.upper())
		if stop=='no':
			print(' 	thanks for using me :)'.upper())
			break
	else:
		print('\n Please enter the option number from the given.\n you can see again'.upper())