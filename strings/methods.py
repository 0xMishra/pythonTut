text = "THIS IS PYTHON"
print(text.lower()) # converts characteres of a string into lowercase
print(text.upper()) # converts characteres of a string into uppercase
print(text.capitalize()) # converts only the first character of a string into uppercase
print(text.title()) # convert only the first characters of every word in a string into uppercase
print(text.swapcase()) # reverses the casing of every single character

"""
search and replace
find(): returns the first occurence of the substring passed into the method
replace(): search and replace s substring
"""
print(text.find("PY"))
print(text.replace("PYTHON","JAVA"))

"""
splitting and joining
str.split(d): str is a string, d is delimeter
d.join(s): d is a delimeter, s is an iterator
"""

str = "a,b,c"
print()
print(str.split(","))
s = str.split(",")
print(",".join(s))


"""
checking methods
str.startswith(s): str is the original string, s is the substring passed into the method
str.endswith(s): str is the original string, s is the substring passed into the method
str.isalpha(): returns True is all characters are alphabetic
str.isalnum(): returns True is all characters are alphabetic or numeric
"""

print()
print("hello".startswith("s"))
print("hello".endswith("s"))
print("hello".isalpha())
