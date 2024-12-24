# Write a Python program to remove duplicate characters of a given

input_string = input("Enter a string: ")

unique_chars = []

for char in input_string:
    if char not in unique_chars:
        unique_chars.append(char)  # append all the unique values

print("".join(unique_chars))
