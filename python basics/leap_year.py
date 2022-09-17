import random


def year():
    y = random.randint(1500, 2050)
    if y % 4 == 0:
        print("leap year")
    else:
        print("not a leap year")

    print("year was", y)
    return


year()
