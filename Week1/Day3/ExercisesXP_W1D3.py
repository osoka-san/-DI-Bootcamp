# 🌟 Exercise 1 : Convert lists into dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result = dict(zip(keys,values))
print(result)
# 🌟 Exercise 2 : Cinemax #2
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Given the following object:
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# How much does each family member have to pay ?
# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).
price3 = 0
price3_12 = 10
price_o12 = 15
total = 0
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
for member, age in family.items():
    if age < 3:
        cost = price3
    elif 3 <= age <= 12:
        cost = price3_12
    else:
        cost = price_o12
    
    print(f"{member} should pay {cost}$")
    total += cost
print(f"The whole price for a family movie session is {total}$")

# 🌟 Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green
# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.
# 3. Change the number of stores to 2.
# 4. Print a sentence that explains who Zaras clients are.
# 5. Add a key called country_creation with a value of Spain.
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# 7. Delete the information about the date of creation.
# 8. Print the last international competitor.
# 9. Print the major clothes colors in the US.
# 10. Print the amount of key value pairs (ie. length of the dictionary).
# 11. Print the keys of the dictionary.
# 12. Create another dictionary called more_on_zara with the following details:
# creation_date: 1975 
# number_stores: 10 000
# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# 14. Print the value of the key number_stores. What just happened ?
# 2. Создание словаря с информацией о бренде
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
brand["number_stores"] = 2
print(f"Zara provides clothes to men, women, children, and  some home decor for enthusiasts.")
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
del brand["creation_date"]
print(f"The last international competitor is {brand['international_competitors'][-1]}.")
print(f"The major clothes colors in the US are {brand['major_color']['US']}.")
print(f"The dictionary has {len(brand)} key:value pairs.")
print(f"The keys of the dictionary are {list(brand.keys())}.")
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}
brand.update(more_on_zara)
print(f"The value of the 'number_stores' key is {brand['number_stores']}.")

# Value of the number_stores is updated to 10000 because update method merge two dictionaries and replace existing details with new ones


# Exercise 4 : Disney characters
# Instructions
# Use this list :

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analyse these results :

# #1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_A = {}
number = 0
for user in users:
    disney_users_A[user] = number
    number +=1
print(disney_users_A)
# #2/

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
disney_users_B ={}
number = 0
for user in users:
    disney_users_B[number] = user
    number += 1
print(disney_users_B)

# #3/ 
# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
disney_users_C = {}
number = 0
sorted_users = sorted(users)
for user in sorted_users:
    disney_users_C[user] = number
    number += 1
print(disney_users_C)



# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.


# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
disney_users_I = {}
number = 0 
for user in users:
    if "i" in user:
        disney_users_I[user] = number
        number += 1

print(disney_users_I)

# The characters, which names start with the letter “m” or “p”.
disney_users_MP = {}
number = 0 
for user in users:
    if "M" == user[0] or "P" == user[0] :
        disney_users_MP[user] = number
        number += 1

print(disney_users_MP)
