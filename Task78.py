prev_word = input()

while True:
    new_word = input()
    
    if new_word[0] != prev_word[-1]:
        print(new_word)
        break
        
    prev_word = new_word 