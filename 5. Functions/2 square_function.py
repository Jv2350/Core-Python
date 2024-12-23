# Square Function with One Parameter:

# function definition
def square(num):
    return num * num  # returns squared result


# taking inputs
num = float(input("Enter a number to find its square: "))
result = square(num)  # function call
print(f"The square of {num} is: {result}")
