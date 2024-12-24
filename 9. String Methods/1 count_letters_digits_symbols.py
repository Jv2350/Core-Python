# Write a Python program to Count all letters, digits, and special

input_string = input("Enter a string: ")

chars = sum(c.isalpha() for c in input_string)  # using isalpha method for letters
digits = sum(c.isdigit() for c in input_string)  # isdigit for all the digits
symbols = sum(not c.isalnum() for c in input_string)  # isalnum for the symbols

print(f"Chars = {chars} Digits = {digits} Symbol = {symbols}")
