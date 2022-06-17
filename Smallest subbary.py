def smallestsub(arr, n, x):

    min_len = n + 1
    for start in range(0,n):
        curr_sum = arr[start]
 
        if (curr_sum > x):
            return 1
 
        for end in range(start+1,n):

            curr_sum += arr[end]
 
            if curr_sum > x and (end - start + 1) < min_len:
                min_len = (end - start + 1)
         
    return min_len;

arr1 = [1, 4, 45, 6, 10, 19]
x = 51
n1 = len(arr1)
b = smallestsub(arr1, n1, x);
if b == n1+1:
    print("Not possible")
else:
    print(b)
 
arr2 = [1, 10, 5, 2, 7]
n2 = len(arr2)
x = 9
c = smallestsub(arr2, n2, x);
if c == n2+1:
    print("Not possible")
else:
    print(c)
 
arr3 = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
n3 = len(arr3)
x = 280
a = smallestsub(arr3, n3, x)
if a == n3+1:
    print("Not possible")
else:
    print(a)