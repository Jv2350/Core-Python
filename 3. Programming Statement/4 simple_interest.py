# Calculate Simple Interest
# take inputs from the user
principal = float(input("Enter the principal amount (Rs.): "))  # ex 200Rs
rate_of_interest = float(input("Enter the rate of interest (% per year): "))  # ex 5%
time_period = float(input("Enter the time period (in years): "))  # ex 5 years

# calculate simple interest
simple_interest = (principal * rate_of_interest * time_period) / 100

# print the simple interest
print(f"The Simple Interest is: Rs. {simple_interest}")
