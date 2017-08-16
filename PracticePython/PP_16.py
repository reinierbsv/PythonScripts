"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have
a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random,
generating a new password every time the user asks for a new password. Include your run-time code in a
main method.

Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""


import random as rd
import string


def passwordGenerator(seed):
    sym = '+-*/'
    if seed == 'w':
        return "".join(rd.choice(string.ascii_letters) for x in range(10))
    elif seed == 'm':
        return "".join(rd.choice(string.ascii_letters + string.digits) for x in range(10))
    else:
        return "".join(rd.choice(string.ascii_letters + string.digits + sym) for x in range(10))


seed = input("Select how strong you want your password. Weak 'w', Medium 'm', Strong 's': ")
print passwordGenerator(seed)
