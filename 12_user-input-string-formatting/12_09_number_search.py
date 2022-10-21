# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

user_input = input("Please enter a number between 0 and 1,000,000,000.\n")

i = 0

while True:
    i = i + 1
    if i == user_input:
        print(i)
        break