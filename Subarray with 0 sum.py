def subarr(arr, n):
	sum = 0
	s = set()

	for i in range(n):
		sum += arr[i]
		if sum == 0 or sum in s:
			return True
		s.add(sum)

	return False


arr = [4, 2, -3, 1, 6]
n = len(arr)
if subarr(arr, n) == True:
	print("Found a sunbarray with sum 0")
else:
	print("No Such sub array exits!")