items = [5, 8, 9, 42, 33, 99, 100]
def binarysearch(item, itemlist):
    listsize=len(itemlist)-1
    lowerindex = 0
    upperindex = listsize
    while lowerindex <= upperindex:
        midpoint = (lowerindex+upperindex)//2
        if itemlist[midpoint]== item:
            return midpoint
        if item> itemlist[midpoint]:
            lowerindex=midpoint +1
        else: 
            upperindex= midpoint -1
    if lowerindex > upperindex: 
        return None
print(binarysearch(23, items))
print(binarysearch(98, items))
print(binarysearch(8, items))