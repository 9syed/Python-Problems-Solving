def repeating():
	
	arr = [ 3, 1, 3 ]
	
	missing = {}
	
	max = len(arr)
	for i in arr:
		if not i in missing:
			missing[i] = True
			
		else:
			print("Repeating =", i)
	
	for i in range(1, max + 1):
		if not i in missing:
			print("Missing =", i)
repeating()