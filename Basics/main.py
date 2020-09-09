total = 0
count = 0
while True:
    input_number = input("enter a number: ")
    if input_number == "done":
        break
    try:
        number = float(input_number)

    except:
        print("invalid data")
        continue

    total = total + number
    count = count + 1
    average = total / count
print("Done")
print(f"count: {count} average: {average} total: {total}")
