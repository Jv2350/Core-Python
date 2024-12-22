# Python Program to Find the Largest Among Three Numbers

# function definition
def largest_of_three(num1, num2, num3):
    return max(num1, num2, num3)  # using max() function to find largest num


# taking inputs from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest = largest_of_three(num1, num2, num3)  # function call
print(f"The largest number is: {largest}")
