def array(arr, n):

	if n == 1:
		print(0)

	x, y = 1, 1

	prod = [1 for x in range(n)]

	for x in range(n):
		prod[x] = y
		y *= arr[x]

	y = 1

	for x in range(n - 1, -1, -1):
		prod[x] *= y
		y *= arr[x]

	for x in range(n):
		print(prod[x], end=" ")


arr = [10, 3, 5, 6, 2]
n = len(arr)
array(arr, n)