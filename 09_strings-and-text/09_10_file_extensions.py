# Use a Python string method to prove which of the following files
# are .pdf files, and which aren't.
# Call the method on each file string and print() Python's response.

file_1 = "operators.pdf"
file_2 = "snowfall.jpg"
file_3 = "uncle-joes-wedding.doc"
file_4 = "invitation.pdf"

suffix = "pdf"
print(file_1.endswith(suffix))
print(file_2.endswith(suffix))
print(file_3.endswith(suffix))
print(file_4.endswith(suffix))
