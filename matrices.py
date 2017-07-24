def mult_matrix(__name1__, __name2__):
    C, D = [], []
    (i, j, k) = (0, 0, 0)
    Alen = len(__name1__[0][:])
    Blen = len(__name2__)
    if Alen == Blen:
        for k in range(len(__name1__)):
            for j in range(len(__name1__[0][:])):
                for i in range(len(__name2__)):
                    C.append(__name1__[k][i] * __name2__[i][j])
                D.append(sum(C))
        D = [D[x:x + len(__name2__)] for x in range(0, len(D), len(__name2__))]
        print "matrix 1 by matrix 2 is equal to: ", D
    else:
        print"Matrices cannot be multiplies", "Please enter new matrices"
        __name1__ = input("Enter matrix 1: ")
        __name2__ = input("Enter matrix 2: ")
        mult_matrix(__name1__, __name2__)

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mult_matrix(x, y)
