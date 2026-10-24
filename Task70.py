set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

result = set1 ^ set2

if not result:
    print("EMPTY")
else:
    print(*sorted(result))