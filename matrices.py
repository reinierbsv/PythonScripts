A = [[1, 2, 3], [4, 5, 6]]
B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
C = []
D = []
i = 0
Alen = len(A[0][:])
Blen = len(B)
if Alen == Blen:
    for k in range(len(A)):
        for j in range(len(A[0][:])):
            for i in range(len(B)):
                C.append(A[k][i] * B[i][j])
            D.append(sum(C))
    D = [D[x:x + len(B)] for x in range(0, len(D), len(B))]
    print D
else:
    input("The matrices cannot being multiplies")
