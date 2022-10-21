# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

user_input_1 = input("Please enter a word or phrase. \n")

user_input_2 = input("Please enter a second word or phrase. \n")

user_input_3 = input("Please enter a third word or phrase. \n")


# if len(user_input_1) < len(user_input_2) < len(user_input_3):
#     print(user_input_3)
# elif len(user_input_3) < len(user_input_1) < len(user_input_2):
#     print(user_input_2)
# else:
#     print (user_input_1)

if len(user_input_1) < len(user_input_3) and len(user_input_2) < len(user_input_3):
    print(f"{len(user_input_3)}, {user_input_3}")
elif len(user_input_3) < len(user_input_2) and len(user_input_1) < len(user_input_2):
    print(f"{len(user_input_2)}, {user_input_2}")
elif len(user_input_2) == len(user_input_3) and len(user_input_3) > len(user_input_1):
    print(f"{len(user_input_2)}, {user_input_2}")
else:
    print(f"{len(user_input_1)}, {user_input_1}")