def matrix(x, y, z, k):
	l = 0
	r = y - 1
	mid = 0
	while (l <= r) :
		mid = int((l + r) / 2)
		
		if(k == x[mid][0]):
			print("Found at (" , mid , ",", "0)", sep = "")
			return
		
		if(k == x[mid][z - 1]):
			t = z - 1
			print("Found at (" , mid , ",", t , ")", sep = "")
			return
		if(k > x[mid][0] and k < x[mid][z - 1]):
			sortedmatrix(x, y, z, k, mid) 
			return
		if (k < x[mid][0]):
			r = mid - 1
		if (k > x[mid][z - 1]):
			l = mid + 1

def sortedmatrix(x, y, z, k,):
	
	l = 0
	r = z - 1
	mid = 0
	while (l <= r):
		mid = int((l + r) / 2)
		
		if (x[x][mid] == k):
			print("Found at (" , x , ",", mid , ")", sep = "")
			return
		if (x[x][mid] > k):
			r = mid - 1
		if (x[x][mid] < k):
			l = mid + 1
	
	print("Element not found")

y = 4
z = 5
x = [[1, 5, 9], [14, 20, 21], [30, 34, 43]]
k = 31
matrix(x, y, z, k)