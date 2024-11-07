# Вивести на екран три найпоширеніші символи в рядку (пробіл за символ не вважаємо).
dict = {}

input_str = 'Введіть рядок'
# Рядок в якому є повторюючіся букви
for char in input_str:
    char = char.lower()
    if char == ' ':
        continue
    
    if char not in dict.keys():
        dict[f'{char}'] = 1
    else:
        dict[f'{char}'] += 1
    
    
    
    
print(dict)