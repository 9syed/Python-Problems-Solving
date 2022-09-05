def element(arr, x):
	arr.sort(reverse = True)
	for i in range(x):
		print (arr[i], end =" ")

arr = [1, 23, 12, 9, 30, 2, 50]
x = 3
element(arr, x)