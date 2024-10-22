# Написати програму генератор пароля, яка просить користувача надати довжину бажаного пароля.

import random

list = ['@', '!', '?', '.']

pass_length = int(input('Введіть довжину паролю: '))
rand_number = random.randint(0, 99)
password = ''

for i in range(pass_length):
    
    randasdas = random.randint(0, 100)
    number = random.randint(0, rand_number)
    rand_char = random.randint(0, len(list) - 1)
    
    
    if randasdas > 50:
        password += str(list[rand_char])
    else :
        password += str(number)
        
print(f'Ваш пароль: {password}')