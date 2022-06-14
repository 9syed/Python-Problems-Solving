arr1 = [ 11, 1, 13, 21, 3, 7 ]
arr2 = [ 11, 3, 7, 1 ]
x = len(arr1)
y = len(arr2)
z = set()
for i in range(x) :
	z.add(arr1[i])

p = len(z)
for i in range(y) :
	z.add(arr2[i])

if (len(z) == p) :
	print("Array2 is subset of array1")
else :
	print("Array2 is not subset of array1")