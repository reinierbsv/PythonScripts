"""
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten,
a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4
to help you. Take this opportunity to practice using functions
"""


def prime_number(num):
    a = []
    for x in range(2, num):
        if num % x == 0:
            a.append(x)
    if a == []:
        print (num, "IS a prime number")
    else:
        print (num, "IS NOT a prime number")

num = input("Enter the number you want to know if it is a 'prime number': ")
prime_number(num)
