l=float(input('\n\n\n        CONVERT FOOT TO INCH AND INCH TO CENTIMETER\n\n============================================================\n\n Enter lenght: '))
t=input(' Enter of unit of length (foot,inch): ')
if t=='foot':
    print('\n Lenght=',l*12,'cm',sep='')
elif t=='inch':
    print('\n Lenght=',l*2.54,'cm',sep='')
else:
    print('\n INCORRECT UNIT') 