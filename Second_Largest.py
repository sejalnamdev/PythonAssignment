#Find the Second Largest Element
#approach 1: through sorting
#time=O(nlogn)
#space=O(1)
def Find_Second_largest(arr):
    arr.sort(reverse=True)

    for i in range(1,len(arr)):
        if arr[i]!=arr[0]:
            return arr[i]
        
    return -1

#approach 2: Two Traversals
#time=O(n)
#space=O(1)
    #1st loop → Find largest
def Find_Second_largest(arr):
    max_val=max(arr)
    second =-1

    #2nd loop → Find largest smaller than max
    for num in arr:
        if num!=max_val and num>second:
            second=num
    
    return second

#Approach 3: Single Traversal (Optimal)
#time= O(n)
#space=O(1)
def Find_Second_largest(arr):
    first= float('-inf')
    second= float('-inf')

    for num in arr:
        if num > first:
            second=first
            first=num
        elif num > second and num!=first:
            second=num

    return second