# Check whether a number is even or odd using a ternary operator
# input one number
number = int(input("Enter a number: "))

# check even or odd using a ternary operator
result = "Even" if number % 2 == 0 else "Odd"

# print the result
print(f"The number {number} is {result}.")