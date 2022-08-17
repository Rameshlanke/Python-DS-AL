# Binary Search in Python

def binary_function(A, key):
    l=0
    r=len(A)-1
    while l<=r:
        mid=(l+r)//2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            r = mid -1
        elif key > A[mid]:
            l = mid+1
    return print("Not FOund")
#    0  1  2  3  4  5  6  7  8  9
A = [12,22,33,44,55,66,77,88,99,100]
found = binary_function(A,663)
found = binary_function(A,66)
print("Result: ",found)



#Binary Search using Recursion

def binarysearch_rec(A,key,l,r):
    if l>r:
        return print("Not Found")
    else:
        mid = (l+r) //2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return binarysearch_rec(A, key,l,mid-1)
        elif key > A[mid]:
            return binarysearch_rec(A,key,mid+1,r)
            
#   0  1  2  3  4  5  6  7
A=[22,33,44,55,66,77,88,99]

found = binarysearch_rec(A,88,0,7)
found = binarysearch_rec(A,885,0,7)
print("Result: ",found)