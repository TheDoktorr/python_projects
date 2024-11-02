import math

def matrixmult(A,B):
    
    arow = len(A)
    brow = len(B)
    acol = len(A[0])
    bcol = len(B[0])

    if acol != brow:
        raise ValueError("Cannot multiply the two matrices A and B. Number of columns in A is not equal to the number of rows in B")
    if acol == arow:
        return True
    else:
        raise ValueError("check dimensions!")
    if bcol == brow:
        return True
    else:
        raise ValueError("check dimensions!")
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


        # Test 1: Matrices cannot be multiplied
    try:
        A = [[1, 2], [3, 4]]  # 2x2 matrix
        B = [[5, 6, 7]]       # 1x3 matrix
        matrixmult(A, B)
    except ValueError as e:
        assert str(e) == "Cannot multiply the two matrices A and B. Number of columns in A is not equal to the number of rows in B", "Test 1 failed: Incorrect ValueError message"
    else:
        assert False, "Test 1 failed: ValueError not raised"

    # Test 2: Matrices are not rectangular - matrix A
    try:
        A = [[1, 2, 3], [4, 5]]  # Non-rectangular matrix
        B = [[1, 2], [3, 4], [5, 6]]  # 3x2 matrix
        matrixmult(A, B)
    except ValueError as e:
        assert "not rectangular" in str(e), "Test 2 failed: Incorrect ValueError message for non-rectangular matrix"
    else:
        assert False, "Test 2 failed: ValueError not raised for non-rectangular matrix"

    # Test 3: Matrices are not rectangular - matrix B
    try:
        A = [[1, 2], [3, 4]]  # 2x2 matrix
        B = [[1, 2, 3], [4]]  # Non-rectangular matrix
        matrixmult(A, B)
    except ValueError as e:
        assert "not rectangular" in str(e), "Test 3 failed: Incorrect ValueError message for non-rectangular matrix"
    else:
        assert False, "Test 3 failed: ValueError not raised for non-rectangular matrix"

    # Test 4: Valid multiplication
    try:
        A = [[1, 2, 3], [4, 5, 6]]  # 2x3 matrix
        B = [[7, 8], [9, 10], [11, 12]]  # 3x2 matrix
        result = matrixmult(A, B)
        expected_result = [[58, 64], [139, 154]]  # Expected multiplication result
        assert result == expected_result, "Test 4 failed: Incorrect multiplication result"
    except ValueError:
        assert False, "Test 4 failed: ValueError raised unexpectedly for valid multiplication"

    print("All tests passed!")