cat_found = False

while True:
    text = input()
    
    if text == "СТОП":
        break
        
    if "пёс" in text or "Пёс" in text:
        cat_found = False
    elif "кот" in text or "Кот" in text:
        cat_found = True

if cat_found:
    print("МЯУ")
else:
    print("НЕТ")