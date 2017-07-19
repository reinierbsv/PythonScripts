"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock
"""
i = 1
while i == 1:
    ply_1 = input("Enter your choice: P:Paper or S:Scissors or R:Rock")
    ply_2 = input("Enter your choice: P:Paper or S:Scissors or R:Rock")
    if ply_1 == "P" and ply_2 == "R":
        print("Player 1 wins")
        ans = input("Would you like to play again, Y:Yes or N:No")
        if ans == "Y":
            i = 1
        else:
            i = 0
    elif ply_1 == "P" and ply_2 == "S":
        print("Player 2 wins")
        ans = input("Would you like to play again, Y:Yes or N:No")
        if ans == "Y":
            i = 1
        else:
            i = 0
    elif ply_1 == "R" and ply_2 == "P":
        print("Player 2 wins")
        ans = input("Would you like to play again, Y:Yes or N:No")
        if ans == "Y":
            i = 1
        else:
            i = 0
    elif ply_1 == "R" and ply_2 == "S":
        print("Player 1 wins")
        ans = input("Would you like to play again, Y:Yes or N:No")
        if ans == "Y":
            i = 1
        else:
            i = 0
    elif ply_1 == "S" and ply_2 == "P":
        print("Player 1 wins")
        ans = input("Would you like to play again, Y:Yes or N:No")
        if ans == "Y":
            i = 1
        else:
            i = 0
    elif ply_1 == "S" and ply_2 == "R":
        print("Player 2 wins")
        ans = input("Would you like to play again, Y:Yes or N:No")
        if ans == "Y":
            i = 1
        else:
            i = 0
    else:
        print("Null game")
        ans = input("Would you like to play again, Y:Yes or N:No")
        if ans == "Y":
            i = 1
        else:
            i = 0
