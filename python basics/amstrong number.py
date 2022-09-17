# Function to determine number of digits
def count_num(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count


# Function to check number is armstrong
def strong(n):
    num = 0
    number_copy = n
    digit = count_num(n)
    while n != 0:
        reminder = n % 10
        num += reminder**digit
        n //= 10
    print('%d will be = ' % number, num)
    return num == number_copy


number = int(input("enter num"))

print(count_num(number))

# Checking for Palindrome
if strong(number):
    print('%d is ARMSTRONG.' % number)
else:
    print('%d is NOT ARMSTRONG.' % number)
