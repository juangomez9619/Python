

#  not consider an specific order
#  each value with its own label


purse = dict()   # creates a dictionary

# label(key)  - value

purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75

purse['candy'] = purse['candy'] + 2
print(purse)

dictionary = {'item_1': 14,
              'item_2': 13,
              'item_3': True,
              }

print(dictionary)

#  counting names

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)


# get method

x = counts.get('Juan', False)  # it returns the second parameter if the first one is not present
print(x)

counts_2 = dict()
names = ['juan', 'pedro', 'andres', 'juan']

for name in names:
    counts_2[name] = counts_2.get(name, 0) + 1
print(counts_2)

for key in counts_2:
    print(key, counts_2[key])


# convert key into a list
keys_counts_2 = counts_2.keys()
values_counts_2 = counts_2.values()

# two iteration variables

for key, value in counts_2.items():
    print(key, value)
















