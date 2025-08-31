'''
burger - function
extra cheese - extra function

main function > function add
without changing the main function code
'''

def my_decorator(func):
    def wrapper():
        print("something is happening before the hello function")
        func()
        print("something is happening after the hello function")
    return wrapper

@my_decorator
def hello():
    print("hello")

hello()
