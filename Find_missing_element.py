#Find the Missing Number: Find the missing number in an array of size n containing numbers from 1 to n.
def missing_number(arr, n):
    arr.sort()
    
    for i in range(len(arr)):
        if arr[i] != i+1:
            return i+1
    
    return n