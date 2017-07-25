a = input("Enter a 'string' to reverse: ")
b = list(a)
for i in range(len(a)):
    b[i] = a[(len(a)-1)-i]
    b[(len(a) - 1) - i] = a[i]
print(''.join(b))
