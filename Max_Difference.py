#Find Maximum Difference (j > i)
def max_difference(arr):
    min_element = arr[0]
    max_diff = arr[1] - arr[0]
    
    for i in range(1, len(arr)):
        max_diff = max(max_diff, arr[i] - min_element)
        min_element = min(min_element, arr[i])
    
    return max_diff