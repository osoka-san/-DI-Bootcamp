# # What is a class?
# Class is like a template that specify which properties and methods will be will be assigned to on an object(instance) 
# # What is an instance?
# Instance is a specific object with realization of a class instructions to it
# # What is encapsulation?
# Encapsulation is a concept related to the building of data and methods in one unit, typically restricted and denoted by double underscore
# # What is abstraction?
# Abstraction is a concept that helps to focus on main object features, hiding complex, unnecessary or less important stuff and provide a simple interface for the user 
# # What is inheritance?
# Inheritance is a mechanism that allows sub-class to inherit existing attributes and methods from a parent class. 
# # What is multiple inheritance?
# Multiple inheritance is when a class inherits from more than one parent class in order to combine and extend functionality 
# # What is polymorphism?
# Polymorphism is the ability of different objects to respond to the same method in different ways
# # What is method resolution order or MRO?
# MRO (Method Resolution Order) is the order in which Python looks for methods (and attributes) when they are called on an instance of a class. Particularly important in multiple inheritance cases.


# Part 2: Create a deck of cards class.
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.
import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]

    def shuffle(self):
        if len(self.cards) < 52:
            print("Deck is incomplete. Consider reshuffling the deck.")
        random.shuffle(self.cards)
        print("\nDeck shuffled.")

    def deal(self):
        if len(self.cards) == 0:
            print("No more cards left in the deck. Please reshuffle.")
            return None
        return self.cards.pop()

    def cards_left(self):
        return len(self.cards)

    def reshuffle(self):
        self.__init__()
        self.shuffle()

def main():
    deck = Deck()
    deck.shuffle()

    while True:
        user_input = input("\nPress '1' to deal a card, '2' to reshuffle the deck, or 'q' to quit: ").strip().lower()

        if user_input == '1':
            card = deck.deal()
            if card:
                print(f"You were dealt: {card}")
            else:
                print("No cards left to deal.")
        elif user_input == '2':
            deck.reshuffle()
        elif user_input == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please press '1' to deal a card, '2' to reshuffle the deck, or 'q' to quit.")

if __name__ == "__main__":
    main()