n = int(input())
strings = []

for i in range(n):
    strings.append(input())

query = input()

for text in strings:
    if query in text:
        print(text)