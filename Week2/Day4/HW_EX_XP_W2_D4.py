# 🌟 Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.
import random as r
# Hint : The generated sentences do not have to make sense.

# Download this word list

# Save it in your development directory.

# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?
def get_words_from_file():
    try:
        with open ('wordlist.txt', 'r') as words_file:
            words = words_file.read().split()
        return words
    except FileNotFoundError:
        print("File is not found. Please check filename.")
        return []
# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
def get_random_sentence(length):
    words = get_words_from_file()
    random_words = r.sample(words, length)
    random_sentence = " ".join(random_words)
    return random_sentence.lower()

# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), the sentence should be lower case.

# Create a function called main which will:

# Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.
def main():
    print("This program generates random sentence from a wordlist with variable length")
    try:
        length = int(input("Please provide a sentence length from 2 to 20 words: " ))
        if 2 <= length <= 20:
            random_sentence = get_random_sentence(length)
            if random_sentence:
                print("Random sentence: ", random_sentence)
            else:
                print("Random sentence generation failed.")
        else: 
            print("Failure: sentence length should be between 2 and 20 words.")
    except ValueError:
        print("Failure. Please provide a correct int number")
if __name__ == "__main__":
    main()
    

# 🌟 Exercise 2: Working with JSON
# Instructions
# import json

import json

# Access the nested “salary” key from the JSON-string above.

sampleJson = """{ 
"company":{ 
    "employee":{ 
        "name":"emma",
        "payable":{ 
            "salary":7000,
            "bonus":800
        }
    }
}
}"""
nested = json.loads(sampleJson)
salary = nested['company']['employee']['payable']['salary']
print("Salary:", salary)

# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.

nested['company']['employee']['birth_date'] = '2000-08-14'
# Save the dictionary as JSON to a file.
with open ('updated_sample.json', 'w') as json_file:
    json.dump(nested, json_file, indent=2)
