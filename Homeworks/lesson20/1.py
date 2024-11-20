# Реалізуйте програму, яка зчитує вміст файла "input.txt" і зберігає його у файлі "output.txt" у зворотньому порядку.

with open('input.txt', 'r', encoding='utf-8') as input:
    lines = input.readlines()
    

lines.reverse()

with open('output.txt', 'w', encoding='utf-8') as output:
    output.writelines(lines)
    
