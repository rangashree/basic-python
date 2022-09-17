from math import gcd


# Defining function to calculate hcf
def hcf(a, b, c):
    num = 1
    for i in range(1, b+1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            num = i
    return num

# either methods can be used
    """num = gcd(b, c)
    num1 = gcd(a, num)
    return num1"""


# Defining function to calculate lcm
def lcm(a, b, c):
    num = 1
    num1 = 1
    for i in range(1, b+1):
        if b % i == 0 and c % i == 0:
            num = i
    l = b * c // num
    for i in range(1, a+1):
        if a % i == 0 and l % i == 0:
            num1 = i
    l2 = a * l // num1
    return l2

# either methods can be used
    """num = gcd(b, c)
    l = b * c // num
    num1 = gcd(a, l)
    l2 = a * l // num1
    return l2"""


# Reading numbers from user
first = int(input('Enter first number: '))
second = int(input('Enter second number: '))
third = int(input('Enter third number: '))

# Printing the results
print('HCF or GCD of %d and %d and %d is %d' % (first, second, third, hcf(first, second, third)))

print('LCM of %d and %d and %d is %d' % (first, second, third, lcm(first, second, third)))
