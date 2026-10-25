n = int(input())

for i in range(n):
    text = input()
    
    if text.startswith("%%"):
        print(text[2:])
    elif text.startswith("####"):
        continue
    else:
        print(text)