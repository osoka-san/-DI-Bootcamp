# Instructions :
# The goal of the exercise is to create a class that will help you analyze a specific text. A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.



# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code
class Text:
    def __init__(self, text):
        self.text = text
# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
    def word_frequency(self, word):
        words = self.text.split()
        frequency = words.count(word)
        if frequency == 0:
            return f"The word '{word}' does not appear in the text."
        return frequency
# a method that returns the most common word in the text.
    def most_common_word(self):
        words = self.text.split()
        word_count = {word: words.count(word) for word in words} 
        most_common = max(word_count, key=word_count.get)
        return most_common
    
# a method that returns a list of all the unique words in the text.
    def unique_words(self):
        words = self.text.split()
        unique = set(words)  
        return list(unique)



# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.

# Implement a classmethod that returns a Text instance but with a text file:
@classmethod
def from_file(cls):
    try:
        with open('the_stranger.txt', 'r') as file:
            text = file.read()
        return cls(text)
    except FileNotFoundError:
        print(f"File 'the_stranger.txt' not found.")
        return None
#     >>> Text.from_file('the_stranger.txt')
text = Text("A good book would sometimes cost as much as a good house.")
print("Frequency of 'good':", text.word_frequency("good"))
print("Most common word:", text.most_common_word())
print("Unique words:", text.unique_words())
# Hint: You need to open and read the text from the text file.
text_instance = Text.from_file()

if text_instance:
    print("Most common word:", text_instance.most_common_word())
    print("Unique words:", text_instance.unique_words()[:10])
    print("Frequency of 'the':", text_instance.word_frequency('the'))

# Now, use the provided the_stranger.txt file and try using the class you created above.

