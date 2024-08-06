# Instructions
# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples
# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]
# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

number = int(input("Please provide a number: "))
length = int(input("Please provide a length: "))
multiplication = [number * i for i in range(1, length + 1)]
print(multiplication)


# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.

dupl_string = input("Provide a word with any duplicate consecutive letters ")
fixed_string = ""
for i in range(len(dupl_string)):
    if i == 0 or dupl_string[i] != dupl_string[i - 1]:
        fixed_string += dupl_string[i]
print(fixed_string)

# Examples
# user's word : "ppoeemm" ➞ "poem"

# user's word : "wiiiinnnnd" ➞ "wind"

# user's word : "ttiiitllleeee" ➞ "title"

# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
# Notes
# Final strings won’t include words with double letters (e.g. “passing”, “lottery”).

