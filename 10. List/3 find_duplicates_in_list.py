# Python program to find duplicate values from a list and display those:

input_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

seen = set()
duplicates = set()
for num in input_list:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
print(f"Duplicate values: {list(duplicates)}")
