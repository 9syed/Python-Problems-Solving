def threewaypartition(arr, n, lowVal, highVal):

	start = 0
	end = n - 1
	i = 0

	while i <= end:
		if arr[i] < lowVal:
			arr[i], arr[start] = arr[start], arr[i]
			i += 1
			start += 1

		elif arr[i] > highVal:
			arr[i], arr[end] = arr[end], arr[i]
			end -= 1

		else:
			i += 1

if __name__ == "__main__":
	arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
	n = len(arr)
	threewaypartition(arr, n, 10, 20)
	for i in range(n):
		print(arr[i], end = " ")