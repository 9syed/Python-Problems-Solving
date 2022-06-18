a = set()

def str_subsequence(str):
	for x in range(len(str)):

		for j in range(len(str),x,-1):
			str_sub = str[x: x+j]
			a.add(str_sub)

			for y in range(1,len(str_sub)):
				sb = str_sub

				sb = sb.replace(sb[y],"")
				str_subsequence(sb)

s = "aabc"
str_subsequence(s)
for x in a:
	print(x, end = ", ")
print()