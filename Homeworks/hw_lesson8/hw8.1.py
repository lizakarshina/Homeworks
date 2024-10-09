# 1. Ввести рядок з клавіатури. Видалити з нього всі цифри.

str = input('Введіть рядок із якого хочете видалити числа')
str2 = ''
list_of_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for char in str:
    if char not in list_of_nums:
        str2 += char
        
print(str2)