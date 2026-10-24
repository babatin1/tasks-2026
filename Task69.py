m = int(input())
available_dishes = set()

for i in range(m):
    available_dishes.add(input())

n = int(input())
cooked_dishes = set()

for i in range(n):
    dishes = input().split()
    cooked_dishes.update(dishes)

never_cooked = available_dishes - cooked_dishes

for dish in never_cooked:
    print(dish) 