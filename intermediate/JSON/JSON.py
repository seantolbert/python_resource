from json import JSONEncoder
import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": [
        "engineer",
        "programmer"
    ]
}

# decodes JSON data into python dictionary
personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

# creates a separate JSON file
# with open('personJSON', 'w') as file:
#     json.dump(person, file, indent=4)

person = json.loads(personJSON)
print(person)


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('Max', 27)

# we have to create a custom encoding function


def encode_user(o):
    # checking if the object is an instance of the class User
    if isinstance(o, User):
        # the format you want the code to be in to make it serializable
        return {
            'name': o.name,
            'age': o.age,
            # a trick to show the class name of the instance as a string
            o.__class__.__name__: True
        }
    else:
        raise TypeError('Object of type User is not JSON serializable')


# second way to implement json encoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        else:
            return JSONEncoder.default(self, o)


# insert the above function
# if using the class instead: cls=UserEncoder INSTEAD of default=encode_user
# or
# userJSON = UserEncoder().encode(user)
userJSON = json.dumps(user, default=encode_user)
print(userJSON)  # {"name": "Max", "age": 27, "User": true}

# now that we know how to encode objects, lets decode them

# custom decode method
def decode_user(dictionary):
    # in this instance we created a key 'User' so we are
    # checking if the passed in dictionary has that key as well
    if User.__name__ in dictionary:
        return User(name=dictionary['name'], age=dictionary['age'])
    return dictionary


user = json.loads(userJSON, object_hook=decode_user)
# now we have a python dictionary
print(user.name)  # {'name': 'Max', 'age': 27, 'User': True}
