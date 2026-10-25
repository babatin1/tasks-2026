n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

# Сортировка пузырьком
for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            # Меняем местами, если левый элемент больше правого
            a[j], a[j + 1] = a[j + 1], a[j]

for num in a:
    print(num)