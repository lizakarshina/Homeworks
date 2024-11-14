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


def dwa():
    return 2 + 2