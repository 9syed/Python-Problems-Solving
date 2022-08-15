from functools import cmp_to_key
class Job:

	def __init__(self, start, finish, profit):

		self.start = start
		self.finish = finish
		self.profit = profit

def jobscheduling(s1, s2):

	return s1.finish < s2.finish

def latestNonConflict(arr, i):

	for j in range(i - 1, -1, -1):
		if arr[j].finish <= arr[i - 1].start:
			return j

	return -1

def profit(arr, n):

	arr = sorted(arr, key=cmp_to_key(jobscheduling))

	table = [None] * n
	table[0] = arr[0].profit

	for i in range(1, n):

		inclProf = arr[i].profit
		l = latestNonConflict(arr, i)

		if l != -1:
			inclProf += table[l]

		table[i] = max(inclProf, table[i - 1])
	result = table[n - 1]

	return result

values = [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]
arr = []
for i in values:
	arr.append(Job(i[0], i[1], i[2]))

n = len(arr)
print(profit(arr, n))