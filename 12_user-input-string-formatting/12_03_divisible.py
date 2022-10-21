# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

user_input = input("Please enter a number between 1 and 1,000,000,000. \n")

user_input = int(user_input)

if (user_input % 3) == 0:
    print("It is divisible by 3!")
else:
    print("It is not divisible by 3.")