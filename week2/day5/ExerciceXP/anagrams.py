from .anagram_checker import AnagramChecker


def get_valid_word_from_user():

    while True:
        user_input = input("\nPlease enter a word: ").strip()

        # Empty input
        if not user_input:
            print("You didn't type anything. Please try again.")
            continue

        # Check how many words: split on whitespace
        parts = user_input.split()
        if len(parts) > 1:
            print("Only a single word is allowed. You typed multiple words.")
            continue

        word = parts[0]

        # Only alphabetic characters allowed
        if not word.isalpha():
            print("Only alphabetic characters are allowed (no numbers or symbols). Try again.")
            continue

        return word.lower()


def main():
    checker = AnagramChecker()  

    while True:

        print("1) Enter a word")
        print("2) Exit")
        choice = input("Choose an option (1/2): ").strip()

        if choice == "2":
            print("\nGoodbye! ")
            break

        elif choice == "1":
            word = get_valid_word_from_user()

            # Check if it's a valid word in your dictionary
            is_valid = checker.is_valid_word(word)
            if not is_valid:
                print(f"\n '{word}' is not a valid word in the dictionary.")
                continue

            # Get anagrams
            anagrams = checker.get_anagrams(word)

            # Nicely formatted output
            print("\n----------------------------")
            print(f" Word: {word}")
            if anagrams:
                print(f" Anagrams found: {', '.join(anagrams)}")
            else:
                print(" Anagrams found: None ")
            print("----------------------------")

        else:
            print("Invalid choice. Please type 1 or 2.")


if __name__ == "__main__":
    main()
