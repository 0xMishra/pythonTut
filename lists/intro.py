"""
can contain heterogenous elements
- ordered, indexed, dynamic and mutable
"""

# ways of creating a list
# using square brackets
my_list = [1,2,3,4]
print(my_list)

# using list constructor
list2 = list((1,2,3,4))
print(list2)

# using range function
a = list(range(1,20))

# concatenate lists
l1 = [1,2,3,4,5]
l2 = [6,7,8,9]
print(l1+l2)

# repeatetion of elements in a list
print(3*[1,2,3])

# membership of an element in a list
print(3 in [1,2,3])

# aliasing and cloning lists
lst1 = [1,2,3]
"""
if you update lst2 then lst1 will be
automatically updated as they both are
pointing to the same memory address
"""
lst2 = lst1

"""
if you update lst3 then lst1 will not be
automatically updated as they both are not
pointing to the same memory address
bcz we have used copy to make a shallow copy
the list
"""
lst3 = lst1.copy()

"""
list comprehension
syntax - [ expression for item in iterable if condition ]
condition is optional here
"""
squares = [ i**2 for i in range(1,4)]
print(squares)
