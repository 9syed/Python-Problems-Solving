def flip(ch):
	return '1' if (ch == '0') else '0'

def getflip(str, expected):

	flipCount = 0
	for i in range(len( str)):
		if (str[i] != expected):
			flipCount += 1

		expected = flip(expected)
	return flipCount

def minflip(str):
	return min(getflip(str, '0'),
			getflip(str, '1'))

if __name__ == "__main__":
	
	str = "000111000101010111"
	print(minflip(str))