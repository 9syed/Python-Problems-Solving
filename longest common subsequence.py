def subsequence(I, J, x, n):

	if x == 0 or n == 0:
		return 0
	elif I[x-1] == J[n-1]:
		return 1 + subsequence(I, J, x-1, n-1);
	else:
		return max(subsequence(I, J, x, n-1), subsequence(I, J, x-1, n));

I = "AGGTAB"
J = "GXTXAYB"
print ("Length of LCS is", subsequence(I , J, len(I), len(J)) )