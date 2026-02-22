#Move Zeroes to End: Move all zeroes in an array to the end while maintaining the order of non-zero elements.
def move_zeroes(arr):
    i = 0
    
    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    return arr