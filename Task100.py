n = int(input())
word = [''] * n

for i in range(n):
    line = input().split()
    pos = int(line[0])
    letter = line[1]
    word[pos - 1] = letter

print("".join(word))