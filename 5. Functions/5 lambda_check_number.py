# Lambda Function to Check Positive, Negative, or Zero:

# lambda function to check if the number is positive, negative, or zero
check_number = lambda num: "Positive" if num > 0 else "Negative" if num < 0 else "Zero"

# some test-case from different numbers
print(check_number(10))  # positive
print(check_number(-5))  # negative
print(check_number(0))  # zero
