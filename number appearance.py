c=int(input('Enter the range:'))
n=input('Enter number:')
apr=0
for i in range(1,c+1):
	b=str(i)
	if n in b:
		apr+=1
print('Number of appearance=',apr)