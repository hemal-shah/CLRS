# 8.2-4, Pg. No. : 197
# Describe an algorithm that, given n integers in the range 0 to k, preprocesses its
# input and then answers any query about how many of the n integers fall into a
# range [a..b] in O(1) time. Your algorithm should use Big-theta(n + k) preprocessing
# time.
# CLRS Question solution

# First let's read the data
fileObject = open("input.txt", "r+")
data = fileObject.read()
fileObject.close()

# Take the data into suitable form
A = list(map(int, data.split("\n")))


def get_max_number(arr):
    max_number = -1
    for i in arr:
        if i > max_number:
            max_number = i

    return max_number


def modified_counting_sort(A, k):
    C = list()
    for i in range(0, k + 1):
        C.append(0)

    for j in range(0, len(A)):
        C[A[j]] = C[A[j]] + 1

    for k in range(1, k + 1):
        C[k] = C[k] + C[k - 1]

    # print(C)
    return C


C = modified_counting_sort(A, get_max_number(A))

data = input("Enter the range, separated by space:")
a, b = map(int, data.split(" "))

# make sure a and b satisfy the index range..
if not a < b and a > 0 and b < len(C):
    print("The range is not constrained.")
    exit(1)

ans = C[b] - C[a]
print(ans)
