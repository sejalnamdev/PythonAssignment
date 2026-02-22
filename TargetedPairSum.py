#Find Pair with Given Sum: Find a pair of elements that adds up to a target sum
def find_pair(arr, target):
    n = len(arr)
    
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return arr[i], arr[j]
    
    return -1