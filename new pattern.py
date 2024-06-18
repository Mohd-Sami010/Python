'''#
  # #
 #   #
#     #
 #   #
  # #
   #  '''

for i in range(4):
	for j in range(3-i):
		print(' ',end='')
		
	for k in range(2*i+1):
		if k == 0 or k== 2*i:
			print('#',end='')
		else:
			print(' ',end='')
	print()
	
for i in range(3,0,-1):
	for j in range(4-i):
		print(' ',end='')
		
	for k in range(2*i-1):
		if k == 0 or k== 2*i-2:
			print('#',end='')
		else:
			print(' ',end='')
	print()