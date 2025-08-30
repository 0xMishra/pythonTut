"""
if
if else
if elif else
"""

age = int(input("Enter your age: "))

if age < 0:
    print("invalid age")
elif age >= 18:
    print("You can vote")
elif age >100:
    print("greater than 100")
else:
    print("You can't vote")
