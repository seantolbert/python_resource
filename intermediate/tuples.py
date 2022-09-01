# my_tuple = ("Max", 28, "Boston")
# or
my_tuple = "Max", 28, "Boston"
# since you do not need parenthesis
print(my_tuple)

# you will need a comma even for only one item in tuple
my_tuple2 = ("max",)
print(my_tuple2)

my_tuple3 = tuple(["max", 28, "boston"])
print(my_tuple3)

# grabbing individiual items from tuples
item = my_tuple[-1]
print(item)

# tuples are immutable so you cannot change what is within them

# iterate through tuples
for i in my_tuple3:
    print(i)

# check if element i within tuple
if "boston" in my_tuple3:
    print("yes")
else:
    print("no")

# amount of elements
print(len(my_tuple))

# counting amount of specific element
my_tuple4 = "yo", "yo", 2, 4, 3, "yo"
print(my_tuple4.count("yo"))

# finding the index of element (will stop at first found)
print(my_tuple4.index("yo"))