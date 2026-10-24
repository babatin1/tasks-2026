set1 = set(input().split())
set2 = set(input().split())

result = set1 ^ set2

if not result:
    print("EMPTY")
else:
    print(*result) d d 