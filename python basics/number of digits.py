def count_digit(n):
    count = 0
    while n:
        n //= 10
        count += 1

    return count


number = int(input('Enter number: '))

print('Number of digit is', count_digit(number))

# This method holds best for strings only, whereas for inputs like 0123 it reads it as 4 digits
"""number = input('Enter number: ')
print(len(str(number)))"""