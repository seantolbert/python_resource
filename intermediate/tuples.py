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

# slicing works the same as lists
a = 1, 2, 3, 4, 5, 6, 7
b = a[3::]
print(b)

# labelling tuple elements
name,age,city = my_tuple
print(name)
print(age)
print(city)

# adding the asterisk grabs all the elemnts not obviously labelled
my_tuple5 = 1, 2, 3, 4, 5
i1, i2, *i3 = my_tuple5
print(i3)

# working with tuples over lists can be much 
# more efficient since they are immutable
import sys
my_list = [0, 1, 2, 3, 4, 5]
my_tuple6 = 0, 1, 2, 3, 4, 5
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple6), "bytes")
# you will notice that list file sizes are larger

# using the timeit function to measuer time for creating lists vs tuples
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
# list took much longer to recreate

