number = int(input('Enter Number: '))
copy = number
reverse = 0

# Finding Reverse
while number != 0:
    remainder = number % 10
    reverse = reverse * 10 + remainder
    number = number//10

# Checking for Palindrome
if copy == reverse:
    print('%d is PALINDROME' % copy)
else:
    print('%d is NOT PALINDROME' % copy)


# This method can also be used
"""
num = input("Enter a number")
if num == num[::-1]:
    print("Yes its a palindrome")
else:
    print("No, its not a palindrome")
"""