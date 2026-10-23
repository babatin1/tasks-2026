a = int(input())
b = int(input())
operation = input()

if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    if b == 0:
        print("ОШИБКА")
    else:
        print(a / b)
else:
    print("ОШИБКА")