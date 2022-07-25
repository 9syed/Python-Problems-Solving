def commonarray(arr, n, element):

	l,h = 0,n - 1
	while (l <= h):
		mid = (l + h) // 2
		if (arr[mid] == element):
			return True

		elif (arr[mid] > element):
			h = mid - 1

		else:
			l = mid + 1

	return False

def findCommon(a, b, c, n1, n2, n3):

	for j in range(n1):
		if (j != 0 and a[j] == a[j - 1]):
			continue
	
		if (commonarray(b, n2, a[j]) and commonarray(c, n3, a[j])):
			print(a[j],end=" ")

ar1 = [ 1, 5, 10, 20, 40, 80 ]
ar2 = [ 6, 7, 20, 80, 100 ]
ar3 = [ 3, 4, 15, 20, 30, 70, 80, 120 ]
n1 = len(ar1)
n2 = len(ar2)
n3 = len(ar3)

print("The Common Elements are:")
findCommon(ar1, ar2, ar3, n1, n2, n3)