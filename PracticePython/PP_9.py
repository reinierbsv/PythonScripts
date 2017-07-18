'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then
tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user
input lessons from the very first exercise)

Extras:
Keep the game going until the user types exit
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''
import random
x = random.randint(1, 11)
print("On this game you have to guess which number between 1 and 9 I choose before")
print("If you want to end the game type 'exit'")
i = 1
c = 0
while i == 1:
    ans = input("Enter your guess: ")
    c = c + 1
    if ans == 'exit':
        i = 0
        print("God Bye!")
    elif ans < x:
        print("Too low")
    elif ans > x:
        print("Too high")
    else:
        print("You got it!!! It took you", c, "attempts")
        print("New game!!!")
        x = random.randint(1, 11)
