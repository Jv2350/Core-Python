# Program to count the occurrences of each word in a given sentence

string = input("Enter a sentence: ")

word_counts = {}

for word in string.split():  # using split to separate each word
    word = word.strip(".").lower()
    word_counts[word] = word_counts.get(word, 0) + 1  # counting logic
print(word_counts)
