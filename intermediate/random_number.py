# psudorandom number method seems random but the numbers are reproduceable
import random

a = random.random()  # prints fandom decimal from 0-1
# controls decimal places etc (upperbound not included)
b = random.uniform(1, 10)
c = random.randint(1, 10)  # random integers, including upperbound
d = random.randrange(1, 10)  # randint without the upperbound
# pick a random number from a normal dist
# with mean of 0 and standard deviation of 1
e = random.normalvariate(0, 1)

print(a)
print(b)
print(c)
print(d)
print(e)

# lists

mylist = list('ABCDEFGHIJKLMNOP')
print(mylist)

f = random.choice(mylist)  # picks a random item from a given list
g = random.sample(mylist, 2)  # picks unique elements 2 at a time
# does not pick unique elements so you will get repeats
h = random.choices(mylist, k=3)
i = random.shuffle(mylist)  # shuffles list in place

print(f)
print(g)
print(h)
print(i)

# remember these are psudorandom numbers and can be replicated
random.seed(1)  # basically remembers all random usage below so if you...
print(random.random())
print(random.randint(1, 10))
# do it again below, you will have the exact same random numbers
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)  # $ same goes for anything on different seed,
print(random.random())
print(random.randint(1, 10))
random.seed(2)  # you just need to match up the seed number
print(random.random())
print(random.randint(1, 10))


# for cryptographic-level randomness
# takes more time for these algos though
import secrets 

j = secrets.randbelow(10) # will produce a random number between 0 and 9
k = secrets.randbits(4) # 4 digits in the number produced
l = secrets.choice(mylist) # random choice that is not reproducable

print(j)
print(k)
print(l)

# when working with arrays, use numpy (make sure you pip install on projects)
import numpy as np

m = np.random.rand(3) # creates a 1-d array with 3 elements
n = np.random.rand(3, 3) # creates 3 x 3 array
o = np.random.randint(0, 10, 3) # creates a list with 3 numbers between 0 and 9
p = np.random.randint(0, 10, (3, 4)) # creates a 3 x 4 array

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

q = np.random.shuffle(arr)

np.random.seed(1) # same seed stuff as before
print(np.random.randint(3, 3))
np.random.seed(1)
print(np.random.randint(3, 3))

print(m)
print(n)
print(o)
print(p)
print(q)