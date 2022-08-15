def rearrange(x):

	freq = dict()
	max_freq = 0
	for j in range(len(x)):
		freq[x[j]] = freq.get(x[j], 0) + 1
		if (freq[x[j]] > max_freq):
			max_freq = freq[x[j]]

	if (max_freq <= (len(x) - max_freq + 1)):
		return True

x = "geekforgeeks"
if rearrange(x):
	print("Yes")
else:
	print("No")