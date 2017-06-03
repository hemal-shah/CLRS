# First reading the data.
fileObject = open("input.txt", "r+")
data = fileObject.read()

# Close the file.
fileObject.close()

A = list(map(int, data.split("\n")))
B = [None] * len(A)


def print_array(arr, start, end):
    """
    A helper method to print any provided list from start to end.
    :param arr: array to print
    :param start: starting index
    :param end: fixated index
    :return: 
    """
    print(arr[start:(end + 1)])


def get_max_value(arr):
    """
    Gets the maximum value out of an list.
    :param arr: list
    :return: maximum value in the list.
    """
    max_value = -1
    for i in arr:
        if i > max_value:
            max_value = i
    return max_value


def counting_sort(A, B, k):
    C = list()
    for i in range(0, k + 1):
        C.append(0)

    for j in range(0, len(A)):
        C[A[j]] = C[A[j]] + 1

    for k in range(1, k + 1):
        C[k] = C[k] + C[k - 1]

    for l in range(len(A) - 1, -1, -1):
        B[C[A[l]] - 1] = A[l]
        C[A[l]] = C[A[l]] - 1

    return B


B = counting_sort(A, B, get_max_value(A))
print_array(B, 0, len(A))
