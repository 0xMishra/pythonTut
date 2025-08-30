"""
multiple condition combine - output boolean (True/False)
and - all conditions must be true to return true
or - at least one condition must be true to return true
not - used on single operand, reverse the result
"""

age = 22
is_student = False
print(age>19 and is_student)
print(age>19 or is_student)
print(not is_student)

