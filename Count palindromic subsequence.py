def count(str):

	n = len(str)
	abc = [[0 for i in range(n + 2)]for j in range(n + 2)]

	for i in range(n):
		abc[i][i] = 1
	for l in range(2, n + 1):

		for i in range(n):
			k = l + i - 1
			if (k < n):
				if (str[i] == str[k]):
					abc[i][k] = (abc[i][k - 1] +
								abc[i + 1][k] + 1)
				else:
					abc[i][k] = (abc[i][k - 1] +
								abc[i + 1][k] -
								abc[i + 1][k - 1])

	return abc[0][n - 1]

str = "abcd"
print("Total palindromic subsequence are:", count(str))