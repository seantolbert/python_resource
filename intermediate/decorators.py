# function decorators allow you to add functionality to a function without mutating it

def start_end_decorator(func):

    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

@start_end_decorator
def print_name():
    print('Sean')

# print_name = start_end_decorator(print_name) # use a decorator instead of this line
print_name()

# this time, the function being decorated will have arguments
import functools

def start_end(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end
def add5(x):
    return x + 5

print(add5(10  ))
print(add5.__name__)









# class decorators
