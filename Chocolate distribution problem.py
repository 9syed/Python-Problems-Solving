def diff(arr, a, b):

	if (b==0 or a==0):
		return 0

	arr.sort()
	if (a < b):
		return -1
	min_diff = arr[a-1] - arr[0]

	for i in range(len(arr) - b + 1):
		min_diff = min(min_diff , arr[i + b - 1] - arr[i])

	return min_diff

arr = [7, 3, 2, 4, 9, 12, 56]
b = 3
a = len(arr)
print("Minimum difference is", diff(arr, a, b))