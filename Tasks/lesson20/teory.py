# r - Відкриває існуючий файл для читання
# w - Відкриває існуючий файл для запису. Якщо у файлі 
# міститься якась інформація — вона буде перезаписана. 
# Якщо файлу не існує — він буде створений автоматично.
# a - Відкриває існуючий файл для дозапису інформації — 
# вона не буде перезаписана.
# r+, w+ - Для читання та запису інформації у файл. 
# Попередня інформація буде перезаписана.
# a+ - Для дозапису та читання інформації з файлу. 
# Інформація не перезаписується.

# file = open ('test.txt', 'r')
# for line in file:
#     print(line)
    
# file.close()


# file = open('text.txt', 't', encoding='utf-8')
# print(file.read())

# file.close()

# file = open('test.txt', 'w', encoding='utf-8')

# file.write('Це команда для запису')
# file.write('11111111\n')

# file.close()


# file = open('test.txt', 'a', encoding='utf-8')
# file.write('\n Буде додано в кінець')

# file.close()

# Автоматично закриває файл

# with open('file.txt', 'w') as file:
#     file.write('Hi <3')
    
    
    # 
with open('file.txt', 'r', encoding='utf-8') as file:
    a = file.readline()
    print(a)
    
    a = file.readline() # зберігає в а рядок та переводить курсор на наступний рядок
    print(a)
    
    a = file.readlines() # зберігає в а масив рядків
    print(a)
    
    

lines_to_write = ['рядок 1', "рядок 2"]    # 
with open('file.txt', 'w', encoding='utf-8') as file:
    file.writelines(lines_to_write)

with open('file.txt', 'r', encoding='utf-8') as file:
    file.seek(5) # Переставляє курсор на деяку кількість байт
    data = file.read()
    print(data)