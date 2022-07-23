def bracketbalance(y):
	
	swap = 0
	notbalance = 0;
	
	for x in y:
		if x == '[':
			notbalance -= 1
		else:
			notbalance += 1

			if notbalance > 0:
				swap += notbalance
	return swap

b = "[]][][";
print(bracketbalance(b))