def negativeinteger(arr, x):
	index = 0

	for i in range(x - 1, len(arr)):
		while index < i and (index <= i - x or arr[index] >= 0):
			index += 1

		element = arr[index] if arr[index] < 0 else 0
		print(element, end=', ')

arr = [-8, 2, 3, -6, 10]
x = 2
negativeinteger(arr, x)