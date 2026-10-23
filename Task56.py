count = 0
total = 0
answer = -1

while True:
    num = int(input())
    
    if num == 0:
        break
        
    count += 1
    total += num
    
    if total == 10 and answer == -1:
        answer = count

print(answer) 