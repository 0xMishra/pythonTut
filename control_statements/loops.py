"""
repeat a block of code multiple times
for: iterates over sequences
while: as long as the condition is true
"""

count = 0

while count <=10:
    print(count)
    count+=1


print("")
l = [1,2,3,4,5]
for a in l:
    print(a)



"""
range function
range(start,stop,step)

start - 1
stop - 100 exclude
step - 2
"""

a = list(range(1,10,1))
print(a)

# nested loops
for i in range(1,3):
    for j in range(1,3):
        print(i,j)


# break and continue statements
for num in range(1,10):
    if num == 5:
        break
    if num == 2:
        continue
    print(num)

# pass statement does nothing just a dummy
for num in range(1,10):
    if num == 2:
        pass # does nothing just a placeholder
    print(num)
