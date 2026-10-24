n = int(input())
names = []

for i in range(n):
    names.append(input())

unique_names = set(names)
total_namesakes = 0

for name in unique_names:
    count = names.count(name)
    if count > 1:
        total_namesakes += count

print(total_namesakes) 