whitelist = set()

# Считываем белый список до пустой строки
while True:
    line = input()
    if line == "":
        break
    whitelist.add(line)

# Считываем запросы до пустой строки и проверяем
while True:
    query = input()
    if query == "":
        break
    if query in whitelist:
        print(query)