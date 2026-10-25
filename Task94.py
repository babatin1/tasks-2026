n = int(input())
strings = []

for i in range(n):
    strings.append(input())

for text in strings[::-1]:
    print(text)