# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

string_input = input("Please enter a few words. \n")
symbol_input = input("Please choose a symbol. \n")
output = ""

for x in string_input:
    if x == string_input[0]:
        output = output + symbol_input
    else:
        output = output + x
print(output)

# print(string_input.replace('', 'symbol_input'))

# for x in range(0, 10):
#     print(x)

