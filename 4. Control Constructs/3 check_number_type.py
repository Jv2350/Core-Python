# Python Program to Check if a Number is Positive, Negative or 0

# function definition
def check_number(num):
    if num > 0:  # condition for positive nums
        return "Positive"
    elif num < 0:  # condition for negative nums
        return "Negative"
    else:  # if both condition fails then print zero
        return "Zero"


# taking input
num = float(input("Enter a number: "))

result = check_number(num)  # function call
print(f"The number is: {result}")
