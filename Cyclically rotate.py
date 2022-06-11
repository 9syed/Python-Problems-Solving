def rotate(arr):
	arr[:] = arr[-1:]+arr[:-1]

arr = [1, 2, 3, 4, 5]
rotate(arr)

print("The rotated array is ", *arr)