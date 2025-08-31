"""
child class inherit all the methods and attributes
from the parent class
"""

# method overriding
class Animal:
    def speak(self):
        print("animals make sound")

class Dog(Animal):
    def bark(self):
        print("dogs bark")


dog = Dog()
dog.speak() # can access methods from parent class Animal
dog.bark()
