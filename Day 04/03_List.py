# Lists are containers in python

list1 = ["hello","agent",47,"!"]

print(list1)

# some list operations
# append, adds "single item" to the end of the list
# incase u add a list, it will be added as a single item

list1.append("Bye")
print(list1)

# extend, adds "list" to the end of the list as individual items

list1.extend(["hi","HI","hI"])
print(list1)

# insert, inserts the said item at the said index
list1.insert(4,"no")
print(list1)

# remove, removes the first occurence of the item from the list
list1.remove("hi")
print(list1)

# pop, pops the item from a given index or if no indexs is given, removes the last item
list1.pop(6)
print(list1)