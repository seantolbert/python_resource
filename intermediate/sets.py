# collection data type that does not allow duplicate elements, unordered and mutable
my_set = {1, 2, 3, 1, 2}
print(my_set)
# or
my_set2 = set([1, 2, 3, 6, 4, 3, 1, 2])
print(my_set2)
# or for strings
my_set3 = set("hello")
print(my_set3)

# add elemets
my_set.add(51)
print(my_set)

# remove elements
my_set.remove(51)
print(my_set)

# removes first element
my_set.pop()
print(my_set)

# iterate through set
for i in my_set:
    print(i)

# empty set
my_set.clear()

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# union method combines 2 sets without duplication
u = odds.union(evens)
print(u)
# intersection creates a new set of duplicated numbers between 2 sets
i = odds.intersection(primes)
print(i)