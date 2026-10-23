while True:
    password = input()
    repeat_password = input()
    
    if len(password) < 8:
        print("Слишком короткий!")
    elif "123" in password:
        print("Содержит 123!")
    elif password != repeat_password:
        print("Пароли не совпадают!")
    else:
        print("OK")
        break