s=24
for i in range(1,26):
	print(' '*s,end=' ')
	for j in range(1,i+1):
		print('*',end=' ')
	s-=1
	print()