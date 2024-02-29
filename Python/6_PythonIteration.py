import time

print("Someone is here")
username = "Vinay Rai"
print(username)

# >>> r = open("6_PythonIteration.py")
# >>> r.readline()
# 'import time\n'
# >>> r.readline()
# '\n'
# >>> r.readline()
# 'print("Someone is here")\n'
# >>> r.readline()
# 'username = "Vinay Rai"\n'
# >>> r.readline()
# 'print(username)\n'
# >>> r.readline()
# ''
# >>> 

# When we use __next__() at place of readline() then at last we get stopIteration at last when no other thing is present to read inside file.

# Now let's us discuss about list iteration

# >>> myList = [1,2,3]
# >>> r = iter(myList)
# >>> r
# <list_iterator object at 0x000002C30F93B0A0>
# >>> r__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'r__next__' is not defined
# >>> r.__next__() 
# 1
# >>> r.__next__()
# 2
# >>> r.__next__()
# 3
# >>> r.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

# Note --> file also have iter() but it already do this task and take ref of f.iter().
# When we take reference of file in some variable then it is iterable and in case of list it is not true.