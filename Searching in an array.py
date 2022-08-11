def search(arr, n, x, k):

	i = 0
	while (i < n):
		if (arr[i] == x):
			return i

		i = i + max(1, int(abs(arr[i] - x) / k))
	return -1

arr = [4, 5, 6, 7, 6]
x = 6
k = 1
n = len(arr)
print(search(arr, n, x, k))