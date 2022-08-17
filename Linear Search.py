# Linear Search using Python

def linear_search(A, key):
    index=0
    while index < len(A):
        if A[index]==key:
            return index
        index = index+1
    return (print("Not Found"))

#    0 1  2  3  4  5  6  7  8  9 ------ INDEX
A = [21,3,54,98,34,67,34,67,45,1]
found = linear_search(A,22)
print('Result: ',found)