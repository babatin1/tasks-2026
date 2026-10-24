n = int(input())
cities = set()

for i in range(n):
    city = input()
    cities.add(city)

new_city = input()

if new_city in cities:
    print("TRY ANOTHER")
else:
    print("OK") 