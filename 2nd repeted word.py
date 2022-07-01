def repeated(seq):
	
	x = {}
	for i in range(len(seq)):
		x[seq[i]] = x.get(seq[i], 0) + 1

	# Find the second largest occurrence
	first_max = -10**8
	sec_max = -10**8

	for it in x:
		if (x[it] > first_max):
			sec_max = first_max
			first_max = x[it]
			
		elif (x[it] > sec_max and
			x[it] != first_max):
			sec_max = x[it]

	for it in x:
		if (x[it] == sec_max):
			return it

if __name__ == '__main__':
	
	seq = [ "ccc", "aaa", "ccc",
			"ddd", "aaa", "aaa" ]
	print(repeated(seq))