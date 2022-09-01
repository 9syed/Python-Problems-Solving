def stocks(prices, n):
	buy = prices[0]
	max_profit = 0

	for x in range(1, n):
		if (buy > prices[x]):
			buy = prices[x]

		elif (prices[x] - buy > max_profit):
			max_profit = prices[x] - buy;
	return max_profit;

if __name__=='__main__':
	prices = [ 7, 1, 5, 6, 4 ];
	n = len(prices)
	max_profit = stocks(prices, n);
	print(max_profit)