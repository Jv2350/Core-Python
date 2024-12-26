# Write a Python Count vowels in a string

input_string = input("Enter a string: ")
vowels = "aeiouAEIOU"

vowel_count = {
    v: input_string.count(v) for v in vowels if v in input_string
}  # using comprehension

print(f"Total vowels: {sum(vowel_count.values())}")
print("Vowel occurrences:", vowel_count)
