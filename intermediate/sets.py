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

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
# difference creates a new set with what is not duplicated between sets
diff = setA.difference(setB)
print(diff)
# symetric difference method would return all the numbers that 
# are not found in the other set and vice versa
symdiff = setA.symmetric_difference(setB)
print(symdiff)

setC = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setD = {1, 2, 3, 10, 11, 12}

setC.intersection_update(setD)
print(setC)
print(setD)
print('overlap', setC)

# update method adds both sets together without duplicates
setA.update(setB)
print(setA)

setE = {1, 2, 3, 4, 5, 6}
setF = {1, 2, 3}
setG = {7, 8}
# issubset method returns true if all elements of first set are found in second set
print(setE.issubset(setF)) # False
print(setF.issubset(setE)) # True
# issuperset method is the opposite
print(setE.issuperset(setF)) # True
print(setF.issuperset(setE)) # False
# isdisjoint method returns true if there are no duplicates in the second set from first
print(setE.isdisjoint(setG)) # True


