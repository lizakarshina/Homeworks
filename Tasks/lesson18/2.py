# Написати програму-помічник,
# яка приймає температуру на вулиці у градусах цельсія та радить користувачеві що одягнути на вулицю.
# За бажанням: Дати користувачеві вибір в яких одиницях передавати температуру.
# Всередині функції робити зведення до однієї зі зручніших температур, потім давати пораду користувачеві.
# Дати користувачеві можливість ввести приблизну швидкість вітру.


def kelvin_to_celsiy(num):
    return num - 273


def far_to_celsiy(num):
    return (num - 32) / 1.8


def porada(temp):

    if temp <= 0:
        print("На вулиці холодно, одягайся теплоіше\n")

    if temp in range(0, 16):
        print("На вулиці не дуже холодно, але одягай шапку")

    if temp in range(16, 20):
        print("Можна без куртки")

    if temp >= 20:
        print("На вулиці тепло, одягайся як хочеш")


variable = int(input("1. Цельсії\n2. Кельвіни\n3. Фаренгейт\n"))

temp = int(input("Скільки градусів?\n"))

if variable == 1:
    porada(temp)
if variable == 2:
    temp = kelvin_to_celsiy(temp)
    porada(temp)
if variable == 3:
    temp = far_to_celsiy(temp)
    porada(temp)
