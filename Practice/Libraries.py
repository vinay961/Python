# Modules --> Block of code written by someone else to perform some specific works.It is resuable.

# 1. Random --> It is a built-in module in python to do something random works, like selecting a number between 1 to 10.  (i. choice, ii.randint, iii.shuffle )

import random

# def main():
#     get_value()
    
# def get_value():
#     while True:
#         try:
#             res = random.choice(["Head","Tail"])
#             ans = input("A Coin is tossed guess the result (.. Head/Tail ..)? ")
#             if res == ans:
#                 print("You won the toss.")
#                 break
#             else:
#                 print("No, Please try again.")
#         except ValueError:
#             print("result must be string type.Please enter again...")

# main()
    
# number = random.randint(1,10)
# print(number)

# cards = ["Jack","Queen","King"]
# random.shuffle(cards)
# for card in cards:
#     print(card, " " , end="")


# 2. Statistics --> to calculate the average, mean like things.

# 3. sys --> it give the information about the system.

import sys

# try:
#     print("My name is",sys.argv[1])
# except IndexError:
#     print("You have to write your name on terminal.")

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments.")
# elif len(sys.argv) > 3:
#     sys.exit("Too many arguments.")

# for name in sys.argv[1:]:
#     print("My name is",name)

# import cowsay

# if len(sys.argv) == 2:
#     cowsay.trex("Hello, "+ sys.argv[1])

import requests
import json

if len(sys.argv) != 2:
    sys.exit()
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

x = response.json()
# print(json.dumps(response.json(), indent=2))
for result in x["results"]:
    print(result["trackCensoredName"])