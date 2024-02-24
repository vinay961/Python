# In python string is immutable and can be written in sigle quotes or double quotes or triple quotes also.

str = "Vinay Rai"
# print(str)

# Slicing in string 
print(str[:5])   # here it print string starting from index 0 to 4, note that 5 is not included.
print(str[-1])   # we get last element of string as output
# Now let try to reverse the string using slicing
print(str[::-1])  # basically slicing take three parameters [start:end:jump] --> when we write [::-1] it means that slicing start from 0th element and jump by -1.

# replace method
print(str.replace("Vinay","Jaanvi"))

# find method
print(str.find("Rai"))

# count method
print(str.count("i"))

# string format --> here we learn how to pass varible within a string.
dept = "cse"
info = "I am {} and I am a {} student."
print(info.format(str,dept))

# List to string in python
language = ["cpp","python","Javascript"]
print(" ".join(language))  #output--> cpp python Javascript
print("-".join(language))  #output--> cpp-python-Javascript

# I want to print all charcter of string seprately
for char in str:
    print(char)
    
# Now some special cases
str1 = "c:\\user\\pwd"
print(str1) #output--> c:\user\pwd

str2 = r"c:\user\pwd"
print(str2) #output is same, when we use r then compiler treat string as a raw string.
