n = int(input())
records = []

# Считываем данные и сохраняем в виде кортежей
for i in range(n):
    line = input().split()
    surname = line[0]
    score = int(line[1])
    records.append((surname, score))

# Выводим все пары
for surname, score in records:
    print(surname, score)

# Выводим пустую строку
print()

# Выводим только тех, у кого 4 или 5
for surname, score in records:
    if score == 4 or score == 5:
        print(surname, score)