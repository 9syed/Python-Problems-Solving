def heap(arr, i, N):
	l = 2 * i + 1
	r = 2 * i + 2
	largest = i
	if l < N and arr[l] > arr[i]:
		largest = l
	if r < N and arr[r] > arr[largest]:
		largest = r
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		heap(arr, largest, N)

def maxheap(arr, N):

	for i in range(int((N - 2) / 2), -1, -1):
		heap(arr, i, N)

def printArray(arr, size):
	for i in range(size):
		print(arr[i], end=" ")
	print()

if __name__ == '__main__':

	arr = [3, 4, 8, 11, 13]
	N = len(arr)
	print("Min Heap:")
	printArray(arr, N)
	maxheap(arr, N)

	print("Max Heap:")
	printArray(arr, N)