def elements(arr, n, k) :
	x = n // k
	
	freq = {}

	for i in range(n) :	
		if arr[i] in freq :
			freq[arr[i]] += 1
		else :
			freq[arr[i]] = 1

	for i in freq :
		
		if (freq[i] > x) :
			
			print(i)

arr = [3, 1, 2, 2, 1, 2, 3, 3]
n = len(arr)
k = 4

elements(arr, n, k)