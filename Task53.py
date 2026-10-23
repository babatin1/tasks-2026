line_number = 0
cat_index = -1

while True:
    text = input()
    
    if text == "СТОП":
        break
        
    line_number += 1
    
    if "кот" in text or "Кот" in text:
        cat_index = line_number
        break

print(cat_index)