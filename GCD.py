print "Enter the two numbers for witch you want to find the Greatest Common Divisor"
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
A, B, C = [], [], []
for x in range(1, num1):
    if num1 % x == 0:
        A.append(x)
for y in range(1, num2):
    if num2 % y == 0:
        B.append(y)
C = [a for a in A if a in B]
print "The GCD is for", num1, "and", num2,"is:", C[-1]
