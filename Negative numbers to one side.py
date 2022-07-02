def negative(arr):
    arr.sort()

arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
negative(arr)
for x in arr:
    print(x, end = " ")