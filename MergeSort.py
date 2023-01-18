items = [5, 6, 22, 67, 2, 4, 99, 66]
def mergesort(dataset):
    if len(dataset)>1:
        mid = len(dataset)//2
        leftarr = dataset [:mid]
        rightarr = dataset[mid:]
        mergesort(leftarr)
        mergesort(rightarr)
        i = 0
        j = 0 
        k = 0 
        while i < len (leftarr)and j < len(rightarr):
            if leftarr[i]<rightarr[j]:
                dataset[k] = leftarr [i]
            else:
                dataset[k] = rightarr[j]
                j+=1
    while i < len(leftarr): 
        dataset[k]=leftarr[i]
        i +=1
        k +=1 
    while j < len(rightarr): 
        dataset[k]=rightarr[j]
        j +=1
        k +=1 

print(items)
mergesort(items)
print(items)