#Find the First Missing Positive: Find the smallest positive integer missing in the array.
def first_missing_positive(arr):
    n = len(arr)
    
    for i in range(n):
        while 1 <= arr[i] <= n and arr[arr[i]-1] != arr[i]:
            correct = arr[i] - 1
            arr[i], arr[correct] = arr[correct], arr[i]
    
    for i in range(n):
        if arr[i] != i+1:
            return i+1
    
    return n+1