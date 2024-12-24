# Program to count and display the vowels in a given text

string = input("Enter a text: ")
vowels = "aeiouAEIOU"

vowel_count = {
    v: string.count(v) for v in vowels if v in string
}  # count each vowel's appearance in the sentence

print(f"Total vowels: {sum(vowel_count.values())}")  # display total vowel count
print("Vowel occurrences:", vowel_count)
