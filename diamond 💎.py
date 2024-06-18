# Making upper triangle
ast= 1
space=7
for i in range(8):
    for j in range(space):
        print(' ',end='')
    for k in range(ast):
        print('*',end='')
    ast+=2
    space-=1
    print()
    
# Getting ready for second triangle
ast-=4
space+=2

# Making Lower triangle
for i in range(7,0,-1):
    for j in range(space):
        print(' ',end='')
    for k in range(ast):
        print('*',end='')
    ast-=2
    space+=1
    print()