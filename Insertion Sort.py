#	Insertion Sort
l=[15,6,13,22,3,52,2]

for i in range(1,len(l)):
	key=l[i]
	j=i-1
	
	while key < l[j] and j >= 0:
		l[j+1]=l[j]
		j-=1
		
	else:
		l[j+1]=key
		
print(l)