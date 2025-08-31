dic = {
        "fruits":["apple","banana","berry"],
        "price":100
}
dic["amount"]=10
dic["price"]=200
del dic["amount"]
print(dic)

profile ={
        "name":"adam","age":22,"salary":2000
}

"""
getting a value from a key:
get(key,default_value) - returns None if default_value is not passed
"""
age = profile.get("age")
height = profile.get("height",5.6)
print(age,height)

# get a list of all the keys in a dict
print(list(profile.keys()))

# get all values in a dict
print(list(profile.values()))

"""
get all the items in the dict
returns in this form : [(key,value)]
"""
print(list(profile.items()))

"""
popping a key from a dict:
pop(key,default_value) - returns None if default_value is not passed
"""
age = profile.pop("age")
height = profile.pop("height",5.6)
print(age,height)

# popitem() - removes the last key:value pair from the dict
popped = profile.popitem()
print(popped)

# clear the dict
profile.clear()

"""
dict comprehension
syntax - { expression for item in iterable if condition }
condition is optional here
"""
squares = {x:x**2 for x in range(1,4)}
print(squares)
