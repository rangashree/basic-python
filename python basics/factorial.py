# Finding factorial using for loop
"""n = int(input('Enter number: '))
factorial = 1
for i in range(1, n+1):
    factorial = factorial*i
print("factorial", factorial)"""


# Finding factorial using while loop
def fact(num):
    factorial = 1
    while num != 0:
        factorial = factorial * num
        num -= 1
    return factorial


n = int(input('Enter number: '))
print("factorial", fact(n))
