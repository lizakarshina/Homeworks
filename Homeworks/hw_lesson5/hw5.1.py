# Домашнє завдання:
# Створіть програму, яка вимагає список рядків та 
# повертає список, у якому кожен елемент дорівнює довжині 
# відповідного рядка у вихідному списку.
# Приклад: ['aaa', 'bb', 'cccc'] => [3, 2, 4]

list = ['aaa', 'bb', 'cccc']

# Була помилка що елементу не існує тому не можна йому присвоєти значення len(list[i])
# changed_lsit = []

# Тому використав тернарний оператор
changed_list = [int(i) for i in range(len(list))]

for i in range(len(list)):
    changed_list[i] = len(list[i])
    
print(changed_list)