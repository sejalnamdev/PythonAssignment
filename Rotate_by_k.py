#Rotate Array by k Positions: Rotate the array to the right by k positions
def rotate_right(arr, k):
    n = len(arr)
    
    for _ in range(k):
        last = arr[-1]
        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = last
    
    return arr