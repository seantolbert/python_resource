# lambda functions are like one liner arrow functions in js
# lambda arguments: expression

def add10(x): return x + 10
print(add10(5))

# as opposed to a regular pythion function
def add10_func(x):
    return x + 10

# you can have multiple arguments as well
def multiarg_function(x, y): return x*y
print(multiarg_function(5, 10))

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
# the key x[1] has the tuple list sorted based on the y digit if (x, y)
points2D_sorted = sorted(points2D, key=lambda x: x[1])
# or based on the sum of the 2 digits
points2D_sorted2 = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D)
print(points2D_sorted)
print(points2D_sorted2)

a = [1, 2, 3, 4, 5]
# map functions - map(func, sequence)
# map function will add 2 to each item in the list
b = map(lambda x: x+2, a)
print(list(b))
# or
c = [x+2 for x in a]
print(c)

# filter function has the same structure as map function
# only return the even numbers
d = filter(lambda x: x%2 == 0, a)
print(list(d))
# or 
e = [x for x in a if x%2 == 0]
print(e)

from functools import reduce
product_a = reduce(lambda x,y: x*y, a)
print(product_a)