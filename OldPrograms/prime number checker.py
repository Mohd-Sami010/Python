n=int(input(' Enter a number= '))
s=0
print(' It can be divisible by=',end=' ')
for i in range(2,n):
	if n%i ==0:
		print(i,end=',')
		s=i
if s==0:
	print('only 1 &',n,'\n   ∆•Hence it is a prime number•∆')
else:
	print('\n   ∆•Not a prime number•∆')