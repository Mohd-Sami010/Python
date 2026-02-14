
# Making upper triangle

ast= 1
space=14
for i in range(8):
    for j in range(space):
        print(' ',end='')
    for k in range(ast):
        print('*',end='')
    ast+=4
    space-=2
    print()
    
    
# Getting ready for second triangle

ast-=8
space+=4


# Making Lower triangle

for i in range(6,0,-1):
    for j in range(space):
        print(' ',end='')
    for k in range(ast):
        print('*',end='')
    ast-=4
    space+=2
    print()
    
# Making tail
space=11
ast=7
for i in range(3):
    for j in range(space):
        print(' ',end='')
    for k in range(ast):
        print('*',end='')
    ast+=4
    space-=2
    print()