
#Find the Maximum & Minimum Element
#approach 1: Linear Scan
#Time= o(n)
#space = o(1)
def find_max_min(arr):
    min_val=arr[0]
    max_val=arr[0]

    for num in arr:
        if num < min_val:
            min_val= num
        if num > max_val:
            max_val=num

    return min_val,max_val