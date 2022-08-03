def median(arr, n):

	sorted(arr)

	if n % 2 != 0:
		return int(arr[n // 2])
	
	return int((arr[int((n-1)/2)] +
				arr[int(n / 2)])/2)

arr = [ 56, 67, 30, 79]
n = len(arr)
print(median(arr, n))
