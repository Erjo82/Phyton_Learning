total_letters = int(input())
for first_letter in range(total_letters):
    for second_letter in range(total_letters):
        for third_letter in range(total_letters):
            print(f'{chr(97 + first_letter)}{chr(97 + second_letter)}{chr(97 + third_letter)}')
