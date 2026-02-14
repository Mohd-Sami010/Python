# Manually consume an iterator using next() inside a loop and handle StopIteration properly.

iterator = iter([1,2,3,4,5,6,7,8,9])

while True:
    try:
        print(next(iterator))
    except:
        break