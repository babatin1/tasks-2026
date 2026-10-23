line_number = 0
cat_count = 0
first_cat_index = -1

while True:
    text = input()
    
    if text == "СТОП":
        break
        
    line_number += 1
    
    if "кот" in text or "Кот" in text:
        cat_count += 1
        if first_cat_index == -1:
            first_cat_index = line_number

print(cat_count)
print(first_cat_index)