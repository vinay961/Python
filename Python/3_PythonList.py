name = ["Vinay","IAS","IPS"]
print(name[1])

# We can perform slicing operation on list.it also support negative indexing.

# Learn how below operation works basically
# name[1:2] = "DCP"
# print(name) #output--> ['Vinay', 'D', 'C', 'P', 'IPS']
# Now we can observe that our string is treated as array.
# If we want to put whole string in list then what we can do
name[1:2] = ["DCP"]
print(name)  # output--> ['Vinay', 'DCP', 'IPS']

if "IPS" in name:
    print("I can become IPS")
    
# we can use append method which add element to last of list and can use pop() method to delete last element.
name.pop()
print(name)

# we can use insert method to insert the element in list
name.insert(1,"Jaanvi")
print(name)

# Now let's discuss about copy --> reference of copy of main is given to that variable.
copy_list = name.copy()

copy_list.pop()
copy_list.append("IAS")
print(copy_list)
print(name)


# Comprehension in list
square_num = [x**2 for x in range(10)]
print(square_num)
