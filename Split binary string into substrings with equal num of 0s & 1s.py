def substring(str, n):
	
	count0 = 0
	count1 = 0
	count2 = 0
	
	for i in range(n):
		if str[i] == '0':
			count0 += 1
		else:
			count1 += 1
		if count0 == count1:
			count2 += 1

	if count0 != count1:
		return -1
			
	return count2

str = "0100110101"
n = len(str)
print(substring(str, n))