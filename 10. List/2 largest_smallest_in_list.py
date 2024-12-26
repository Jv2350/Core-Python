# Python program to get the largest and smallest number from a list without builtin functions:

input_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

smallest = largest = input_list[0]  # we can also use the max and min function
for num in input_list:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
print(f"Smallest: {smallest}, Largest: {largest}")
