number_1 = int(input())
number_2 = int(input())
operation = input()

if operation == '+':
    result = number_1 + number_2
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
    print(f'{number_1} {operation} {number_2} = {result} - {even_odd}')
elif operation == "-":
    result = number_1 - number_2
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
    print(f'{number_1} {operation} {number_2} = {result} - {even_odd}')
elif operation == '*':
    result = number_1 * number_2
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
    print(f'{number_1} {operation} {number_2} = {result} - {even_odd}')
elif operation == '/':
    if number_2 == 0:
        print(f'Cannot divide {number_1} by zero')
    else:
        result = number_1 / number_2
        print(f'{number_1} / {number_2} = {result:.2f}')
elif operation == '%':
    if number_2 == 0:
        print(f'Cannot divide {number_1} by zero')
    else:
        result = number_1 % number_2
        print(f'{number_1} % {number_2} = {result}')
