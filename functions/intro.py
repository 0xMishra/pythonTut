"""
reusability, modular, scoping, better maintainence
conventions to follow:
    - concise function names
    - length of function body should be smaller
    - avoid global varibales
"""

"""
parameter - placeholders for the values to be passed
arguments - values actually passed when calling the function

-- types of arguments
positional, default and keyword
"""

def greet(name="adam",city="mumbai"): # default arguments
    print(f'Welcome to {city} {name}')

greet("adam","mumbai") # positional arguments
greet(name="adam",city="mumbai") # keyword arguments

# return statement
def get_full_name(first_name,last_name):
    full_name = f'{first_name} {last_name}'
    return full_name

name = get_full_name("adam","smith")
print(name)
