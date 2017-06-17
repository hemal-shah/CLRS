# First read the input file
fileObject = open("input.txt", "r+")
data = fileObject.read()
fileObject.close()

# Transform the data...
arr = list(map(int, data.split("\n")))
index = 1
# based on number of elements, make initial comparison
length = len(arr)

# Directly assign the first value as min_value and second_order_value
min_value = second_order_value = arr[0]

# Now, the iterations...
for i in range(index, length - 1, 2):

    if arr[i] < arr[i + 1]:
        if min_value > arr[i]:
            second_order_value = min_value
            min_value = arr[i]
            if second_order_value > arr[i + 1]:
                second_order_value = arr[i + 1]
    else:
        if min_value > arr[i + 1]:
            second_order_value = min_value
            min_value = arr[i + 1]
            if second_order_value > arr[i]:
                second_order_value = arr[i]

print("Minimum value =  ", min_value)
print("Second Order Value = ", second_order_value)
