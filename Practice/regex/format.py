import re


name = input("What's name? ").strip()

matches = re.search("^(.+), *(.+)$", name)

if matches:
    name = matches.group(2)+ " " + matches.group(1)

print("hello,",name)
print(matches)