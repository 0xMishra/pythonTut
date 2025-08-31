# append - adds new elements at the end of the list
lst = [1,2,3]
lst.append(4)
print(lst)

# extend - appending the elements of one list onto another
l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
print(l1)

# insert an element on a specific index - does not remove an existing element
a = [1,2,3]
a.insert(0,"hello world") # if the index is out of bound, it will insert it at the end of the list
print(a)

# remove an element from the list- without knowing the index
a.remove(1)
print(a)

# remove an element from the list- with the specific index
a.pop(0) # returns the element popped
print(a)

# get the index of a spicfic element in the list
idx = a.index(3) # throws value error if the element is not in the list
print(idx)

# a[10]=1- this gives index error
a = [1,2,3,4,5,6,2,3,1,1,1,1,999,2,4,5,6,3,6,78]
print(a)

# count the occurence of an element in the list
counter = a.count(1)
print(counter)

# sorting a list
a.sort()

# reversing a list
a.reverse()

# finding minimum and maximum values in a list
print(max(a))
print(min(a))

# finding common element in two lists
a = [1,2,3]
b = [1,2,5,6]

a_set = set(a)
b_set = set(b)
int_set = a_set.intersection(b_set)
print(list(int_set))

# clear the entire list
a.clear()
