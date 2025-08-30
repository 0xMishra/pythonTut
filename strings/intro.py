"""
string is a sequence of characters: numbers, a-z, A-Z, !@#$%^&*, whitespace,

string can be enclosed in single or double quotes

multiline strings are enclosed in triple quotes

** strings are immutable and indexed

indexing: there are two types of indexing; positve(starts from 0) and negative(starts from -1)
"""

name = 'adam'
name_2 = "python"
multiline_str = """
this is a
multiline string
"""

print(name, name_2,multiline_str)

print()

a = 'python'
print(a[0],a[-1])

print()
# looping through the string
for i in a:
    print(i)
