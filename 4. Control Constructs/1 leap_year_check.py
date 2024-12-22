# Python Program to Check Leap Year

def is_leap_year(year):
    # year is a leap year if it's divisible by 4 but not by 100, unless it's divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# taking input from user
year = int(input("Enter a year: "))

# function call and if true then says leap year otherwise not a leap
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
