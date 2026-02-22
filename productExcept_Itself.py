#Product of Array Except Self
#Given an array, return a new array where each element is the product of all elements except itself.
#Do not use division.
def product_except_self(arr):
    n = len(arr)
    result = [1]*n
    
    left = 1
    for i in range(n):
        result[i] = left
        left *= arr[i]
    
    right = 1
    for i in range(n-1, -1, -1):
        result[i] *= right
        right *= arr[i]
    
    return result