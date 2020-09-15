#  tuple are like lists

x = ('1', '2', '3')
print(x[2])

#  you can´t modify a tuple.
#  tuples are more efficient than lists.

# tuples and assignment

(x, y) = (3, 'hi')
print(x)

counts = dict()

counts['Lapices'] = 50
counts['Resmas'] = 25
counts['Ganchos'] = 20

for (key, value) in counts.items():
    print(key, value)

inventario = counts.items()  # list of tuples

# tuples are comparable

print((1, 2) < (3, 4)) #priority to first item


# list of tuples
d = {'a':10,
     'b':1,
     'c':22}

#  sorted works based by the key
for key, value in sorted(d.items()):
    print(key, value)

c = {'a': 10,
     'b': 1,
     'c': 22}

tmp = list()
for key, value in c.items():
    tmp.append((value, key))

print(tmp)

tmp = sorted(tmp, reverse=True) #descending order
print(tmp)

e = {'a':13, 'b':2, 'c': 20}

print(sorted([(v, k) for k, v in e.items()], reverse=True))
