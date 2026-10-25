n = int(input())
people = []

for i in range(n):
    line = input().split()
    surname = line[0]
    height = int(line[1])
    people.append((surname, height))

people_sorted = sorted(people, key=lambda person: person[1], reverse=True)

for surname, height in people_sorted:
    print(surname, height)