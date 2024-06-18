fileName= input('enter the name of file here: ')
f=open(fileName,'w')

try:
    f=f.write(input('Enter data: '))
    f=open(fileName,'r')
    print()
    print(f.read())
    
except:
    print('your entered data has been store into a new file')

finally:   
    f.close() # type: ignore