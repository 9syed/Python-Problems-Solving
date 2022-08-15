def prefix(x):	
	size = len(x)
	if (size == 0):
		return ""

	if (size == 1):
		return x[0]

	x.sort()
	end = min(len(x[0]), len(x[size - 1]))

	i = 0
	while (i < end and
		x[0][i] == x[size - 1][i]):
		i += 1

	pre = x[0][0: i]
	return pre

if __name__ == "__main__":
	input = ["apple", "ape", "april"]
	print(prefix(input))