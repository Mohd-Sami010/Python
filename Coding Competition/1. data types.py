# List methods
l = [2,4,6,3,9,10]
l.sort()
l.append(5)
l.remove(2)
l.extend([1,3,6])

# Dictionary methods
d = {'a':1,'b':2,'c':3}
d['d'] = 4
d.pop('c')
print(d.keys())
print(d.values())
print(d.items())
print(d.get('a'))

# Set Methods
s = {2,4,5,8,7,4}
s.add(18)
s.remove(2)
print(s)