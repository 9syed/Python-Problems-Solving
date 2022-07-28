def pairdifference(arr,n):

	size = len(arr)

	i,j = 0,1

	while i < size and j < size:

		if i != j and arr[j]-arr[i] == n:
			print("Pair found",arr[i],",",arr[j],)
			return True

		elif arr[j] - arr[i] < n:
			j+=1
		else:
			i+=1
	print("No pair found")
	return False

arr = [1, 8, 30, 40, 100]
n = 60
pairdifference(arr, n)