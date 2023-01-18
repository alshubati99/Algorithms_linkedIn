# searching for an item in an unordered list, sometimes called Linear search. 
items = [3, 5, 77, 98, 3, 90]
def find_item(item, itemlist):
    for i in range(0, len(items)): 
        if item == itemlist[i]:
            return i
        return None

print(find_item(87, items))
print(find_item(250, items))