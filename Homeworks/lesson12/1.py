# Потрібно написати програму, яка приймає рядок від користувача та перевіряє чи є у рядку хоча б одна група символів,
# що повторюється не менше як 2 рази. У результаті виводить ці групи у довільному форматі.
# ЗРОБИТИ ЗА ДОПОМОГОЮ ЦИКЛУ WHILE

str = "this is the think"
list = []

i = 0
while i < len(str):
    j = i + 1

    while j < len(str):
        
        zriz1 = str[i:j]
        zriz2 = str[j:]

        if zriz1 in zriz2:
            list.append(zriz1)
        j += 1
    i += 1
list = set(list)

print(list)
