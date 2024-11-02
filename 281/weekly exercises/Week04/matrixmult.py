import math

def matrixmult(A,B):
    
    arow = len(A)
    brow = len(B)
    acol = len(A[0])
    bcol = len(B[0])

    if acol != brow:
        raise ValueError("Cannot multiply the two matrices A and B. Number of columns in A is not equal to the number of rows in B")

    for row in A:
        if len(row) != len(A[0]):
            raise ValueError("matrix is not rectuangular")
    for row in B:
        if len(row) != len(B[0]):
            raise ValueError("matrix is not rectuangular")
   # if not all(len(row) == len(A[0]) for row in A):
   #         raise ValueError("this is not rectuangular")


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


import math 
x = math.pi / 2
A = [[math.cos(x), -math.sin(x)], [math.sin(x), math.cos(x)]]
B = [[1], [0, 0]]
try:
    C = matrixmult(A, B)
except ValueError as inst:
    print("Caught ValueError")
    print("You have thrown the right type of error")
