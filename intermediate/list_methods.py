mylist = ["banana", "cherry", "apple"]
# print(mylist)

item = mylist[0]

# print(item)

# to iterate through the list
for i in mylist:
    print(i)

# check if item is in list
if "banana" in mylist:
    print('yes')
else:
    print("no")

# check how many elements in list
print(len(mylist))

# add element to the end
mylist.append("lemon")
print(mylist)

# inserting item to particular position
mylist.insert(1, "bluberry")
print(mylist)

# removing element from the end
removeditem = mylist.pop()
print(removeditem)
print(mylist)

# removing element by name
mylist.remove("bluberry")
print(mylist)

mylist.reverse()
mylist.sort()
# or if you need to create a new one
newlist = sorted(mylist)


# trick for creating repetitive list
mylist2 = [0] * 5
print(mylist2)

# concat lists
new_list = mylist + mylist2
print(new_list)

# to run an operation on every number of a list
listy_list = [1, 2, 3, 4, 5]
b = [i*i for i in listy_list]

print(listy_list)
print(b)

# remove all elements
mylist.clear()
print(mylist)

# slicing lists
my_list = [1, 2, 3, 4, 5, 6, 7]
a = my_list[1:]
print(a)