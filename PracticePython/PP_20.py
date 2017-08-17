"""
Write a function that takes an ordered list of numbers (a list where the elements are in order
from smallest to largest) and another number. The function decides whether or not the given number
is inside the list and returns (then prints) an appropriate boolean.
Extras:
Use binary search.
"""


def elmsearch(a, num):
    i = 0
    while i <= len(a) - 1:
        if a[i] == num:
            return "True"
        else:
            i += 1
    else:
        return "False"


def binarysearch(a, num):
    key = False
    if num == a[0] or num == a[len(a) - 1]:
        key = True
    else:
        pmin = 1
        pmax = len(a) - 2
        p = int((pmax - pmin) / 2)
        while key is False:
            if int((pmax - pmin) / 2) == 0:
                break
            elif num == a[p]:
                key = True
            elif num > a[p]:
                pmin = p + 1
                p = pmax - int((pmax - pmin) / 2)
                if num == a[p]:
                    key = True
            else:
                pmax = p - 1
                p = pmin + int((pmax - pmin) / 2)
                if num == a[p]:
                    key = True
    return key

a = [1, 3, 8, 15, 68, 78, 99, 124, 147]
num = 100

print(elmsearch(a, num))
print(binarysearch(a, num))
