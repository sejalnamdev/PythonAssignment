#Find the Leader Elements: An element is a leader if it is greater than all elements to its right.
#(An element is called a Leader if it is greater than all elements to its right.)
def find_leaders(arr):
    n = len(arr)
    leaders = []
    
    max_right = arr[n-1]
    leaders.append(max_right)
    
    for i in range(n-2, -1, -1):
        if arr[i] >= max_right:
            max_right = arr[i]
            leaders.append(arr[i])
    
    return leaders[::-1]