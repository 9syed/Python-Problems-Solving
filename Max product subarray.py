def maxproduct(arr, x):

	max_ending = arr[0]
	min_ending = arr[0]
	max_far = arr[0]

	for i in range(1, x):
		temp = max(max(arr[i], arr[i] * max_ending), arr[i] * min_ending)
		min_ending = min(min(arr[i], arr[i] * max_ending), arr[i] * min_ending)
		max_ending = temp
		max_far = max(max_far, max_ending)
	
	return max_far

arr = [6, -3, -10, 0, 2]
x = len(arr)
print(f"Maximum Sub array product is {maxproduct(arr, x)}")