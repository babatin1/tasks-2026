n = int(input())
total = 0

for i in range(n):
    num = int(input())
    
    if num <= 0:
        continue
        
    total += num

print(total) 