def selectionsort(A):
    n = len(A)
    for i in range(n-1):
        position = i
        for j in range(i+1, n):
            if A[j] < A[position]:
                position = j
        temp = A[i]
        A[i] = A[position]
        A[position] = temp

A = [3,6,9,1,5,2,7]
print('Original Array: ',A)
selectionsort(A)
print('Sorted Array: ',A)



#Selection Sort telugu

data = [1,7,3,6,2,9,4]
def selectionSort(array):
    for i in range(len(array)):
        min_index=i
        for j in range(i+1, len(array)):

            if array[j] < array[min_index]:
                min_index=j
        array[i], array[min_index] = array[min_index], array[i]

print("list Before Sorting")
print(data)
selectionSort(data)
print("list After Sorting")
print(data)