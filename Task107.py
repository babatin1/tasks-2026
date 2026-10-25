n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

# Превращаем список во множество, чтобы убрать дубликаты
unique_numbers = set(numbers)

# Выводим количество уникальных элементов
print(len(unique_numbers))