"""
    This program implements the stresson's algorithm for matrix multiplication.
    The inputted matrix should be square matrix only (n x n) format only.
"""

from __future__ import print_function

def printMatrix(A):
    """
        Prints the matrix that is supplied to the function.
    """
    assert type(A) == list
    print("----------------")
    for row in A:
        print("\t".join(map(str, row)))


def addMatrix(A, B):
    """
        To add two matrices
    """
    C = [[0 for j in xrange(len(A))] for i in xrange(len(B))]
    for i in xrange(len(A)):
        for j in xrange(len(B)):
            C[i][j] = A[i][j] + B[i][j]
    return C

def diffMatrix(A, B):
    """
        To find difference between two matrices.
    """
    C = [[0 for j in xrange(len(A))] for i in xrange(len(B))]
    for i in xrange(len(A)):
        for j in xrange(len(B)):
            C[i][j] = A[i][j] - B[i][j]

    return C
    
    
def simple_matrix_multiplication(A, B):
    """
        Performs simple straightforward ijk matrix multiplication
        for base cases in stressons recursion
    """
    
    # Checking for equal dimensions of a and b
    assert type(A) == list and type(B) == list
    assert len(A) == len(A[0]) == len(B) == len(B[0])
    ANS = [ [0 for j in xrange(0, len(B))] for i in xrange(0, len(A)) ]
    printMatrix(ANS)
    for i in xrange(0, len(A)):
        for j in xrange(0, len(B)):
            for k in xrange(0, len(A)):
                ANS[i][j] = ANS[i][j] + A[i][k] + B[k][j]

    return ANS


input1 = open("matrix_input1.txt", "r")
A = map(int, input1.read().split("\n"))
input1.close()

input2 = open("matrix_input2.txt", "r")
B= map(int, input2.read().split("\n"))
input2.close()

rows_a = int(len(A)**0.5)
rows_b = int(len(B) ** 0.5)

# Checking for errors in input here.
# Checking if matrix a is square
if len(A) % rows_a != 0:
    raise ValueError("Matrix A is not square matrix")

# checking if matrix b is square
if len(B) % rows_b != 0:
    raise ValueError("Matrix B is not square matrix")

# checking if both matrix have same number of elements
# we can do this by comparing number of rows, as both are square matrix
if rows_a != rows_b:
    raise ValueError("Both the matrix should have equal number of elements.")

# Converting the input matrix into a more manageable form.
A = [A[i : i + rows_a] for i in xrange(0, len(A), rows_a)]
B = [B[i : i + rows_b] for i in xrange(0, len(B), rows_b)]
printMatrix(A)
printMatrix(B)




def stresson_multiplication(A, B):
    
    pass
    
C = simple_matrix_multiplication(A, B)
printMatrix(C)