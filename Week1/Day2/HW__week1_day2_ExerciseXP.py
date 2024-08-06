# 🌟 Exercise 1 : Favorite Numbers
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = {3,9,27}
my_fav_numbers.add(33)
my_fav_numbers.add(108)
my_fav_numbers.pop()
friend_fav_numbers = {7,19,24,42}
our_fav_numbers =(my_fav_numbers | friend_fav_numbers)
print(our_fav_numbers)  

# 🌟 Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
# --No, tuples are immutable--

# 🌟 Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket = ["Apples"] + basket
basket.count("Apples")
apples_num = 0
for fruit in basket:
    if fruit == "Apples":
        apples_num += 1
print(f"Apples number: {apples_num}")
del basket[:]
print(f"The basket is {basket}")

# 🌟 Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# Can you think of another way to generate a sequence of floats?
# Float is decimal value e.g 1.1. Integer is a whole value e.g 2
sequence = [x * 0.5 for x in range(3, 11)]
print(sequence)

# start = 1.5
# step = 0.5
# end = 5.0
# sequence = []
# current = start
# while current <= end:
#     sequence.append(current)
#     current += step
# print(sequence)


# 🌟 Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
for numbers in range(1,21):
    print(numbers)
    
for numbers in range(1,21):
    if numbers %2 == 0:
        print(numbers)
    

# 🌟 Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
name = ("Ezra")
Person_name = input("input your name: ")
while Person_name != name:
    Person_name = input("Input your name: ")
print("Wow what a coincidence")
    
    
# 🌟 Exercise 7: Favorite fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

fruits = input("Input your favourite fruit/fruits separated by single space: ")
fruits_list = fruits.split()
input_fruit = input("Input any name of fruit: ")
if input_fruit in fruits_list: 
    print("You chose one of your favorite fruits! Enjoy!")
else: 
    print("You chose a new fruit. I hope you enjoy")

# Exercise 8: Who ordered a pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

start_price = 10
topping_price = 2.5
toppings = []
while True:
    pizza_topping = input("Enter a series of pizza toppings or enter 'quit' to stop: ")
    if pizza_topping == 'quit':
        break
    else:
        toppings.append(pizza_topping)
        print(f"{pizza_topping} added to your pizza.")
total_price = start_price + len(toppings) * topping_price
print("you ordered a pizza with: ")
for topping in toppings: 
    print(f"- {toppings} ")
print(f"Total pizza price ${total_price}")


    


# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.
price3 = 0
price3_12 = 10
price_o12 = 15
total = 0 

while True:
    person_age = input("Please provide your age or type 'quit' to finish: ")
    if person_age.lower() == "quit":
        break
    person_age = int(person_age)
    
    if person_age < 3:
        cost = price3
    elif 3 <= person_age <= 12:
        cost = price3_12
    else:
        cost = price_o12
        
    total += cost 
print(f"Total price for the tickets is {total} $")
    
# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.¿




# Exercise 10 : Sandwich Orders
# Instructions
# Using the list below :

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
# We need to prepare the orders of the clients:
# Create an empty list called finished_sandwiches.
# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich