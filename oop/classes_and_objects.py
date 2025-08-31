'''
a class is a blueprint or template for creating objects
objects are the instance of a class
self is used inside the class definiton
it refers to the current object
'''

class Car:
    def start(self):
        print("CAR IS STARTING...")

    def stop(self):
        print("CAR IS STOPPING...")

car1 = Car()
car2 = Car()

car1.start()
car1.stop()

car2.start()
car2.stop()

class Student:
    def set_details(self ,name,marks):
        self.name = name
        self.marks = marks

student1 = Student()
student1.set_details("Udit",50)
print(student1.name,student1.marks)
