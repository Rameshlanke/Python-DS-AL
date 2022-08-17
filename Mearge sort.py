array = [43,67,23,98,54,76,11,223]

#time complexity O(nlogn)
def mearge(left,right):
    merged = []
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            mearge.append(left[i])
            i+=1
        else:
            mearge.append(right[j])
            j+=1
    merged += left[i:] + right[j:]
    return merged
def meargesort(array):
    if len(array) ==1: #length of the array one vache varaku cheskuntu pothadhi

        return array
    mid = len(array)//2
    left = meargesort(array[:mid])
    right = meargesort(array[mid:])
    return meargesort(left,right)

print(meargesort(array))