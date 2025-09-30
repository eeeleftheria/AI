print("Hello world!")

# INTEGERS
x = 3
y = 5
z = x + y
print(z)

# FLOATS
x = 4.5
y = 6.6
print(x+y)

# BOOLEAN
x = True
y= False
z = x and y
print(z)

# STRINGS
x = "Hello"
y = "Everyone"
z = x + y;
print(z)

k = x[4] + " " + y[0]
print(k)

print(x[-1]) # last letter 
print(y[3:])
print(y[4:6])


print("Hello", "World", x[3])

s = "World"
print(f"Hello {s}") # most readable
print("Hello {}" .format(s))
print("Hello %s" %s) # old fashioned

####----------- LIST -------------####
l1 = [0,1,2,3,4,5,6,7,8]
l2 = ['a', 'b', '2', True, 2.4, [2], True]
s = len(l1)
print(f"length of l1 is {s}")
s = len(l2)
print(f"length of l2 is {s}")

# FIND INDEX
print(l2.index('b')) # find pos of b
print(l2.index(True))

# MIN, MAX
print(min(l1))
#print(min(l2)) NOT VALID!!!!

# SUM
print(sum(l1))

#Generate list of sequential items
newl = list(range(2,10)) # only for integers
print(newl)

newl.append(-1)
print(newl)

newl += [-2, -5, 7]
print(newl)
newl.sort()
print(newl)

newl.reverse()
print(newl)

newl.pop() #remove last item
print(newl)


####--------- TUPLES ------------####
# tuples cannot change at all
print("\n\nTUPLES")
l1 = ('a', '2', 'b', True, [2])
print(len(l1))
print(l1[0])
# l1[0] = 0 NOT VALID!!!!!!!


####--------- SETS ------------####
#Unordered collection of items (Mutable) - No Indexing, unique items
print("\n\nSETS")

s1 = {'a', 'b', 'c', 'b'}
print(s1)

s1.update(['c', 'a', 'd']) # union of two or more sets
print(s1)

####--------- DICTIONARIES ------------####
#Map of items (Mutable) - Unique Keys, possibly duplicate Values

print("\n\nDICTIONARIES")

# key:value
d1 = {'a': 1, 'b': 10, 'c': 1}
print(d1)
print(d1['a'])

del d1['b']
print(d1)

d1['a'] = 2
print(d1)

print(d1.keys())
print(d1.values())
print(d1.items())
