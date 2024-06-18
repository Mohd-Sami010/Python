n=int(input('Enter a number:'))

#check a number is perfect or not
perfect=0
for i in range(1,n):
	if n%i==0:
		perfect=perfect+i
if n==perfect:
	print(n,'Is a perfect number\n')
elif n!=perfect:
	print(n,'Is not a perfect number\n')
	
#check a number is armstrong number or not
armstrong=0
a=n
while a!=0:
	x=a%10
	armstrong=armstrong+x**3
	a=a//10
if n==armstrong:
	print(n,'Is an Armstrong number\n')
elif n!=armstrong:
	print(n,'Is not an Armstrong number\n')
	
#check a number is palindrome or not
r=n
palindrome=0
while r!=0:
	a=r%10
	palindrome=palindrome*10+a
	r=r//10
if n==palindrome:
	print(n,'Is a Palendrome number')
else:
	print(n,'Is not palendrome number')