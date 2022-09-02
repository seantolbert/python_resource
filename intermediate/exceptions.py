# types of errors

# a = 5 print(a) # sytax error 
# b = 5 + "10" # type error
# import module # modulenotfound error
# b = c # name error
# f = open('somefile.txt') # filenotfound error 
a = [1, 2, 3]
# a.remove(4) # value error
# a[4] # index error
my_dict = {'name': 'Max'}
# my_dict['age] # key error
# a = 5 / 0 # zerodivision error 

x = -5
# if x < 0:
#     raise Exception('x should be positive')
# assertions, unlike exceptions cannot be used in if statements
# assert (x >= 0), 'x is not positive' # assertion error and message will show in terminal
try:
    # a = 5 / 0
    pass
except Exception as e:
    # using the exception key, you get what python would print in termional naturally
    print(e)

# you can also explicitly type the error type in the except line
try:
    a = 5/1
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is A-OK')
finally: # runs always, no matter what
    # good spot for clean up function or clearing an input etc...
    print('cleaning up')

# you can create your owen errors as well
class ValueTooHighError(Exception):
    pass

class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError(f'value ({x}) is too high')
    if x < 5:
        raise ValueTooLowError(f'value ({x}) is too low', x)

try:
    test_value(4)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message, e.value)