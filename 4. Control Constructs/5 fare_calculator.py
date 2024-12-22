# Program to Calculate Fare Based on Distance

# function definition
def calculate_fare(distance):
    if 1 <= distance <= 50:
        return distance * 8  # 8 Rs./Km
    elif 51 <= distance <= 100:
        return distance * 10  # 10 Rs./Km
    elif distance > 100:
        return distance * 12  # 12 Rs./Km
    else:
        return "Invalid distance"


# taking input from user
distance = float(input("Enter the distance traveled in kilometers: "))

fare = calculate_fare(distance)  # function call

print(f"The fare for {distance} kilometers is: Rs. {fare}")
