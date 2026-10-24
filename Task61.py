n = int(input())
unique_words = set()

for i in range(n):
    word = input()
    unique_words.add(word)

print(len(unique_words)) 