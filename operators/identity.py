"""
to compare the memory address of two objects
is - same memory address returns True
is not - not same memory address returns true
"""

a = [1,2,3]
b=a
c = [1,2,3]

print(a is b)
print(a is c)
