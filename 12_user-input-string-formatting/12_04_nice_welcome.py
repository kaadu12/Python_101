# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.


name = input("Please enter your name. \n")

space_index = name.find(" ")

print(space_index)

if space_index == -1:
    print(f"A nice welcome, {name}!")
else:
    print(f"A nice welcome, {name[0:space_index]}!")