#Find Subarray with Given Sum
def subarray_sum(arr, target):
    start = 0
    curr_sum = 0
    
    for end in range(len(arr)):
        curr_sum += arr[end]
        
        while curr_sum > target:
            curr_sum -= arr[start]
            start += 1
        
        if curr_sum == target:
            return arr[start:end+1]
    
    return -1