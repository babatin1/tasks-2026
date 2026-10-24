first_list = []
while True:
    text = input()
    if text == "":
        break
    first_list.append(text)

second_list = []
while True:
    text = input()
    if text == "":
        break
    second_list.append(text)

# Превращаем списки в множества для быстрого поиска
set1 = set(first_list)
set2 = set(second_list)

# Находим пересечение
common = set1 & set2

if not common:
    print("EMPTY")
else:
    # Проходим по первому списку, чтобы сохранить порядок
    for item in first_list:
        if item in common:
            print(item, end=" ")
            common.remove(item) # Удаляем, чтобы не вывести дубликат (если он был в первом списке) d d