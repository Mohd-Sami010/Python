str=input('Enter any sentance:')

'''7=t,T
1=i,I
0=o,O
3=e,E
4=a,A
'''
new=''

for i in str:
    if (i=='i' or i=='I'):
        new+= '1'
        
    elif (i=='o' or i=='O'):
        new+= '0'
    
    elif (i=='e' or i=='E'):
        new+= '3'
        
    elif (i=='a' or i=='A'):
        new+= '4'
        
    elif (i=='b' or i=='B'):
        new+= '6'
    
    elif (i=='s' or i=='S'):
        new+= '$'
        
    elif (i=='c' or i=='C'):
        new+= '('
        
    else:
        new+=i

print(new)