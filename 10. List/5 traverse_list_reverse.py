# Python program to traverse a given list in reverse order, and print the elements with the original index:

input_list = input("Enter list items separated by spaces: ").split()

for index, item in enumerate(reversed(input_list)):
    print(f"{item} (Original index: {len(input_list) - index - 1})")
