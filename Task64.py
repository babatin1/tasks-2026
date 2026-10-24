m = int(input())
english = set()

for i in range(m):
    english.add(input())

n = int(input())
german = set()

for i in range(n):
    german.add(input())

only_one = english ^ german

if len(only_one) == 0:
    print("NO")
else:
    print(len(only_one))  