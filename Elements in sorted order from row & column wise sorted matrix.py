def matrix(y, mat):
	x = []

	for i in range(0, y):
		for j in range(0, y):
			x.append(mat[i][j])

	x.sort()

	for i in range(len(x)):
		print(x[i], end=' ')


if __name__ == "__main__":
	y = 4
	mat = [[10, 20, 30, 40], [15, 25, 35, 45],
		   [27, 29, 37, 48], [32, 33, 39, 50]]
	matrix(y, list(mat))