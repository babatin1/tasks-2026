n = int(input())
found = False

for i in range(n):
    text = input()
    if "кот" in text or "Кот" in text:
        found = True
        break

if found:
    print("МЯУ")
else:
    print("НЕТ") 