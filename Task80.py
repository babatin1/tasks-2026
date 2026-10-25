shift = int(input())
text = input()

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
encrypted = ""

for char in text:
    if char in alphabet:
        old_index = alphabet.index(char)
        new_index = (old_index + shift) % 33
        encrypted += alphabet[new_index]
    else:
        encrypted += char

print(encrypted) 