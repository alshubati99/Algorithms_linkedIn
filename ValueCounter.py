# use a hash table to count individual items

items = ["apples","pear", "banana", "apples", "orange","kiwi", "orange"]
counter = dict()
for item in items:
    if (item in counter.keys()):
        counter[item]+=1
    else:
        counter[item]=1
print(counter)