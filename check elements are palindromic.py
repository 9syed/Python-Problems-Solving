def palindrome(N):
	str1 = "" + str(N)
	len1 = len(str1)
	for i in range(int(len1 / 2)):
		if (str1[i] != str1[len1 - 1 - i]):
			return False
	return True

def palin(arr, n):
	
	for i in range(n):
		ans = palindrome(arr[i])
		if (ans == False):
			return False
	return True
	
if __name__ == '__main__':
	
	arr = [ 121, 131, 20 ]
	
	n = len(arr)
	res = palin(arr, n)
	if (res == True):
		print("Array is a PalinArray")
	else:
		print("Array is not a PalinArray")