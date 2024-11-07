# Створіть програму, яка приймає список та повертає словник, 
# де ключі — це елементи списку, а значення — це кількість входжень цих елементів в список.

dict = {}

input_str = input('Введіть рядок:\n')
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
    