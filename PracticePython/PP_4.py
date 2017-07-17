
num = input("Enter the number for witch you want to find the divisors: ")
A = []
for x in range(2, num):
    if num % x == 0:
        A.append(x)
print(A)
