arr = [7, 10, 4, 3, 20, 15]
n = len(arr)
k = 3

s = set(arr)

for itr in s:
    if k == 1:
        print(itr)
        break
    k -= 1