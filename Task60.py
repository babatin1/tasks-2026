total = 0
count = 0

while True:
    num = int(input())
    
    if num == 0:
        print("OK")
        break
        
    count += 1
    total += num
    
    if total > 100:
        print("СТОП")
        print(count)
        break 