n = int(input())
tuples_list = []

for i in range(n):
    text = input()
    tuples_list.append((len(text), text))

for item in tuples_list:
    print(item)