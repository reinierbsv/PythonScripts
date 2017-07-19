"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""
a = input("Enter a word to verify if it is a palindrome or not: ")
if len(a) % 2 == 0:
    print(a, "is not a palindrome")
else:
    i = 0
    while i < int((len(a) - 1) / 2):
        if a.__getitem__(i) == a.__getitem__((len(a) - 1) - i):
            i = i + 1
        else:
            print(a, "is not a palindrome")
            break
    if i == int((len(a) - 1) / 2):
            print(a, "is a palindrome")
