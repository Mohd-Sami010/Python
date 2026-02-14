print('\n		>>Welcome to python quiz<<\n\n============================================================')
ans=input('1. In which year python is developed.\n a.1947		b.1990\n c.1956		d.1980\n=')
if ans=='b':
	print(' Correct ans')
	a=input('''\n2. who developed python.
 a. Nikola testla	b.Charles babbage
 c.Guido van rossum	d.None of these\n=''')
	if a=='c':
		print(' Correct ans')
		a=input('''\n3. Where python is created?
 a. New york	b.Los angeles
 c.nether land	d.Tokyo\n=''')
		if a=='c':
			print(' Correct ans')
			a=input('''\n4. while can be used as a variable.
a. No		b.yes
c.may be yes	d.may be no\n=''')
			if a=='a':
				print(' Correct ans')
				a=input('''\n5. * is.
 a. Exponent operator	b.For decoration
 c.addition operator	d.multiply operator\n=''')
				if a=='d':
					print(' Correct ans')
				else:
					print(' Wrong correct=d')
			else:
				print(' Wrong correct=a')
		else:
			print(' Wrong correct=c')
	else:
 		print(' Wrong correct=c')
else:
	print(' Wrong correct=b')