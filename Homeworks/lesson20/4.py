# Напишіть функцію, яка перевіряє, чи є файл "data.txt" порожнім.

def is_empty():
    with open('data.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
    print(lines)
    if lines:
        return False
    else:
        return True
    
    
print(is_empty())