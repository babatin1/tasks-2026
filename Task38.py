num = int(input())
num = abs(num)  

if num == 0:
    print(1)
else:
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    print(count)