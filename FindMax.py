# use a recursive algorithm to find a maximum value
items = [5, 4, 6, 88, 99, 29, 4, 100]
def find_max(items):
    if len(items)==1:
        return items[0]
    operation1 = items[0]
    operation2 = find_max(items[1:])
    if operation1 > operation2:
        return operation1
    else:
        return operation2


print(find_max(items))