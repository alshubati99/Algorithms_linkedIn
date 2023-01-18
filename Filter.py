# use hash table to filter out duplicate items

items = ["apples","pear", "banana", "apples", "orange","kiwi", "orange"]
filter = dict()
for item in items:
    filter[item]=0
result= set(filter.keys())
print(result)