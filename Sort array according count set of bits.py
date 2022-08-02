def bitcount(num):
	
	count = 0
	while (num):
		if (num & 1):
			count += 1
			
		num = num >> 1
		
	return count

def sortbybitcount(arr, n):

	count = []
	for i in range(n):
		count.append([(-1) *
		bitcount(arr[i]), arr[i]])
		
	count.sort(key = lambda x:x[0])
	
	for i in range(len(count)):
		print(count[i][1], end = " ")

arr = [ 5, 2, 3, 9, 4, 6, 7, 15, 32 ]
n = len(arr)
sortbybitcount(arr, n)