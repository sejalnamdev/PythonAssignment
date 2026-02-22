#Check if Array is Sorted
def is_sorted(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                return False
    return True