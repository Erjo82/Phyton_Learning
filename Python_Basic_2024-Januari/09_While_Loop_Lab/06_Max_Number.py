import sys
max_number = -sys.maxsize

while True:
    number = input()
    if number == 'Stop':
        break
    current_number = int(number)
    if current_number > max_number:
        max_number = current_number

print(max_number)

