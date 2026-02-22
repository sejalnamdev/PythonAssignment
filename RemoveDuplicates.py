#Remove Duplicates from Array: Remove duplicates from the array while maintaining order
def remove_duplicates(arr):
    result = []
    
    for num in arr:
        if num not in result:
            result.append(num)
    
    return result