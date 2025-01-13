# Створити програму, яка зчитує дані з одного текстового файлу і записує їх у інший файл, 
# змінивши при цьому регістр всіх літер на протилежний (верхні на нижні, нижні на верхні).


def revert(str):
    result = ''
    
    for char in str:
        if char in lower:
            result += char.upper()
        else:
            result += char.lower()

    return result

lower = 'abcdefhiigklmnopqrstuvwxyz'

with open('text.txt', 'r') as file:
    lines = file.readlines()
    
new_lines = []

for line in lines:
    new_lines.append(revert(line))
    
with open('reverted_text.txt', 'w') as file:
    file.writelines(new_lines)

print(revert(lines[0]))