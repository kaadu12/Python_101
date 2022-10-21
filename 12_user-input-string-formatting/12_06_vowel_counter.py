# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

user_input = input("Please enter a phrase. \n")     

count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

for char in user_input:
    if char == "a":
        count_a = count_a + 1
    if char == "e":
        count_e = count_e + 1
    if char == "i":
        count_i = count_i + 1
    if char == "o":
        count_o = count_o + 1
    if char == "u":
        count_u = count_u + 1
print(f"a:{count_a}")
print(f"e:{count_e}")
print(f"i:{count_i}")
print(f"o:{count_o}")
print(f"u:{count_u}")