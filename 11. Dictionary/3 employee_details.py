# empty dictionary to store values
employee_details = {}

# taking inputs for each value
employee_details["name"] = input("Enter employee name: ")
employee_details["no"] = input("Enter employee number: ")
employee_details["ID"] = input("Enter employee ID: ")
employee_details["dep"] = input("Enter department: ")
employee_details["des"] = input("Enter designation: ")
employee_details["DOJ"] = input("Enter date of joining: ")
employee_details["DOB"] = input("Enter date of birth: ")
employee_details["salary"] = float(input("Enter salary: "))

# printings keys
print("\nKeys:")
for key in employee_details.keys():
    print(key)

# printing values
print("\nValues:")
for value in employee_details.values():
    print(value)

# printing items (key-value pairs)
print("\nItems (Key-Value Pairs):")
for item in employee_details.items():
    print(item)
