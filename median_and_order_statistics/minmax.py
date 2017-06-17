# First read the input file
fileObject = open("input.txt", "r+")
data = fileObject.read()
fileObject.close()

# Transform the data...
arr = list(map(int, data.split("\n")))

min_value = -1
max_value = -1
index = -1
# based on number of elements, make initial comparison
length = len(arr)
if length % 2 == 0:
    # Even, hence compare first two elements and then assign to min and max
    if arr[0] < arr[1]:
        min_value = arr[0]
        max_value = arr[1]
    else:
        min_value = arr[1]
        max_value = arr[0]
    index = 2
else:
    # Odd, assign first value to both...
    min_value = max_value = arr[0]
    index = 1

# Now, the iterations...
for i in range(index, length - 1, 2):
    if arr[i] < arr[i + 1]:
        if min_value > arr[i]:
            min_value = arr[i]
        if max_value < arr[i + 1]:
            max_value = arr[i + 1]
    else:
        if min_value > arr[i + 1]:
            min_value = arr[i + 1]
        if max_value < arr[i]:
            max_value = arr[i]

print("Maximum value = ", max_value)
print("Minimum value =  ", min_value)   