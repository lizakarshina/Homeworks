# Замінить всі цифри у рядку на слова "цифра".
str = 'mega string s 1 cifroy'
str2 = ''

list_of_nums = '0123456789'

for item in str:
    if item in list_of_nums:
        str2 += '(ЦИФРА)'
    else:
        str2 += item
        
print(str2)