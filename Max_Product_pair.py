#Find Maximum Product Pair: Find two elements whose product is maximum.
def max_product_pair(arr):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')
    
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
        
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    
    if max1*max2 > min1*min2:
        return (max1, max2)
    else:
        return (min1, min2)