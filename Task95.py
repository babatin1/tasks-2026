n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

for num in numbers:
    print(num * 3, end=" ")