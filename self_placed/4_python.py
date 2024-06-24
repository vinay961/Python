# Arguments and parameters

# 1.Positional argument
def marks(a,b):
    return a+b

result = marks(12.8,18)
# print("The total marks are:",result)

# 2.Default argument
def power(base,exp=2):
    return base**exp

# print(power(2))
# print(power(2,4))

# 3.Keyword argument
def greet(name,message):
    return f"Hello, {name}! {message}"  # it return f-string means formatted string.

# print(greet(message="How are you?",name="Vinay"))

# 4.*args and **kwargs are used to allow a function to accept a variable number of arguments.

def example_function(arg1, *args):
    print(f"arg1: {arg1}")
    print(f"args: {args}") 
    print(type(args))   # tuples
    

example_function(1, 2, 3, 4)

def example_function(arg1, **kwargs):
    print(f"arg1: {arg1}")
    print(f"kwargs: {kwargs}")

example_function(1, name="Alice", age=25)

