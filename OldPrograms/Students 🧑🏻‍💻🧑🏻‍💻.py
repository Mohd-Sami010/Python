std={}
c='y'
while c=='y'or c=='Y':
	roll=int(input('Enter roll number: '))
	marks=eval(input('Enter Marks: '))
	std[roll]=marks
	c=input('\nWant to add more:')

#Percentage, highest percantage & less than 50%
highest=0
highroll=0
less={}
for i in std:
	total=0
	perc=1
	x=std[i]
	for j in x:
		total+=j
		perc=total/500*100
		std[i]=perc
	if perc>highest:
		highest=perc
		highroll=i
	if perc<50:
		less[i]=perc
print('\n',std,'\n\nHighest percentage\n'.upper(),'Roll number=',highroll,':',highest,'%','\n\nLower than 50% percentage list\n',less,sep='') 