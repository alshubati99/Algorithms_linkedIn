items = [20, 4, 6, 25, 66, 99]
def quicksort(dataset, first, last):
    if first < last: 
        pivotindex = partition(dataset, first, last)
        quicksort(dataset, first, pivotindex-1)
        quicksort(dataset, pivotindex+1, last)
def partition(datavalues, first, last):
    pivotvalue = datavalues[first]
    lower= first+1
    upper = last
    done = False
    while not done:
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower+=1
        while datavalues[upper]>= pivotvalue and upper >= lower: 
            upper-=1
        if upper < lower:
            done = True
        else: 
            temp = datavalues[first]
            datavalues[first]=datavalues[upper]
            datavalues[upper]= temp


    temp = datavalues[first]
    datavalues[first]=datavalues[upper]
    datavalues[upper]= temp
    return upper
    
print(items)
quicksort(items,0, len(items)-1)
print(items)