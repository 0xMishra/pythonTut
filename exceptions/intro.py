"""
erros interrupted the execution of a program
types of errors:
    - runtime erros
    - compile time errors
    - logical errors
errors are called bugs and fixing these errors is called debugging
"""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f'Sum of a and b is {a*b}') # logical error

# print(2%0) # runtime error: ZeroDivisionError

'''
Exception is a special type of runtime error
happens at run time, can be handle with try/except block
'''
try:
    num = int(input("Enter a number: "))
    res = 10/num
    print(f'result: {res}')

except ZeroDivisionError:
    print("You cannot divide a number by zero")
except ValueError:
    print("You cannot divide with a string")

