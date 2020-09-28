inicial_value = int(input())
final_value = int(input())

count = 0
while True:
    if inicial_value <= final_value:
        break
    inicial_value /= 2
    count += 1
print(count * 12)