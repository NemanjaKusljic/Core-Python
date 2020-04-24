
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


# RANGE
print(range(5))
for i in range(5):
	print(i)


print(list(range(5, 10)))
#with step argument
print(list(range(0,10,2)))
"""
range(stop)
range(start, stop)
range(start, stop, step)

enumerate:
constructs an iterable of (index, value) tuples around another iterable object
"""
t= [3,56,343545,678676]
for p in enumerate(t):
	print(p)
# with tuples unpacking
for i, v in enumerate(t):
	print(f"i = {i}, v = {v}")

# LISTS
print(t[-1]) #last element
print(t[-2])#second last element

a = [ [1,2], [3,4]]
b= a[:] #full slice
print(a is b) #false
print (a == b) #true
print (a[0] is b[0])
a[0] = [8,9]
print(a[0] is b[0])
a[1].append(5)
print(a[1] == b[1])

w = "the quick brown fox jumps over the lazy dog"
print(w.count("the"))
print("fox" in w)
print("overtccil" not in w )
a = 'I accidentally the whole universe'.split()
a.insert(2, "destroy")
print(a)
print(' '.join(a))

# DICTIONARIES

g = dict(wheat=345, color=555, seashell=16774638)
f = {'goldenrod': 1434567, 'indigo': 34567}
f.update(g)
print(f)


colors = dict(first='blue', second='green', third='black')
for key in colors:
	print(f"{key} => {colors[key]}")

#values method
for value in colors.values():
	print(value)

#keys method
for key in colors.keys():
	print(key)

#iterate over keys and values in tandem
for key, value in colors.items():
	print(f"{key} => {value}")


# SETS are unordered collections of unique elements
# Cannot contain duplicates

for x in {1,2,3,45,6,7,8}:
	print(x)

a = {1,2,3}
b = {4,5,6}
c = {5,6,7, 8, 9}
d = {3,4,9,7}
e = {1,2,3,4,5,6}

print(a.union(b))
print(a.intersection(d))
print(a.difference(d))
print(b.symmetric_difference(c))
print(a.issubset(e))
print(e.issuperset(b))
print(a.isdisjoint(c))
