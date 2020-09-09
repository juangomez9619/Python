str = " My name is Juan David "

print('My' in str)  # True or false
print('upper: ', str.upper())
print('lower:', str.lower())
print(str.replace('Juan David', 'Jose'))

# remove white spaces at the beginning and at the end
str_2 = str.strip()  # lstrip or rstrip

# find

print(str_2.find("Juan"))  # returns the position

# startswith

print(str_2.startswith('My'))  # True or false


