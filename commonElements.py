#Find Intersection of Two Arrays: Find the common elements between two arrays.
def intersection(arr1, arr2):
    arr1.sort()
    arr2.sort()
    
    i = j = 0
    result = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if arr1[i] not in result:
                result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    
    return result