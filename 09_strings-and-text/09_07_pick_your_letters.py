# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers"

word_1 = (word[1:3])
word_2 = (word[-1:-6:-2])
word_3 = (word[0:7:6] + word[3:8:2])

print(word_1, word_2, word_3)