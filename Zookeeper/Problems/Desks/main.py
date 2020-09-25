# put your python code here
numbers = [0, 0, 0, 0]
desks = 0
for i in range(3):
    input_number = int(input())
    numbers[i] = input_number
    if input_number % 2 == 0:
        desks += input_number / 2
    else:
        desks += ((input_number / 2) + 1) // 1

# print(numbers)
print(int(desks))