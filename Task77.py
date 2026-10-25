text = input()
codes = []

for char in text:
    codes.append(ord(char))

print(*codes, sep=", ")