""""# Finding fibonacci through assigning number of terms
term = int(input("enter number of term"))
n1, n2 = 0, 1
count = 0
print("fibonacci series")
while count < term:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1"""


# Finding fibonacci through assigning range of the number
t_max = int(input("enter number of term"))
n1, n2 = 0, 1
print("fibonacci series")
while n1 < t_max:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
