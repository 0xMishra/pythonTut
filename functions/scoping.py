"""
local variable - defined inside the function body
global variable - defined outside the function body
"""

def msg():
    # local variable
    choice = "I love python"
    print(choice)

msg()
# print(choice) this will throw an error as choice is not a global variable

def msg():
    print(choice)

choice = "I love python"
msg()
