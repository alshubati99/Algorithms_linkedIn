items1= dict({"key1":1, "key2":2 , "key3": 3})
print(items1)

items2 = {} #creates an empty dictionary. 
items2["key1"]= 1
items2["key2"]= 2
items2["key3"]= 3
items2["key4"]= 4
print(items2["key4"])
items2["key2"] = "two"
print(items2)
for key, value in items2.items():
    print("key : ", key, "value: ", value)