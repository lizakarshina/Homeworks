# Користувач вводить два рядки тексту,
# програма перевіряє чи є вони анаграмами (тобто містять однакові символи, але в іншому порядку)
# Замінить всі цифри у рядку на слова "цифра".

str1 = input('Введіть рядок\n')
str2 = input('Введіть рядок\n')




copy1 = list(str1.lower())
copy2 = list(str2.lower())

copy1.sort()
copy2.sort()

if len(copy1) != len(copy2):
    print('ne anagrama')
    
if copy1 == copy2:
    print('Є анограмою')