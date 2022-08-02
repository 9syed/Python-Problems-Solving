def unionintersection(a , n, b , m):
	x = {}
	
	for i in range(n):
		x[a[i]] = i

	for i in range(m):
		x[b[i]] = i
	print("The union set of both arrays is: ");

	for key in x.keys():
		print(key,end=" ")

a = [ 1, 2, 5, 6, 2, 3, 5 ];
b = [ 2, 4, 5, 6, 8, 9, 4, 6, 5 ];
	
unionintersection(a, 7, b, 9)