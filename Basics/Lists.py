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