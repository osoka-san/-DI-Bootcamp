from anagram_checker import AnagramChecker

def main():
    checker = AnagramChecker('sowpods.txt')
    while True:
        print("\nAnagram Finder Menu")
        print("1. Find all anagrams")
        print("2. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            user_word = input("Please provide a word: ").strip()
            if not user_word.isalpha():
                print("Error: Please enter a valid word containing only alphabetic characters.")
                continue
            if ' ' in user_word:
                print("Error: Please enter only a single word.")
                continue
            if checker.is_valid_word(user_word):
                anagrams = checker.get_anagrams(user_word)
                print(f"\nYOUR WORD: \"{user_word.upper()}\"")
                print("This is a valid English word.")
                if anagrams:
                    print("Anagrams for your word:", ", ".join(anagrams))
                else:
                    print("No anagrams found.")
            else:
                print(f"\nThe word \"{user_word}\" is not a valid English word.")
        elif choice == '2':
            print("Exiting program. Have a nice day!")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    main()