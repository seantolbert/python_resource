# ordered and immutable text representation

# can use single or double quotes
from re import sub


my_string = "yoyoyo"
print(my_string)

# grabbing individual characters
char = my_string[4]
print(char)

# substring self explanitory
substring = my_string[1:5]
print(substring)

# reverse string
substring = my_string[::-1]
print(substring)

# grab every second letter starting with the first letter
substring = my_string[::2]
print(substring)

name = "Tom"
last = "boop"

# concatinating strings with a space
full_name = name + " " + last
print(full_name)

# iterating through a string
for i in name:
    print(i)

# checking if letter or substring is inside a string
if 'om' in name:
    print('yes')
else:
    print('no')

# strip method removes excress spaces
my_string2 = "   Hello  "
my_string2 = my_string2.strip()
print(my_string2)

# upper method makes whole string upper case; lower = lowercase
upper = my_string2.upper()
lower = my_string2.lower()
print(upper, lower)

# startswith method returns true if the 
# argument is the first character/ word in string
my_string3 = "yoyo hakasho this is your bro"
print(my_string3.startswith('y')) # True
print(my_string3.startswith('yo')) # True
# ends with is the opposite
print(my_string3.endswith('o')) # True
print(my_string3.endswith('bro')) # True

# find method returns first index where argument is found
print(my_string3.find('h')) # 5
print(my_string3.find('ho')) # 10

# count method provides amount of argument within string
print(my_string3.count('o')) # 5

# replace method acts as an insert list method
# if this fails it will return the string without changing anything
print(my_string3.replace('yoyo', 'whatitdo')) # whatido hakasho this is your bro

# convert string to list
my_list = my_string3.split(' ')
print(my_list)

# bringing the list back to a string
new_string = ' '.join(my_list)
print(new_string)

# creating string from scratch
my_list = ['v'] * 6
print(my_list)
my_string = ''
for i in my_list:
    my_string += i
print(my_string)
# refactored
my_string4 = ''.join(my_list)
print(my_string4)

# formatting strings %
var = "tomorrow"
# %s for strings
my_string = "the variable is %s" % var
print(my_string)
# %d for integers rounded up
var2 = 3.1356
my_string = "the variable is %d" % var2
print(my_string)
# %f for floating numbers (6 digits by default) the .2 determines how many decimal places
var3 = 3.1345
my_string = "the variable is %.2f" % var3
print(my_string)

# formatting strings .format()
# empty {} for full variable
# ':.2f' determines you only want 2 digit decimal
var4 = 7654.87564
var5 = "neato"
my_string = "the variable is {:.2f} and {}".format(var4, var5) 
print(my_string)

# formatting with f-strings (most readable and current)
var = "tomorrow"
my_string = f"the variable is {var}"
print(my_string)