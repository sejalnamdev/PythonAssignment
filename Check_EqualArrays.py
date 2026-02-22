#Check if Two Arrays Are Equal: if two arrays contain the same elements
def are_equal(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    
    freq = {}
    
    for num in arr1:
        freq[num] = freq.get(num, 0) + 1
    
    for num in arr2:
        if num not in freq:
            return False
        freq[num] -= 1
        if freq[num] == 0:
            del freq[num]
    
    return len(freq) == 0