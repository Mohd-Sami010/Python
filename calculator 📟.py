# Calculater
A=float(input('enter 1 number'))
B=float(input('enter 2 number'))
C=input('enter operation')

if '+' in C:
	print(A + B)
	
elif '-' in C:
	print(A - B)
	
elif '*' in C:
	print(A * B)
	
elif '/' in C:
	print(A / B)
	
elif 'area' in C:
    print(A * B,'²')
    
elif 'peri' in C:
    print(2 * (A + B))