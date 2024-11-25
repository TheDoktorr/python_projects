import math

def matrixmult(A,B):
    """
    This function takes an input of two matricies and multiplies them by their individual indexes, and outputs the product as a new matrix. 

    """
    
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

A=[[1, 7, 1, 7, 7, 3, 4, 3, 2, 9],
       [4, 5, 1, 4, 8, 1, 1, 2, 2, 7],
       [6, 8, 3, 6, 1, 7, 6, 8, 6, 1],
       [6, 2, 4, 1, 3, 7, 5, 2, 1, 4],
       [2, 8, 7, 0, 0, 5, 0, 5, 2, 4]]
B=[[6, 1, 1],
       [1, 4, 9],
       [8, 5, 4],
       [5, 1, 3],
       [1, 8, 3],
       [7, 1, 7],
       [3, 7, 5],
       [4, 8, 2],
       [4, 8, 3],
       [0, 4, 5]]
try:
    C = matrixmult(B, A)
except ValueError as inst:
    print("Caught ValueError")
    print("You have thrown the right type of error")

if matrixmult.__doc__ is not None:
    print("Hooray! You have a docstring!") 