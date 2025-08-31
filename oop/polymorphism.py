"""
polymorphism - one name, many forms

example - run:
    - car runs fast
    - a person runs slower
    - a computer programs runs the code
"""

# builtin function example of polymorphism : len()
print(len("python"))
print(len([1,2,3]))
print(len({"name":"adam"}))

# method overriding
class Bird:
    def sound(self):
        print("Birds make sound")

class Crow(Bird):
    def sound(self):
        print("Crow say cow cow!")

class Parrot(Bird):
    def sound(self):
        print("Parrot say squawk")
