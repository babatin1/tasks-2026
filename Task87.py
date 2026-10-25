word1 = input()
word2 = input()

# Превращаем строки в списки, чтобы можно было заменять найденные буквы
w1 = list(word1)
w2 = list(word2)

bulls = 0
cows = 0

# 1. Ищем быков (на одинаковых позициях)
for i in range(len(w1)):
    if w1[i] == w2[i]:
        bulls += 1
        w1[i] = None  # Вычеркиваем
        w2[i] = None  # Вычеркиваем

# 2. Ищем коров (есть в другом слове, но не на том месте)
for i in range(len(w1)):
    if w1[i] is not None:
        if w1[i] in w2:
            cows += 1
            # Находим индекс этой буквы во втором слове и вычеркиваем её
            index_in_w2 = w2.index(w1[i])
            w2[index_in_w2] = None
            w1[i] = None

print("Быки:", bulls)
print("Коровы:", cows)