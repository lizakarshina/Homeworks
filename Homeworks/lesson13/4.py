# Напишіть програму, яка дозволяє користувачам реєструватися 
# на сайті та зберігає їх дані у словнику. Ключ — ім'я користувача, а значення — пароль.


users_passwords = {}

name = input("Введіть своє ім'я: ")
password = input('Введіть пароль: ')

user_dict = {name: password}
users_passwords.update(user_dict)

print(f'Всі збережені дані:\n{users_passwords}')