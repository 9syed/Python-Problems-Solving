def kth(arr, x, K):
	arr.sort()
	return arr[K-1]

arr = [7, 10, 4, 3, 20, 15]
x = len(arr)
K = 3

print(kth(arr, x, K))