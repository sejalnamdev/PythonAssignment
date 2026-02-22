#Find the Sum of Elements
#approach 1: Brute Force (Using Loop)...Traverse the array and keep adding each element to a variable sum.
#time=O(n)
#space=O(1)
def Find_Sum(arr):
    total = 0

    for num in arr:
        total+=num

    return total

#approach 2: Recursion(Break problem into smaller parts.) 
#time=O(n)
#space=O(1)
def find_sum(arr, n):
    if n == 0:
        return 0
    return arr[n-1] + find_sum(arr, n-1)
