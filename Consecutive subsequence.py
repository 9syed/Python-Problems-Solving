def conseq(array, n):
     
    ans = 0
    count = 0
    array.sort()
    x = []
    x.append(array[0])

    for i in range(1, n):
        if (array[i] != array[i - 1]):
            x.append(array[i])

    for i in range(len(x)):
        if (i > 0 and x[i] == x[i - 1] + 1):
            count += 1
        else:
            count = 1
        ans = max(ans, count)

    return ans

arr = [ 1, 2, 2, 3 ]
n = len(arr)
print("Length of the Longest contiguous subsequence is",
       conseq(arr, n))