def AP(arr, n):
	if (n == 1):
		return True

	arr.sort()
	x = arr[1] - arr[0]
	for i in range(2, n):
		if (arr[i] - arr[i-1] != x):
			return False

	return True

arr = [ 0, 12, 4, 8 ]
n = len(arr)
print("Yes") if(AP(arr, n)) else print("No")