#Find the Kth Smallest Element
def quick_select(arr, low, high, k):
    pivot = arr[high]
    i = low
    
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[i], arr[high] = arr[high], arr[i]
    
    if i == k-1:
        return arr[i]
    elif i > k-1:
        return quick_select(arr, low, i-1, k)
    else:
        return quick_select(arr, i+1, high, k)

def kth_smallest(arr, k):
    return quick_select(arr, 0, len(arr)-1, k)