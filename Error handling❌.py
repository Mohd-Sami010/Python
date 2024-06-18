# The block that can raise error
try:
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))
    print(f'{x} / {y} = {x/y}')

# Runs when an error occur
except Exception as e:
    print('An Error Occured:', e)

# Runs when No error occurs
else:
     print("No error occured ;)")

# Always runs, Does't care about errors
finally:
	print('Program Finished successfully\n')