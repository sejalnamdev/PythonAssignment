#Find Duplicates in an Array
def find_duplicates(arr):
    arr.sort()
    duplicates = []
    
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1] and arr[i] not in duplicates:
            duplicates.append(arr[i])
    
    return duplicates