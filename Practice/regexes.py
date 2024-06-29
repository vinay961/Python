# Regular Expression --> They are just pattern in the code, for example if we have to take email from user than we know that email have some specific pattern that using regular expression we define that pattern and that using that pattern we validate the user input that user given email is according to defined pattern or not.

import re

# while True:
#     email = input("What's your email? ")
    
#     if re.search('@',email):
#         print("Valid")
#         break
#     else:
#         print("Invalid")
        
        
'''

                     Symbol in Regular Expression
                1-> .     any character except newline
                2-> *     0 or more repetitions
                3-> +     1 or more repetitions
                4-> ?     0 or 1 repetitions
                5-> {m}   m repetitions
                5-> {m,n} m-n repetitions
                6-> ^     matches the start of symbol
                7-> $     matches the end of string or just
                          before the newline at the end of string.
                8-> []    set of characters that have to include
                9-> [^]   compliment of the set

'''

while True:
    email = input("What's your email? ")
    
    if re.search(r"^\w+@\w+\.in$",email):
        print("Valid")
        break
    else:
        print("Invalid")