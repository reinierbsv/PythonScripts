'''
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''
a = raw_input("Enter a word to verify if it is a palindrome or not: ")
if len(a) % 2 != 0:
    i = 0
    for i in range((len(a) - 1) / 2):
        if a.__getitem__(i) != a.__getitem__((len(a) - 1) - i):
            print a, "is not a palindrome"
            break
        elif a.__getitem__(i) == a.__getitem__((len(a) - 1) - i):
            pass
    print a, "is a palindrome"
