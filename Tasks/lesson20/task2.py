# Напишіть функцію, яка приймає шлях до файла як аргумент і повертає кількість рядків у файлі.


path = 'C:\\Users\\hayan\\Desktop\\прогламы\\Python\\Homeworks\\input.txt'

def return_number_of_strings(path):
    count = 0
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            count += 1

    return count
            
            
print(return_number_of_strings(path))