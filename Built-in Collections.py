
""" 
	TUPLES
Immutable sequences of arbitrary objects

 """
t = ("Norway", 4.56, 3)
print(t[0], t[2], len(t))

for item in t:
	print(item)

print(t*3)

a = ((220,265), (1134,43), (234,34), (654.4,98765))
print(a[2][1])

# Create single element tuple
k = (32,) # must have , at the end otherwise it will be parsed as int
print(type(k))

def minmax(items):
	return min(items), max(items)

x = minmax([83,22,45,33,76,89])
print(x)

""" TUPLE UNPACKING
Destructuring operation that unpacks data structures into named references
"""

lower, upper = minmax([83,22,45,33,76,89])
print(lower)
print(upper)

#swap
a = 'jelly'
b = 'bean'
a, b = b, a
print(a, b) 

print(5 in (3,5,7,8,44546))
print (5 not in (3,5,7,8,44546))

""" STRINGS """
colors = ';'.join(['#44ff', '#5117', '#fff'])
print(colors)
print(colors.split(';'))

#concatinate trick: join with empty string
print(''.join(['hig', 'way', 'man']))

print('unforgetable'.partition('forget'))

departure, separator, arrival = 'London:Edinburgh'.partition(':')
print(departure)
print(arrival)

# String Formatting
"{0} north {1} east".format(59.7, 10.4)
print("The age of {0} is {1}".format("Jim", 32))
"Current position {latitude} {longitude}".format(latitude="60N", longitude="5E")

import math
print("Math constants: pi={m.pi}, e={m.e}".format(m=math))

#F-strings available after python 3.6
print(f'Math constants: pi={math.pi}, e={math.e}')
print(f'Math constants: pi={math.pi:.3f}, e={math.e:.4f}')
import datetime
print(f'The current time is {datetime.datetime.now().isoformat()}')