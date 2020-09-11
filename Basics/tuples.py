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

print((1, 2) < (3, 4))