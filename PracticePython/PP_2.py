"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""
number = input("Enter a number: ")
if int(number) % 4 == 0:
    print("The number is multiple of 4")
    pass
else:
    if int(number) % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
num = input("Enter a number: ")
check = input("Enter another number: ")
if int(num) % int(check) == 0:
    print(num, "is a multiple of ", check)
else:
    print(num, "is not a multiple of ", check)
