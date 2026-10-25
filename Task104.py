n = int(input())
strings = []

for i in range(n):
    strings.append(input())

# 1. Сначала сортируем по алфавиту
strings = sorted(strings)

# 2. Затем сортируем по длине (устойчивая сортировка сохранит алфавитный порядок для одинаковых длин)
strings = sorted(strings, key=len)

for text in strings:
    print(text)