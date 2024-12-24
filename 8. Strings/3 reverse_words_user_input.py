# Program to reverse words in a string

string = input("Enter a string: ")
reversed_string = " ".join(
    reversed(string.split())
)  # using the reversed function to reverse the words

print(reversed_string)
