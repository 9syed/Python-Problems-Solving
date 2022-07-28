def find4Numbers(a, n, X):

	a.sort()

	for i in range(n - 3):
		for j in range(i + 1, n - 2):
			l = j + 1
			r = n - 1

			while (l < r):
				if(a[i] + a[j] + a[l] + a[r] == X):
					print(a[i], ",", a[j], ",",
						a[l], ",", a[r])
					l += 1
					r -= 1

				elif (a[i] + a[j] + a[l] + a[r] < X):
					l += 1
				else:
					r -= 1

if __name__ == "__main__":
	a = [1, 4, 45, 6, 10, 12]
	X = 21
	n = len(a)
	find4Numbers(a, n, X)