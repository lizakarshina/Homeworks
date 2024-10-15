# Користувач вводить два рядки тексту,
# програма перевіряє чи є вони анаграмами (тобто містять однакові символи, але в іншому порядку)
# Замінить всі цифри у рядку на слова "цифра".


while True:
    is_true = True

    str1 = input("Введіть слово: ")
    str2 = input("Введіть слово: ")

    if len(str1) != len(str2):
        print("Не є анограмою")
        break

    list1 = list(str1)
    list2 = list(str2)

    list1.sort()
    list2.sort()

    # if list1 == list2:
    #     print('Є анограмою')
    # else:
    #     print('Не є анограмою')

    i = 0
    while i < len(list1):
            
        if list1[i] != list2[i]:
            is_true = False
            print("Не є анограмою")
            break
        i += 1

    if is_true:
        print("Є анограмою")
        
    break
