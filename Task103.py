n = int(input())
strings = []

for i in range(n):
    strings.append(input())

sorted_strings = sorted(strings)

for text in sorted_strings:
    print(text)