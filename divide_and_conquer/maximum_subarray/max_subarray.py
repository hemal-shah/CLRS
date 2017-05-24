A = list()

#Reading the data first!
fileObject = open("input.txt", "r+")

data = fileObject.read()
fileObject.close()

A = map(int, data.split("\n"))

def print_subarray(low, high):
    print A[low : high + 1]


def find_max_crossing_subarray(low, mid, high):

    # print "Got the subarray :"
    # print_subarray(low, high)

    left_sum = -200000
    sum = 0
    max_left = -1
    for i in xrange(mid, low, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = -200000
    sum = 0
    max_right = -1
    for j in range(mid + 1, high + 1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, (left_sum + right_sum)

def find_max_subarray(low, high):
    if low == high:
        return low, high, A[low]

    else :
        mid = int((low + high) / 2)
        # print "%d\t%d\t%d"%(low, mid, high)
        left_low, left_high, left_sum = find_max_subarray(low, mid)
        right_low, right_high, right_sum = find_max_subarray(mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else :
            return cross_low, cross_high, cross_sum

# print "Low\tMid\tHigh"

low, high, sum = find_max_subarray(0, len(A) - 1)

print "What we got is :"
print "Low Index = ", low
print "High Index = ", high
print "Max sum = ", sum
