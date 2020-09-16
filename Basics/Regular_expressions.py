import re


Line = "I am From Colombia"
# ^ At the beginning of each line
# . any character
# * different characters:
# \S any character except whitespace:
if re.search('^From', Line):
    print(Line)

#  search returns True False

# [0-9]+ one or more digits

x = "My favorite numbers are 14 and 1302 and 1"
y = re.findall('[0-9]+', x)
print(y)

# ^F.+:

# '^From (\S+@\S+)'

text = 'From juan.gomez@gmail.com at blablabla'
my_email = re.findall('^From (\\S+@\\S+)', text)
print(my_email)