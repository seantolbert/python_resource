# allow for advanced methods of iterating

# product allows lists to compute the cartesian product of themselves
from itertools import product
a = [1, 2]
b = [3, 4]
prod = product(a, b)
# helps to view as a list
print(list(prod)) # [(1, 3), (1, 4), (2, 3), (2, 4)]
# allows the process to repeat twive in this case before returning
prod2 = product(a,b,repeat=2)
print(list(prod2)) 

# permutatuions returns a list of all possible permutations of a list
from itertools import permutations
a = [1, 2, 3]
perm = permutations(a)
print(list(perm))

# combinations returns all possible combinations of a list with a provided length
from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
c = combinations(a, 2)
print(list(c))
c_wr = combinations_with_replacement(a, 2)
print(list(c_wr))

# accumulate makes an iterative that returns accumulated sums (defaults to addition)
from itertools import accumulate
import operator
a = [1, 2, 5, 3, 4]
acc = accumulate(a)
print(a)
print(list(acc))
# multiplication instead of addition
acc = accumulate(a, func=operator.mul)
print(list(acc))
# max moving from right to left
acc = accumulate(a, func=max)
print(a)
print(list(acc))

# makes an iterator that lumps keys and groups from an iterable
from itertools import groupby

def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
# group_object = groupby(a, key=smaller_than_3)
# refactored^
group_object = groupby(a, key=lambda x: x<3)
for key, value in group_object:
    print(key, list(value))

b = [
    {'name': 'Tom', 'age': 22},
    {'name': 'Thomas', 'age': 22},
    {'name': 'Jim', 'age': 25},
    {'name': 'Tim', 'age': 26}
]
group = groupby(b, key=lambda x: x['age'])
for key, value in group:
    print(key, list(value))

# infinite itertools essenbtially create ruinous infinite loops, beware
from itertools import count, cycle, repeat
# count will start with the given integer
for i in count(10):
    print(i)
    if i == 15:
        break

a = [1, 2, 3]
for i in cycle(a):
    print(i)