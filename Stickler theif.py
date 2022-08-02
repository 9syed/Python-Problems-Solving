def theif(arr, n):

	if (n < 0):
		return 0

	if (n == 0):
		return arr[0]
	
	loot = arr[n] + theif(arr, n - 2)
	notlooted = theif(arr, n - 1)

	return max(loot, notlooted)

arr = [ 5, 5, 10, 100, 10, 5 ]
n = len(arr)
print(theif(arr, n - 1));