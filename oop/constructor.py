'''
__init__ function is python is known as the constructor
it defines the attributes of an object
types of constructors:
    - without any parameters (self)
    - with parameters (self,name,age)
    - with default parameters (self,name='adam',age=20)
'''

class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

car1 = Car("Tesla","Red")
print(car1.brand,car1.color)
