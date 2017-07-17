'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
'''
num = input("Enter the number for witch you want to find the divisors: ")
num = int(num)
A = []
for x in range(2, num):
    if num % x == 0:
        A.append(x)
print(A)
