def triplet_no(x, arr_size, sum):

	x.sort()

	for i in range(0, arr_size-2):
		l = i + 1

		r = arr_size-1
		while (l < r):
		
			if( x[i] + x[l] + x[r] == sum):
				print("Triplet is", x[r], ',', x[l], ',', x[i]);
				return True
			
			elif (x[i] + x[l] + x[r] < sum):
				l += 1
			else:
				r -= 1

	return False

x = [12, 3, 4, 1, 6, 9]
sum = 24
arr_size = len(x)
triplet_no(x, arr_size, sum)