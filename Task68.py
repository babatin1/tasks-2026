m = int(input())
fridge = set()

for i in range(m):
    fridge.add(input().strip())

n = int(input())

for i in range(n):
    line = input().split()
    
    recipe_name = line[0]
    ingredients = set(line[1:])
    
    if ingredients <= fridge:
        print(recipe_name) 