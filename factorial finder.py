n=int(input('\n\n\t\tFACTORIAL(!) FINDER\n\t\tby Mohd Sami\n\n Enter a number: '))
x=n-1
a=n
if n==1:
	print(' ',a,'!= 1',sep='') 
elif x>2:
	while x>0:
		n=n*x
		x=x-1
	print(' ',a,'!= ',n,sep='')   