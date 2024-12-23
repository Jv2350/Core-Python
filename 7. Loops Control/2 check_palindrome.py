# Program to check if the given string is a palindrome

# Simple logic: reverse the string and check if it matches the original
def is_palindrome(s):
    return s == s[::-1]


string = input("Enter a string: ")
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")
