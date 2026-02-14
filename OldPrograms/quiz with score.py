x=input('\n	   >>Welcome to python quiz<<\n\n===================================================\n Press Enter to start round one\n    basic knowledge:')
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