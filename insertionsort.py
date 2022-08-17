def insertionsort(array):
    for i in range(1, len(array)):
        key=array[i]
        j=i-1

        while j>=0 and key < array[j]:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key
data = [5,3,8,7,1,6,10,4,3]
print("List before Sorting: ")
print(data)
insertionsort(data)
print("List after Sorting: ")
print(data)
