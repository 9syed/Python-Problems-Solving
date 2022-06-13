num = [1, 3, 4, 2, 2]

arr_size = len(num)
for i in range(arr_size):

	x = num[i] % arr_size
	num[x] = num[x] + arr_size

print("The Duplicate number is ")
for i in range(arr_size):
	if (num[i] >= arr_size*2):
		print(i)