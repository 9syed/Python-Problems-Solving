def fixedpoint(arr, n):
	for i in range(n):
		if arr[i] is i:
			return i
	return -1

arr = [15, 2, 45, 12, 7]
n = len(arr)
print(str(fixedpoint(arr, n)))