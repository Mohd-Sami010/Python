size=10
while True:
	num = int(input('which record?'))
	with open('Names.dat','rb') as f:
		f.seek(size*(num-1))
		str=f.read(size)
		if len(str)==0:
			print('incorrect record')
		else:
			print(str.decode())
	ch = input('Pres y to continue:')		
	if ch == 'y':
		continue
	else:
		break