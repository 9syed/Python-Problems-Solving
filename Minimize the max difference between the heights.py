def getMinDiff(arr, n, k):

	arr.sort()
	ans = arr[n - 1] - arr[0]
	x = arr[0]
	y = arr[n - 1]

	for i in range(1, n):
		if arr[i] < k:
			continue

		x = min(arr[0] + k, arr[i] - k)
		y = max(arr[i - 1] + k, arr[n - 1] - k)
		ans = min(ans, y - x)

	return ans

k = 6
n = 6
arr = [7, 4, 8, 8, 8, 9]
ans = getMinDiff(arr, n, k)
print(ans)