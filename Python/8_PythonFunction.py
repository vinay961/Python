# function is a block of code that can be resuable when it needed.

import math

# Basic Function Syntax
def squareNum(num):
    return num ** 2;

# res = squareNum(4)
# print(res)

# Create a function that take two parameter as argument and return their sum

def SumNum(a,b):
    return a+b;

# res = SumNum(2,4)
# print(res)

# Write a function multiply that multiplies two numbers, but can also accept and multiply strings
def multiply(num1,num2):
    return num1*num2

# print(multiply(8,5))
# print(multiply('V',4))
# print(multiply("v","J"))  Get error 

# Create a function that returns both the area and circumference of circle given its radius
def Circle(r):
    area =  math.pi*r ** 2
    circumference = 2* math.pi * r
    
    return area, circumference

a,c =  Circle(3)
# print("Area :", a)
# print("Circumference :", c)

# Lamda function--> function without name
cube = lambda x : x**3
# print(cube(3))

# Write a function that takes variable number of arguments and returns their sum
def sum_all(*args):
    for i in args:
      print(i*2)   # gives us tuple which can be modified by us
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,3,4,5))
print(sum_all(1,2,3,4,5,6,7,8,9))



