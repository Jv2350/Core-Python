# Program to check the validity of a password input by users

# using the re (regular expression) library
import re


def check_password_validity(password):
    if len(password) < 8:
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[@#$%^&+=]", password):
        return False
    return True


password = input("Enter a password: ")
if check_password_validity(password):  # function call
    print("Password is valid.")
else:
    print("Password is invalid. Ensure it meets the required criteria.")
