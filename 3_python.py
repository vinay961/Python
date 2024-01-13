# list

# name = []
# print(type(name))

# name = list(("vinay","akash"))
# print(name)

# list1 = ["abc", 34, True, 40, "male"]   # zero based indexing,In case of negative indexing we start from end -1 for last element and soon.
# print(list1[2])
# list1 = ["abc", 34, True, 40, "male"]
# print(list1[-1])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])  # output: ['cherry', 'orange', 'kiwi'] and it start at index 2 (included) and end at index 5 (not included).
# print(thislist[:5])   # By leaving out the start value, the range will start at the first item
# print(thislist[5:])   # By leaving out the end value, the range will go on to the end of the list

# To determine if a specified item is present in a list use the in keyword
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# if "melon" in thislist:
#     print("Yes, mil gya mil gya.")

# Changing items in list -> while accessing the list items we can change them also.
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# thislist[2:5] = ["Vinay","Nihal","Akash"]   # all the three items get replaced by them.
# thislist[:3] = ["Apple"]  # it replace first three items of list by apple.
# thislist.insert(2,"Vinay")
# print(thislist)

# To add an item to the end of the list, use the append() method
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)   output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# thislist.remove("apple")
# tropical.pop(1) # remove specified index item.
# del thislist[1]  # it can also delete the whole list
# thislist.clear()
# The clear() method empties the list.
# The list still remains, but it has no content.

# print(thislist)

# creting newlist based on existing list.
# fruits = ["apple","banana","mango"]
# newlist = [x for x in fruits if x != "apple"]
# print(newlist)

# first capital letter sort and than smaller letter word.
# some other methods such as copy which copy whole list 


# Tuples

# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# to determine how many items a tuple has, use the len() function

# thistuple = ("apple",)  # we need to write comma, otherwise it is string.
# print(type(thistuple)) # tuple

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple)) # string

# In order to change the tuples we need to convert it into list and then make changes after that convert it again in tuples.
# name = ("vinay","yashwani","nihal","kshtij","akash","shikhar","shiv")
# print(type(name))       # tuple
# list_name = list(name)
# print(type(list_name))  # list, now we can change anything by using above methods of lists.

# for deletion we need to follow the same method then use remove() or pop() method.
# Note --> we can use del to delete the entire tuple as del tuple_name

# unpacking the tuples --> it means that assiging the values to variables back which is possible in case of tuples.

# name = ("vinay","yashwani","nihal","kshtij","akash","shikhar","shiv")
# (x,y,*z) = name  # astrick is used because nunber of items is more then number of variables. 
# print(x,y)
# print(z)


