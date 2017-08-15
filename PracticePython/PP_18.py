"""
Create a program that will play the “cows and bulls” game with the user. The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that
the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed
correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many
“cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track
of the number of guesses the user makes throughout teh game and tell the user at the end.
"""

import random as rd


def cowsAndBulls(str_guess, str_number):
    i = 0
    cows, bulls = 0, 0
    for i in range(4):
        if str_guess[i] in str_number:
            bulls += 1
            if str_guess[i] == str_number[i]:
                cows += 1
                bulls -= 1
    print("You have", cows, "cows and", bulls, "bulls")
    print("Guess again")

number = rd.randint(1000, 9999)
str_number = str(number)
print("Welcome to Cows and Bulls Game!")
print("Guess a 4 digit number")
guess = input("#:")
str_guess = str(guess)
counter = 1
while str_guess != str_number:
    counter += 1
    cowsAndBulls(str_guess, str_number)
    guess = input("#:")
    str_guess = str(guess)
else:
    print("You got it, it took you", counter, "attempts")
