# collections are special and unique containers for data
# built in python data structures

# counters create a frequency counting dictionary
from collections import Counter
a = "aaabbbbcccc"
my_counter = Counter(a)
print(my_counter)

# just to get values
print(my_counter.values())

# list of tuples in order starting with most common
print(my_counter.most_common()) # [('b', 4), ('c', 4), ('a', 3)]
# will only show the MOST common key value pair in a tuple list
print(my_counter.most_common(1)) # [('b', 4)]

# create a list from the counter
print(list(my_counter.elements()))


# namedtuple is similar to OOP class system 
from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt.x, pt.y)

# ordered dictionary like regular dicts but remembers when items are inserted
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['c'] = 3
ordered_dict['b'] = 2
print(ordered_dict)

# default dictionaries similr to regular dict, 
# but requires a default value if the key has no value
from collections import defaultdict
# int says default will be whatever int's defaul value is, which is 0
# could be float as well
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d['d']) # 0 would be error if regular dict

# deques double ended queue, used to add or remove elements from both ends
from collections import deque
q = deque()
q.append(1)
q.append(2)
print(q)
# appendleft adds to front of queue
q.appendleft(3)
print(q)
# extend allows you to append lists at the end
q.extend([1, 2, 4, 5, 5])
print(q)
# extendleft allows appendleft for lists, will be in reverse
q.extendleft([1, 2, 4, 5, 5])
print(q)
# with 1 as an arg, rotates all items in queue to the right by 1
q.rotate(1)
print(q)
