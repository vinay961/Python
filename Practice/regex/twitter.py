#Here we have to extract the username from provided twitter url
# like url --> https://www.twitter.com/vinay100rai  then user name is vinay100rai.


import re

url = input("URL? ")
# Using re.sub method
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url)

#Using re.search method
username = re.search(r"^(https?://)?(www\.)?twitter\.com/$",url,re.IGNORECASE)
# Here re.sub(pattern,replace string,original string)

print(username)




