def rowmax( arr, low, high):
	if high >= low:
		
		mid = low + (high - low)//2

		if (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1:
			return mid

		elif arr[mid] == 0:
			return rowmax(arr, (mid + 1), high)
	
		else:
			return rowmax(arr, low, (mid - 1))
	return -1

def rowwithmax1s( mat):	
	R = len(mat)
	C = len(mat[0])
	max_row_index = 0
	max = -1
	
	for i in range(0, R):
		index = rowmax(mat[i], 0, C - 1)
		if index != -1 and C - index > max:
			max = C - index
			max_row_index = i

	return max_row_index

mat = [[0, 1, 1, 1],
       [0, 0, 1, 1],
	   [1, 1, 1, 1],
	   [0, 0, 0, 0]]
print (rowwithmax1s(mat))