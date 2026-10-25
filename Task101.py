n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

target = numbers[-1]  # Последнее число - это то, что мы ищем
found = False

# Ищем пару среди всех чисел, кроме последнего
for i in range(n - 1):
    for j in range(i + 1, n - 1):
        if numbers[i] * numbers[j] == target:
            found = True
            break
    if found:
        break

if found:
    print("ДА")
else:
    print("НЕТ")