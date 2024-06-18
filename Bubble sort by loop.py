l=[14,3,0,1,78,16,87,75,5,98,67,87]
n=len(l)
for i in range(n-1):
	
	for j in range(n-1-i):
		
		if l[j+1] < l[j]:
			l[j+1],l[j]=l[j],l[j+1]
	print(l)
print()
print(l)