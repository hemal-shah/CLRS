# First take the input
fileObject = open("word_input.txt", "r+")
data = fileObject.read()
fileObject.close()

words = data.split("\n")
# Assure that length of each word is same.
length = len(words[0])

for word in words:
    if len(word) != length:
        print("All the words are not of same length")
        exit(1)


def counting_sort(words_array, index):
    # No need to get the maximum value in form of k, as there can be max 26 characters.
    B = [None] * len(words_array)
    C = list()

    for _ in range(0, 26):
        C.append(0)

    for ii in range(0, len(words_array)):
        C[ord(words_array[ii][index]) - 65] += 1

    for j in range(1, len(C)):
        C[j] += C[j - 1]

    for k in range(len(words_array) - 1, -1, -1):
        B[C[ord(words_array[k][index]) - 65] - 1] = words_array[k]
        C[ord(words_array[k][index]) - 65] -= 1
    return B


for i in range(length - 1, -1, -1):
    # perform a stable sort here..
    # We use counting sort.
    words = counting_sort(words, i)

print(words)
