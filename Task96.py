n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

p = int(input())
q = int(input())

# Берем срез от p до q включительно и сразу считаем сумму
result = sum(numbers[p:q + 1])

print(result)