#Arrays Problems:
#ques 1:
#1. Reverse an Array

"""Input:  [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]"""

#approach 1 : Create a new array and copy elements from the end of original array.
#Time: O(n)
#Space: O(n) (extra array used)

def reverse_array():
    arr=[]
    n=int(input("enter size of original aaray"))
    for i in range(n):
        b=int(input("enter elements"))
        arr.append(b)
    n=len(arr)
    result=[0]*n

    for i in range(n):
        result[i]=arr[n-1-i]
    
    return result
print(reverse_array())

#approach 2 : Two Pointers (Optimal & Most Important)
#Time: O(n)
#Space: O(1)
def reverse_array(arr):
    left = 0
    right = len(arr)-1
    
    while left < right :
        arr[left],arr[right] = arr[right],arr[left]
        left+=1
        right-=1

    return arr

#Approach 3: Using Slicing
#Time: O(n)
#Space: O(n)
def reverse_array(arr):
    return arr[::-1]