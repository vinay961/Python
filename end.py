def find_occurrences(string, char):
    occurrences = []
    for i in range(len(string)):
        if string[i] == char:
            occurrences.append(i)
    return occurrences

def main():
    
    str = input("Enter a string: ")
    char = input("Enter a character to find: ")

    char_occurrences = find_occurrences(str, char)

    if char_occurrences:
        print(f"The character '{char}' occurs at index/indices:", char_occurrences)
    else:
        print(f"The character '{char}' does not occur in the string.")

if __name__ == "__main__":
    main()
