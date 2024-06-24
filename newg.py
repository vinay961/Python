def main():
    # Initialize an empty list
    words_list = []

    # Prompt the user to enter multiple words
    print("Enter multiple words (press Enter after each word, type 'done' when finished):")
    while True:
        word = input().strip()  # Strip to remove any leading/trailing whitespace
        if word.lower() == 'done':
            break  # Break the loop when the user enters 'done'
        words_list.append(word)  # Add the word to the list

    # Display the list of words entered by the user
    print("List of words entered:")
    print(words_list)

if __name__ == "__main__":
    main()
