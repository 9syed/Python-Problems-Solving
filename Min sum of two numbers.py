def minsum(arr, x):
	arr.sort()
	a = 0
	b = 0

	for i in range(x):
		if (i % 2 != 0):
			a = a * 10 + arr[i]
		else:
			b = b * 10 + arr[i]

	return a + b

arr = [5, 3, 0, 7, 4]
x = len(arr)
print(minsum(arr, x))