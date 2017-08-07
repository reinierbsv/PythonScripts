"""
Write a program (function!) that takes a list and returns a new list that contains all the elements of the
first list minus all the duplicates.

Extras:
Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""


# using a for loop
def duplicates(A):
    B = []
    for a in A:
        if a not in B:
            B.append(a)
    return B

# using set
def duplicateSet(A):
    return list(set(A))

A = [1, 2, 5, 8, 9, 5, 7, 10, 2, 6, 7, 7, 10, 3]
print duplicates(A)
print duplicateSet(A)
