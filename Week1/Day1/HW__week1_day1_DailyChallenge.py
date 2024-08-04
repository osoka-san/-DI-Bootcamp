import random
str_input = input("Enter your string: ")
if len(str_input) < 10:
    print("string not long enough")
elif len(str_input) > 10:
    print ("string too long")
elif len(str_input) == 10:
    print("perfect string")
first_char = str_input[0]
last_char = str_input[-1]
print (f"The first character is {first_char}, the last character is {last_char}")
step =""
for i in str_input:
    step += i
    print (step)
str_list = list(str_input)
random.shuffle(str_list)
jumbled = ''.join(str_list)
print(f"The jumbled string is: {jumbled}")

