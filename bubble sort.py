data = [9,6,3,7,1,0,2,8]

def bubblesort(array):
    for i in range (len(array)): #traversing the whole array
        for j in range(0, len(array)-i-1): #comparision
            if array[j] > array[j+1]:
                #swaping 2 elements
                array[j], array[j+1] = array[j+1], array[j]


    return array #idhi vunna lekapoyina prob ledh

print("array before: ",data)
bubblesort(data)
print("after sort: ",data)