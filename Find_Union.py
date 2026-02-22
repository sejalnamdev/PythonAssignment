#Find Union of Two Arrays
def union(arr1, arr2):
    i = j = 0
    result = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if arr1[i] not in result:
                result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            if arr1[i] not in result:
                result.append(arr1[i])
            i += 1
        else:
            if arr2[j] not in result:
                result.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        if arr1[i] not in result:
            result.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        if arr2[j] not in result:
            result.append(arr2[j])
        j += 1
    
    return result