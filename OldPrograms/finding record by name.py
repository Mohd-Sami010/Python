name = input('enter name:')
with open('Names.dat','rb') as f:
	data= (f.read()).decode()
	i= data.find(name)
	
	if name not in data:
		print('Not Found')
	else:
		print(int(i/10)+1)