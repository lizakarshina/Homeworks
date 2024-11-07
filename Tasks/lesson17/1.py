# Написати програму «Калькулятор», яка вміє виконувати 
# найпростіші арифметичні операції: додавання, віднімання, 
# множення, піднесення до степеня.
# Арифметичні операції реалізувати у вигляді функцій користувача.

def dodavania(a, b):
    
    print(a + b)
    
def vidnimania(a, b):
    print(a - b)
    
def dodatok(a, b):
    print(a * b)
    
def dilenia(a, b):
     print(a / b)
     
def steptenb(a, x):
    print(a ** x)
    
    

list_of_commands = ['Додавання', 'Віднімання', 'Множення', 'Ділення', 'Степінь', 'Закрити']
while True:
    print()
    i = 1
    for command in list_of_commands:
        print(f'{i}. {command}')
        i += 1
        
    print()
    command = int(input('Оберіть номер команду\n'))
    
    if command in range(len(list_of_commands) + 1):
        if command == 1:
            a = int(input('Введіть число 1\n'))
            b = int(input('Введіть число 2\n'))
    
            dodavania(a, b)
        if command == 2:
            a = int(input('Введіть число 1\n'))
            b = int(input('Введіть число 2\n'))
    
            vidnimania(a, b)
        if command == 3:
            a = int(input('Введіть число 1\n'))
            b = int(input('Введіть число 2\n'))
    
            dodatok(a, b)
        if command == 4:
            a = int(input('Введіть число 1\n'))
            b = int(input('Введіть число 2\n'))
    
            dilenia(a, b)
        if command == 5:
            a = int(input('Введіть число 1\n'))
            b = int(input('В яку степінь?\n'))
    
            steptenb(a, b)
        if command == 6:
            print('Гарного дня!')
            break