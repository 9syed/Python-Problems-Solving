from collections import defaultdict

def anagrams(words):
	collectionwords = defaultdict(list)

	for word in words:
		collectionwords["".join(sorted(word))].append(word)

	for group in collectionwords.values(): 
		print(" ".join(group))

if __name__ == "__main__":
	arr = ['abc', 'def', 'fed', 'cab', 'bca']
	anagrams(arr)