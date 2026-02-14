import random
while True:
	a=input('  Press Enter')
	die=random.randint(1,6)
	if die==1:
		print('\t\t•\n')
	elif die==2:
		print('\t\t•\n\t\t •\n')
	elif die==3:
		print('\t\t•\n\t\t• •\n')
	elif die==4:
		print('\t\t• •\n\t\t• •\n')
	elif die==5:
		print('\t\t• •\n\t\t •\n\t\t• •\n')
	else:
		print('\t\t• •\n\t\t• •\n\t\t• •\n')