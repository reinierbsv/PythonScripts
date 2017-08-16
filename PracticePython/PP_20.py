"""
Write a function that takes an ordered list of numbers (a list where the elements are in order
from smallest to largest) and another number. The function decides whether or not the given number
is inside the list and returns (then prints) an appropriate boolean.

Extras:
Use binary search.
"""

def elmsearch (a, num):
    if num in a:
        return "True"
    else:
        return "False"

def binarySearch(a, nmm):
    key = False
    pointer = int(len(a)/2) - 1
    if num == a[0]:
        key = True
    else:
        while key is False:
            if num == a[pointer]:
                key = True
                break
            elif num > a[pointer]:
                pointer = pointer + int(pointer/2)
                print pointer
                if pointer == len(a):
                    break
            else:
                pointer = pointer - int(pointer/2)
                print pointer
                if pointer == 1:
                    break
    return key

a = [1, 3, 8, 15, 68, 78, 99, 124, 147]
num = 82

print elmsearch(a, num)
print binarySearch(a, num)
