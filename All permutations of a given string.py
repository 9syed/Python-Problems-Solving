def permute_string(List):
	return ''.join(List)

def permute(x, y, z):
	if y==z:
		print (permute_string(x))
	else:
		for i in range(y,z):
			x[y], x[i] = x[i], x[y]
			permute(x, y+1, z)
			x[y], x[i] = x[i], x[y]

string = "ABC"
n = len(string)
x = list(string)
permute(x, 0, n)