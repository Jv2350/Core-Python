# Display Maximum and Minimum of 5 Random Numbers:

# initialized empty list for taking random inputs from usef
nums = []
random_numbers = int(input("How many random numbers who want: "))
for i in range(random_numbers):
    nums.append(
        int(input("Enter number: "))
    )  # runs 5 times and taking inputs from user

# displaying the max and min values
print(f"The random numbers are: {nums}")
print(f"The maximum number is: {max(nums)}")
print(f"The minimum number is: {min(nums)}")
