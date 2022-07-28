def majority(arr, size):
	m = {}
	for x in range(size):
		if arr[x] in m:
			m[arr[x]] += 1
		else:
			m[arr[x]] = 1
	count = 0
	for key in m:
		if m[key] > size / 2:
			count = 1
			print(key)
			break
	if(count == 0):
		print("No Majority element")

arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
n = len(arr)

majority(arr, n)