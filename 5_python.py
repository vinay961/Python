# sets --> it is a collection which is unordered, unindexed, unchangable(but can be remove and delete.)

# name = {"Vinay","Ravi","Ram","Vinay"}
# print(name)  # output: {'Ram', 'Ravi', 'Vinay'}  it means that it doesn't store the duplicate items.

# thisset = {"apple", "banana", "cherry"}
# accessing items of set
# for x in thisset:
#     print(x)

# print("banana" in thisset)  # output: True

# while adding item in set we can use add() method and to combine two set we can use update() method.
# thisset.add("Tom")
# print(thisset)
# name = {"Vinay","Rai"}
# thisset.update(name)
# print(thisset)

# to remove items from sets we can use remove() or discard() methods.
# thisset.discard("banana") # if item to remove doesn't exist then discard doesn't through an error.
# thisset.remove("apple")   # if item is not present then remove will raise the error.
# print(thisset)
# Note-> we can use clear() to remove all items but the set doesn't delete, del can also be used to deleted whole set.

# In order to know the difference between two set we can use difference() method.
# thisset = {"apple", "banana", "cherry"}
# thisset_new = {"apple","mango","cherry"}
# z = thisset.difference(thisset_new)
# print(z)  # output: banana



# dictionaries --> it is a collection which is ordered, changable, but doesn't allow duplicate items.

dic = {
    "name":"Vinay",
    "Dept":"CSE"
}

print(type(dic))
