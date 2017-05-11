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
    length = len(A)
    # Checking for equal dimensions of a and b
    assert type(A) == list and type(B) == list
    assert len(A) == len(A[0]) == len(B) == len(B[0])
    ANS = [ [0 for j in xrange(0, length)] for i in xrange(0, length) ]
    for i in xrange(0, length):
        for j in xrange(0, length):
            for k in xrange(0, length):
                ANS[i][j] = ANS[i][j] + A[i][k] * B[k][j]
                
    return ANS


input1 = open("matrix_input1.txt", "r")
A = map(int, input1.read().split("\n"))
input1.close()

input2 = open("matrix_input2.txt", "r")
B= map(int, input2.read().split("\n"))
input2.close()

rows_a = int(len(A)**0.5)
rows_b = int(len(B)**0.5)

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


def findNextPower(input):
    from math import ceil, log
    base = ceil(log(input, 2))
    # print("Returning : ", int(2**base))
    return int(2**base)


def stresson(A, B):
    row_count = len(A)
    
    if row_count <= 2:
        return simple_matrix_multiplication(A, B)
    else:
        half_count = row_count/2
        
        # Initialize submatrices and their respective values from original matrix
        a11 = [[0 for i in xrange(0, half_count)] for j in xrange(0, half_count)] 
        a12 = [[0 for i in xrange(0, half_count)] for j in xrange(0, half_count)]
        a21 = [[0 for i in xrange(0, half_count)] for j in xrange(0, half_count)]
        a22 = [[0 for i in xrange(0, half_count)] for j in xrange(0, half_count)]
        b11 = [[0 for i in xrange(0, half_count)] for j in xrange(0, half_count)]
        b12 = [[0 for i in xrange(0, half_count)] for j in xrange(0, half_count)]
        b21 = [[0 for i in xrange(0, half_count)] for j in xrange(0, half_count)]
        b22 = [[0 for i in xrange(0, half_count)] for j in xrange(0, half_count)]
        temp1 = [[0 for i in xrange(0, half_count)] for j in xrange(0, half_count)]
        temp2 = [[0 for i in xrange(0, half_count)] for j in xrange(0, half_count)]
        
        for i in xrange(0, half_count):
            for j in xrange(0, half_count):
                a11[i][j] = A[i][j]
                b11[i][j] = B[i][j]
                
                a12[i][j] = A[i][j + half_count]
                b12[i][j] = B[i][j + half_count]
                
                a21[i][j] = A[i + half_count][j]
                b21[i][j] = B[i + half_count][j]
                
                a22[i][j] = A[i + half_count][j + half_count]
                b22[i][j] = B[i + half_count][j + half_count] 
    
        # Calulating Si where i goes from 1 to 10
        S1 = diffMatrix(b12, b22)
        S2 = addMatrix(a11, a12)
        S3 = addMatrix(a21, a22)
        S4 = diffMatrix(b21, b11)
        S5 = addMatrix(a11, a22)
        S6 = addMatrix(b11, b22)
        S7 = diffMatrix(a12, a22)
        S8 = addMatrix(b21, b22)
        S9 = diffMatrix(a11, a21)
        S10 = addMatrix(b11, b12)
        
        # Calculating Pi where i is from 1 to 7
        P1 = stresson(a11, S1)
        P2 = stresson(S2, b22)
        P3 = stresson(S3, b11)
        P4 = stresson(a22, S4)
        P5 = stresson(S5, S6)
        P6 = stresson(S7, S8)
        P7 = stresson(S9, S10)
        
        # printMatrix(P1)
        # printMatrix(P2)
        # printMatrix(P3)
        # printMatrix(P4)
        # printMatrix(P5)
        # printMatrix(P6)
        # printMatrix(P7)
        # 
        # Calculating c11, c12, c21, c22
        c11 = c12 = c21 = c22 = [[0 for i in xrange(0, half_count)] for j in xrange(0, half_count)]
        temp1 = addMatrix(P5, P4)
        temp2 = diffMatrix(temp1, P2)
        c11 = addMatrix(temp2, P6)
        
        c12 = addMatrix(P1, P2)
        c21 = addMatrix(P3, P4)
        
        temp1 = addMatrix(P5, P1)
        temp2 = diffMatrix(temp1, P3)
        c22 = diffMatrix(temp2, P7)
        
        # printMatrix(c11)
        # printMatrix(c12)
        # printMatrix(c21)
        # printMatrix(c22)
        # 
        # Now combine these c submatrices into one matrix which is ANS
        ANS = [ [0 for i in xrange(0, row_count)] for j in xrange(0, row_count)]
        for i in xrange(0, half_count):
            for j in xrange(0, half_count):
                ANS[i][j] = c11[i][j]
                ANS[i+half_count][j] = c21[i][j]
                ANS[i][j+half_count] = c12[i][j]
                ANS[i+half_count][j+half_count] = c22[i][j]
        
        return ANS
        

def stresson_multiplication(A, B):
    n = len(A)
    new_n = findNextPower(n)
    newA = [ [0 for i in xrange(0, new_n) ] for j in xrange(0, new_n) ]
    newB = [ [0 for i in xrange(0, new_n) ] for j in xrange(0, new_n) ]
    for i in xrange(0, n):
        for j in xrange(0, n):
            newA[i][j] = A[i][j]
            newB[i][j] = B[i][j]
    # printMatrix(newA)
    # printMatrix(newB)
            
    C = stresson(newA, newB)
    # printMatrix(C)
    ANS = [[0 for i in xrange(0, n)] for j in xrange(0, n)]
    for i in xrange(0, n):
        for j in xrange(0, n):
            ANS[i][j] = C[i][j]
            
    return ANS
    

C = stresson_multiplication(A, B)
printMatrix(C)