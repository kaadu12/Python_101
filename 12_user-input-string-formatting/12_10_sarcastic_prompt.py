# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

user_input = input("Please give me your honest opinion.\n")

new_opinion = ""

for index in range(len(user_input)):
    if index % 2 == 0:
        new_opinion+=user_input[index].upper()
    else:
        new_opinion+=user_input[index].lower()

print(new_opinion)