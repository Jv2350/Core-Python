# Program to check if a given number is an Armstrong number

# logic: calculate the sum of each digit raised to the power of the number of digits
def is_armstrong(num):
    num_str = str(num)
    n = len(num_str)
    return num == sum(int(digit) ** n for digit in num_str)


number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
