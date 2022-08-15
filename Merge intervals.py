def merge(x):
	x.sort()
	y = []
	y.append(x[0])
	for i in x[1:]:
		if y[-1][0] <= i[0] <= y[-1][-1]:
			y[-1][-1] = max(y[-1][-1], i[-1])
		else:
			y.append(i)

	for i in range(len(y)):
		print(y[i], end=" ")

arr = [[1,3],[2,4],[6,8],[9,10]]
merge(arr)