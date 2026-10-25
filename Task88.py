text = input()

max_streak = 1
current_streak = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        current_streak += 1
        if current_streak > max_streak:
            max_streak = current_streak
    else:
        current_streak = 1

print(max_streak)