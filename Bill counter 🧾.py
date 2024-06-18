from colorama import Fore
name=input(Fore.YELLOW+'Enter name: ')
name=name.upper()
total=0
x=''
while True:
	obj=input(Fore.CYAN+'\nEnter name of item: ')
	if obj=='':
		break
	num=int(input('Enter number of items: '))
	cost=int(input(Fore.GREEN+'Enter cost: '))
	if num==0:
		bill=cost
		x+='  '+' '+obj+': ₹'+str(bill)+'\n'
	else:
		bill=cost*num
		x+=' '+str(num)+' '+obj+': ₹'+str(bill)+'\n'
	total+=bill
	#printing bill
print()
print(Fore.YELLOW+'='*40)
print(Fore.WHITE+'\n\t  bill of '.upper(),name)
print('\n\n',x,sep='')
print(Fore.GREEN+'\n Total amount: ₹',total,'\n')
print(Fore.BLUE+'×'*40)