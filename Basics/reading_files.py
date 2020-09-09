my_file = open('mbox.txt', 'r')  # read the file
print(type(my_file))
hole_file = my_file.read()  # all the file in one string
print(len(hole_file))

count = 0
for line in my_file:
    count = count + 1

print(count)











