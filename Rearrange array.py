def rearrangearray(arr, n, outOfPlace, cur):
	temp = arr[cur]
	for i in range(cur, outOfPlace, -1):
		arr[i] = arr[i - 1]
	arr[outOfPlace] = temp
	return arr


def rearrange(arr, n):
	outOfPlace = -1
	for index in range(n):
		if(outOfPlace >= 0):

			if((arr[index] >= 0 and arr[outOfPlace] < 0) or
			(arr[index] < 0 and arr[outOfPlace] >= 0)):
				arr = rearrangearray(arr, n, outOfPlace, index)
				if(index-outOfPlace > 2):
					outOfPlace += 2
				else:
					outOfPlace = - 1

		if(outOfPlace == -1):

			if((arr[index] >= 0 and index % 2 == 0) or
			(arr[index] < 0 and index % 2 == 1)):
				outOfPlace = index
	return arr

arr = [1, 2, 3, -4, -1, 4]
print(rearrange(arr, len(arr)))