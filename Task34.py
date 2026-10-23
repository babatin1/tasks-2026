temp = float(input())

while temp != 0:
    if temp < 15.5:
        print("ХОЛОДНО")
    elif temp > 28:
        print("ЖАРКО")
    else:
        print("НОРМАЛЬНО")
        
    temp = float(input()) 