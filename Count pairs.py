arr = [1, 5, 7, -1, 5]
m = len(arr)
sum = 6

def pairs(arr, m, sum):
    count = 0
    
    for x in range(0, m):
        for y in range(x + 1, m):
            if arr[x] + arr[y] == sum:
                count += 1

    return count

print("Pairs with sum 6 are:", pairs(arr, m, sum))