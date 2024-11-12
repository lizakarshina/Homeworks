# Створити програму — Advanced Калькулятор використовуючи функції, який включає в себе операції:
# Додавання
# Віднімання
# Множення
# Ділення
# Піднесення до степені
# Взяття кореня
# Обернення числа (576 -> 675)


def dodavania(a, b):
    return a + b

def vidnimania(a, b):
    return a - b

def mnojenia(a, b):
    return a * b

def dilennia(a, b):
    return a / b

def stepinb(a, x):
    return a ** x

def korenb(a):
    return a ** 0.5

def reverse(num):
    str_num = str(num)

    return str_num[::-1]

while True:
    number = int(input("""
    1. Додавання
    2. Віднімання
    3. Множення
    4. Ділення
    5. Степінь
    6. Корінь
    7. Обернути
    8. Вийти
    """))
    
    if number in range(1, 9):
        if number in range(1, 6):
            
            print()
            num1 = int(input("Введіть число 1\n"))
            num2 = int(input("Введіть число 2\n"))
            print()
            
            if number == 1:
                print(dodavania(num1, num2))
                
            if number == 2:
                print(vidnimania(num1, num2))
                
            if number == 3:
                print(mnojenia(num1, num2))
                
            if number == 4:
                print(dilennia(num1, num2))
                
            if number == 5:
                print(stepinb(num1, num2))
        else:
            print()
            num1 = int(input("Введіть число 1\n"))
            print()
            if number == 6:
                print(korenb(num1))
                
            if number == 7:
                print(reverse(num1))
                
            if number == 8:
                break