#Find Majority Element: Find the element that appears more than n/2 times.
def majority_element(arr):
    count = 0
    candidate = None
    
    for num in arr:
        if count == 0:
            candidate = num
        
        if num == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate