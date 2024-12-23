# Division Function with Two Parameters:

# function definition
def div(num1, num2):
    if num2 != 0:
        return num1 / num2  # returns division result
    else:
        return "Division by zero is not allowed"


# taking inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = div(num1, num2)  # calling function
print(f"The division of {num1} by {num2} is: {result}")
