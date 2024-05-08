# def findReciprocal(value):
#     try:
#         print("Value:",value)
#         r = 1/value
#         print("Reciprocal of given number is:",r)
    
#     except ValueError:
#         print("You got value error.")
#     except ZeroDivisionError:
#         print("Number entered is zero.")
#     except:
#         print("Handling all other errors.")
        
# findReciprocal(0)

# def file():
#     try:
#         f = open("youtube.txt","w")
#         f.write("I am Vinay Rai.")
    
#     except FileNotFoundError:
#         print("File not found error.")
#     except IOError:
#         print("Get Error while opening file.")
        
#     finally:
#         f.close()
        
# file()

# a = int(input("Enter a positive number:"))
# try:
#     if a<=0:
#         raise ValueError("Not a Positive number.")
    
#     print("You Entered: ",a)
    
# except ValueError as v:
#     print(v)


# Custom Exception
# class Error(Exception):
#     pass

# class ValueTooSmallError(Error):
#     pass

# class ValueTooLargeError(Error):
#     pass

# number = 10;

# while True:
#     try:
#         num = int(input("Enter a number:"))
#         if num < number:
#             raise ValueTooSmallError
#         elif num > number:
#             raise ValueTooLargeError
#         else:
#             print("You gussed it right.")
    
#     except ValueTooLargeError:
#         print("Entered value is large.")
        
#     except ValueTooSmallError:
#         print("Entered value is small.")
        
#     except Error:
#         print("Handling all other errors.")



        
