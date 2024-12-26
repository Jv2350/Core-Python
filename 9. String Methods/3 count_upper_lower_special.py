# Write a Python program to count Uppercase, Lowercase, special

input_string = input("Enter a string: ")
uppercase = sum(
    c.isupper() for c in input_string
)  # isupper to check the charaster is uppercase
lowercase = sum(
    c.islower() for c in input_string
)  # islower to check charaster is lowercase
numbers = sum(c.isdigit() for c in input_string)  # isdigit to check it is digit
special = sum(
    not c.isalnum() for c in input_string
)  # isalnum to check the character is symbol

print(f"UpperCase: {uppercase}")
print(f"LowerCase: {lowercase}")
print(f"NumberCase: {numbers}")
print(f"SpecialCase: {special}")
