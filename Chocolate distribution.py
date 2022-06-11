def diff(arr, x, y):

	if (y==0 or x==0):
		return 0

	arr.sort()
	if (x < y):
		return -1
	min_diff = arr[x-1] - arr[0]

	for i in range(len(arr) - y + 1):
		min_diff = min(min_diff , arr[i + y - 1] - arr[i])

	return min_diff

if __name__ == "__main__":
	arr = [3, 4, 1, 9, 56, 7, 9, 12]
	y = 5
	x = len(arr)
	print("Minimum difference is", diff(arr, x, y))