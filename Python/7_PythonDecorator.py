# Write a decorator that measure the time required by a function.
import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper


@timer   # this is decorator which act like tollTax from where all vechical need to pass, in sameway function example_function also need to pass from timer function.
def example_function(n):
    time.sleep(n)
    
# example_function(2)


# Create a decorator to print the function name and the value of its arguments every time the function is called.

def debug(func):
    def wrapper(*args,**kwargs):
        
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value} ")
        
        return func(*args,**kwargs)
    
    return wrapper

@debug
def greet(name,greeting="Hello"):
    print(f"{greeting}, {name}")
    
# greet("Vinay",greeting="hanji")


# Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.

def cache(func):
    
    cache_value = {}
    print(cache_value)
    def wrapper(*args,**kwargs):
        if args in cache_value:
            return cache_value[args]
        
        result = func(*args,**kwargs)
        cache_value[args] = result
        return result
    
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a+b

print(long_running_function(2,4))
print(long_running_function(2,4))
print(long_running_function(6,4))
