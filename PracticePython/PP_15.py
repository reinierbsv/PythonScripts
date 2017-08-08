"""
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order. For example,
say I type the string:
  My name is Michele
Then I would see the string:
  Michele is name My
shown back to me.
"""


def reverseWords(w):
    A = w.split(' ')
    B = []
    for i in range(len(A)):
        B.append(A[-i-1])
    return(B)

w = input("Enter a phrase: ")
print(reverseWords(w))
