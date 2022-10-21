# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

string_choice = input("Please enter a word or phrase. \n")
letter_choice = input("Please choose a letter from your word or phrase. \n")
i = 0
for char in string_choice:
    if char == letter_choice:
        print(i)
        break
    else:
        i += 1