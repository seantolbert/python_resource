# dictionaries are unorded and mutable lists of key value pairs
my_dict = {
    "name": "Max",
    "Age": 28,
    "City": "New York"
}
print(my_dict)

# or using the dict method
# you do not have to use quotes for your keys this way
mydict2 = dict(name="Mary", age=22, city="Boston")
print(mydict2)

# grabbing a value by its key
value = my_dict["name"]
print(value)

# adding key and value
my_dict["email"] = "max@xyz.com"
print(my_dict)

# overwriting value
my_dict["email"] = "maxiscool@xyz.com"
print(my_dict)

# deleting entire key value pair
del my_dict['name']
print(my_dict)
# or use pop method
my_dict.pop('Age')
print(my_dict)

# removes last item in dictionary
my_dict.popitem()
print(my_dict)

if "name" in mydict2:
    print(mydict2['name'])


# since there is no names key and the method '
# failed, the except condition is met
try:
    print(mydict2['names'])
except:
    print("error")    

# grabbing all keys 
for key in mydict2.keys():
    print(key)
# or in a different format
keys = mydict2.keys()
print(keys)

# the above works for values as well
for value in mydict2.values():
    print(value)
# or in a different format
values = mydict2.values()
print(values)

# grabbing both
for key, value, in mydict2.items():
    print(key, value)
items = mydict2.items()
print(items)

# use the copy method to kee[p original unchanged
dict_cpy = mydict2.copy()
print(dict_cpy)

# use the update method to add new key value pairs and change existing ones
my_dict = {
    "name": "Max",
    "Age": 28,
    "City": "New York"
}
my_dict.update(mydict2)
print(my_dict)

# you can use numbers and tuples as keys as well
# you may not use lists as keys
my_dict3 = {3: 9, 6: 36, 9: 81}
print(my_dict3)
value = my_dict3[3]
print(value)
mytuple = (8, 7)
my_dict4 = {mytuple: 15}
print(my_dict4)

