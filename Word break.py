def wordbreak(wb,word):

	size = len(word)
	if(size == 0):
		return True
	
	temp = ""
	for i in range(len(word)):
	
		temp += word[i]
		if(temp in wb and wordbreak(wb, word[i+1:])):
		
			return True
		
	return False

def breakproblem(words,word):

	start = 0
	wb = {}
	for it in words:
		wb[it] = True
	
	return "YES" if wordbreak(wb,word ) == True else "NO"

words = ["mobile","samsung","sam","sung",
		"man","mango","icecream","and",
		"go","i","like","ice","cream"]
word = "samsungandmangok"
print(breakproblem(words, word))