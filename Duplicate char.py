from collections import defaultdict

def dups(str):

	count = defaultdict(int)
	for x in range(len(str)):
		count[str[x]] += 1

	for z in count:
		if (count[z] > 1):
			print(z, ", count = ", count[z])

if __name__ == "__main__":

	str = "geeksforgeeks"
	dups(str)