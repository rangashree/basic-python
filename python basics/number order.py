# Reading three numbers
a = int(input("1st no."))
b = int(input("2nd no."))
c = int(input("3rd no."))

# logic for finding first largest
if a + b > b + c:
    if a > b:
        print(a, "is largest")
    else:
        print(b, "is large")
elif b > c:
    print(b, "is large")
else:
    print(c, "is large")

# logic for finding second largest
if a > b:
    if a > c:
        if b > c:
            print(b, "is 2nd largest")
        else:
            print(c, "is 2nd largest")
    else:
        print(a, "is 2nd largest")
else:
    if b > c:
        if c > a:
            print(c, "is 2nd largest")
        else:
            print(a, "is 2nd largest")
    else:
        print(b, "is 2nd largest")

# logic for finding third largest
if a + b < b + c:
    if a < b:
        print(a, "is smallest")
    else:
        print(b, "is smallest")
elif b < c:
    print(b, "is smallest")
else:
    print(c, "is smallest")
