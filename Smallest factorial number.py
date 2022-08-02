def factorial(x, y):

	temp = x
	count = 0
	f = 5
	while (f <= temp):
		count += temp//f
		f = f*5

	return (count >= y)

def smallestfactorial(y):

	if (y==1):
		return 5

	low = 0
	high = 5*y

	while (low <high):

		mid = (low + high) >> 1

		if (factorial(mid, y)):
			high = mid
		else:
			low = mid+1

	return low

y = 1
print(smallestfactorial(y))