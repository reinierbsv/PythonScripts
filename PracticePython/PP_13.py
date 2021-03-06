"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions. Make sure to ask the user to enter
the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of
numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, etc.)
"""


def fibonnaci(n):
    if n == 1:
        a = [1]
    elif n == 2:
        a = [1, 1]
    elif n > 2:
        a = [1, 1]
        for i in range(1, n-1):
            a.append(a[i-1] + a[i])
    return a


n = input("Enter how many Fibonnaci sequence number you want to generate: ")
print(fibonnaci(n))
