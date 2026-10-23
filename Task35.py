password = input()
repeat_password = input()

if len(password) < 8:
    print("Слишком короткий!")
elif password != repeat_password:
    print("Пароли не совпадают!")
else:
    print("OK")2