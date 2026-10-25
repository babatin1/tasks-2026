n = int(input())
soups = ['щи', 'борщ', 'щавелевый', 'овсяный', 'по-чабански']

for i in range(n):
    print(soups[i % len(soups)])