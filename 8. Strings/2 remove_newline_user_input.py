# Program to remove a newline in a Python string

print("Enter multiple lines of text. Press Enter on an empty line to finish:")

lines = []
while True:
    line = input()
    if line == "":  # check for an empty line
        break
    lines.append(line)

# join all lines into a single string separated by spaces
result = " ".join(lines)

print("\nString without newlines:")
print(result)
