#Remove given Element from Array
def remove_element(arr, val):
    result = []
    
    for num in arr:
        if num != val:
            result.append(num)
    
    return result