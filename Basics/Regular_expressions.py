import re


Line = "I am From Colombia"
# ^ At the beginning of each line
# . any character
# * different characters:
# \S any character except whitespace:
if re.search('^From', Line):
    print(Line)

