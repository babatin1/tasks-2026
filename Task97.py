n = int(input())
strings = []

for i in range(n):
    strings.append(input())

word1 = input()
word2 = input()

for text in strings:
    if word1 in text and word2 in text:
        print(text)