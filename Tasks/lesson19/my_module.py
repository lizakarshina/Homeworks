# Створити власний модуль my_module.py, який містить функцію print_message(msg),
# що приймає один аргумент msg та виводить його на екран. Потім імпортувати функцію print_message() 
# в головний файл програми та викликати її.

def print_message(msg):
    return msg

if __name__ == '__main__':
    print(print_message('Повідомлення'))