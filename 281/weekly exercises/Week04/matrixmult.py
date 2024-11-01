import math

def matrixmult(A,B):

    arow = len(A)
    brow = len(B)
    acol = len(A[0])
    bcol = len(B[0])

    C = []

    for i in range(arow):
        crow = []
        for j in range(bcol):
            sum =0
            for k in range(acol):
                sum += A[i][k] * B[k][j]
            crow.append(sum)
        C.append(crow)
    return C


# no of rows given by nrows  = len(A)
# no of columns given by ncols = len(A[0])




A = [[4, 9, 3, 5],
     [6, 7, 3, 3],
     [2, 5, 4, 3]]
B=[[5, 2, 0],
   [6, 1, 4],
   [5, 5, 4],
   [7, 7, 2]]
print(matrixmult(A, B))