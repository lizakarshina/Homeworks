# Напишіть функцію, яка перетворює рядок у "Шифр Цезаря".
# Користувач вводить рядок і зсув, а функція повертає зашифрований рядок,
# де кожна літера зсувається на позицію вправо за алфавітом.

abetka = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"


def ceeeesar(str, gap):
    new_str = ""
    for char in str.lower():

        if char in ',.!?_-<>"@#$%^&* ':
            new_str += char
            continue

        id = abetka.index(char) + gap
        
        if id >= len(abetka):
            id -= len(abetka)

        new_str += abetka[id]

    return new_str


print(ceeeesar('Напишіть функцію, яка перетворює рядок у "Шифр Цезаря".', 1))
