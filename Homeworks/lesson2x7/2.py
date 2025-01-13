# Створити програму, яка зчитує вміст текстового файлу, 
# видаляє всі розділові знаки (приклад: коми, крапки) та записує вміст у новий файл.

with open('2.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    
new_lines = []
for line in lines:
    new_line = ''
    for char in line:
        if char in ',.!?:;':
            continue
        else:
            new_line += char
    new_lines.append(new_line)
    
with open('edited_2.txt', 'w', encoding='utf-8') as file:
    file.writelines(new_lines)
    
    
print('Отредаговані дані додано до файлу edited_2.txt')