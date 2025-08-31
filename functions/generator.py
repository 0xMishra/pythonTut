'''
generator is function that behave like a iterator
uses yield function
'''

def count_down(num):
    while num >0:
        yield num
        num-=1

for n in count_down(5):
    print(n)
