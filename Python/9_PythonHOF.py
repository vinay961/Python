# Higher order function is important part of python which allow function in python to operate with another functions.

#  1. function as objects
def cal(a,b):
    return a*b;

x = cal
# print(x(3,2))

#  2. Passing function as Arguments
def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

def apply(func,a,b):
    return func(a,b)  # returning function as result

# print(apply(add,2,3))


# Functional programming--> It is a programming paradigm in which we try to bind everything in pure mathematical function styles.

data = [1,2,3,4,5]

result1 = map(lambda x: x*2 , data)
print(list(result1))

result2 = filter(lambda x: x>3, data)
print(list(result2))

# result3 = reduce(lambda x,y: x+y, data)
# print(result3)
    


    