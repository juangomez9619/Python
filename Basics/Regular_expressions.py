import re


Line = "I am From Colombia"
# ^ At the beginning of each line
# . any character
# * different characters:
# \S any character except whitespace:
#if re.search('^From', Line):
    #print(Line)

#  search returns True False

# [0-9]+ one or more digits

x = "My favorite numbers are 14 and 1302 and 1"
y = re.findall('[0-9]+', x)
#print(y)

# ^F.+:

# '^From (\S+@\S+)'

text = 'From juan.gomez@gmail.com at blablabla'
my_email = re.findall('^From (\\S+@\\S+)', text)
#print(my_email)

hand = ["X-DSPAM-Confidence: 0.2345 ",
        " X-DSPAM-Confidence: 0.15 ",
        " 0.2345 ",
        " X-DSPAM-Confidence: 1.235 "]

num_list = []
for line in hand:
    line = line.strip()  # remove white spaces at the beginning and the end
    interest_value = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)  # stores one item
    if len(interest_value) != 1:
        continue
    num_list.append(float(interest_value[0]))
print(max(num_list))











