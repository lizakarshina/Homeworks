# Користувач вводить рядок тексту, програма перетворює всі голосні літери у рядку на символ 'X'


str = input("Введіть рядок\n")

golosni = ["а", "е", "у", "є", "и", "і", "ї", "о", "у", "ю", "я"]
list = []

for item in str:
    if item in golosni:
        list.append("X")
    else:
        list.append(item)

str = "".join(list)

print(str)
