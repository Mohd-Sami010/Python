x=input('enter num btw 4 and 10: ')
try:
    if ( int(x)<4 or int(x)>10 ):
        raise ValueError('enter correct number!')

except Exception as e:
    print(e)
    if ( x!='quit'):
        raise ValueError('only quit is acceptable as string')
    
print('hi')