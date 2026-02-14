# Upper triangle
space=10
for i in range(8):
	for j in range(space):
		print(' ',end='')
	for k in range(i+1):
		print('* ',end='')
	space-=1
	print()	
	
# Lower triangle
space+=2
for i in range(7,0,-1):
	for j in range(space):
		print(' ',end='')
	for k in range(i):
		print('* ',end='')
	space+=1
	print()