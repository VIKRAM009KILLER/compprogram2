# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    if len(m1[0]) != len(m2):
        return None

    r = len(m1)
    c = len(m2[0])

    new = []
    for i in range(r):
        rnew = []

        for j in range(c):
            rnew.append(0)
        new.append(rnew)

    for i in range(r):
        for j in range(c):
            for k in range(len(m2)):
                new[i][j] += m1[i][k] * m2[k][j]






    return new
