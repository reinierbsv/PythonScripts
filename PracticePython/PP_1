'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them
that tells them the year that they will turn 100 years old.

Extras:
Add on to the previous program by asking the user for another number and printing out that many copies of the
previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as
pressing the ENTER button)
'''
import datetime
name = input('Enter your name: ')
age = input('Enter your age: ')
date = datetime.datetime.now().strftime("%Y")
hyears = int(date) + (100 - int(age))
print(name, "you'll be 100 years old on", hyears)
repeat = input("Enter a number from 0 to 9: ")
for i in range(int(repeat)):
    print(name, "you'll be 100 years old on", hyears, "\n")
