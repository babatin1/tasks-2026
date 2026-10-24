m = int(input())
common_students = set()

for i in range(m):
    k = int(input())
    current_sheet = set()
    
    for j in range(k):
        name = input()
        current_sheet.add(name)
        
    if i == 0:
        common_students = current_sheet
    else:
        common_students = common_students & current_sheet

for name in common_students:
    print(name) 