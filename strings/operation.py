str = "python"
print(len(str))

"""
slicing[start:stop:step]
start - 0
stop - 3 exclusive
step - 1 by default
"""
print()
text = "this is python"
print(text[1:5:1])
print(text[::]) # complete string
print(text[::-1]) # reverse the string

print()
# repeating a string
b = "hello"
print(10*b) # repeats the string 10 times

print()
# concatenation
print("welcome to the " +str+ " world")

print()
# checking membership
print("py" in str)
