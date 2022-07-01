def rotations(str1, str2):
	s1 = len(str1)
	s2 = len(str2)
	t = ''

	if s1 != s2:
		return 0

	t = str1 + str1

	if (t.count(str2)> 0):
		return 1
	else:
		return 0

str1 = "AACD"
str2 = "ACDA"

if rotations(str1, str2):
	print ("Strings are rotations of each other")
else:
	print ("Strings are not rotations of each other")