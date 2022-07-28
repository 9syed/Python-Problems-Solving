def array(arr, x):
    first = arr.index(x)
    last = len(arr) - 1 - arr[::-1].index(x)
    print("First Occurrence =", first)
    print("Last Occurrence =", last)
        


arr = [ 1, 3, 5, 5, 5, 5, 67, 123, 125 ]
x = 5
array(arr, x);