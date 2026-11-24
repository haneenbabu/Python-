words = input("Enter a list of words separated by spaces: ").split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)
print("Length of word:", len(longest))