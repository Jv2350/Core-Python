# Python program to split a given list into two parts where the length of the first part of the list is given:

input_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

length = int(input("Enter the length of the first part: "))
part1 = input_list[:length]
part2 = input_list[length:]

print(f"Splitted list: ({part1}, {part2})")
