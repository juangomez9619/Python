numbers = [130, 22, -23, -100, 13, 45]  # basic list definition
# first index is 0
# 'is' evaluates value and type
# 0 is 0.0 -> False
# 0 == 0.0 -> True
# lists can have items with different types:
list_2 = [True, "hi", 3.14, 5, None, [3, 4, 5]]

min_number = None

for number in numbers:
    if min_number is None:
        min_number = number
    elif number < min_number:
        min_number = number

print(f"Min number: {min_number}")

# range function

for i in range(len(list_2)):
    print(list_2[i])

# add lists
a = [1, 2, 3]
b = ['a', 'b', 'c']
c = a+b

print(c[-1])

# creating a list from scratch

list_3 = list()
list_3.append(1)
list_3.append(True)
list_3.append('true')

# is x in my list?

print(False in list_3)

# len(list) how many items
# max(list) max value
# min(list) min value
# sum(list) add all values


number_list = list()
while True:
    input_number = input('enter a number')
    if input_number == 'done':
        break
    try:
        number_list.append(float(input_number))

    except:
        print('invalid data')
        continue

print('average: ', sum(number_list)/len(number_list))