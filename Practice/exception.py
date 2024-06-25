# x = int(input("What's x? "))
# print(f"x is {x}")

# 1. Using try_catch block we can handle exception.

# try:
#     x = int(input("What's x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not a integer.")

# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not a integer.")
    
# print(f"x is {x}")  # NameError: when I enter 'cat' as input, because cat can never converted to integer which generate the ValueError. As there is no mutual connection between the print statement and above code so the print statement get executed which cause NameError because x is not defined at.

# try:
#     x  = int(input("What's x? "))
# except ValueError:
#     print("x is not a integer.")
# else:
#     print(f"x is {x}")

# def main():
#     x = get_value()
#     if x != 'None':
#         pass
#     else:
#         print(f"x is {x}")
    
# def get_value():
#     try:
#         x = int(input("What's x? "))
#         return x
#     except ValueError:
#         print("x is not integer.")

# main()

def main():
    x = get_value();
    print(f"x is {x}")
    
def get_value():
    while True:
        try:
            x = int(input("What's x? "))
            return x
        except:
            print("x is not a integer.")
        else:
            break
    
main()