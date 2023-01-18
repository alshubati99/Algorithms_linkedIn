#determines if list is sorted. 
items1 = [6, 8, 9]
items2 = [7, 9, 2]
def is_sorted(itemlist):
    for i in range(0, len(itemlist)-1):
        if (itemlist[i]> itemlist[i+1]):
            return False
        #return all(itemlist[i]<= itemlist[i+1] for i in range(len(itemlist)-1))
    return True
print(is_sorted(items1))
print(is_sorted(items2))