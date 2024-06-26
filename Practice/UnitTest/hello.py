def main():
    to = input("What's your name? ")
    print(hello(to))

def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()