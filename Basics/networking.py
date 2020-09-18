import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

text = ['H', 'o', 'L', 'A']
output = ''
for character in text:
    output = output+character
print(output)

