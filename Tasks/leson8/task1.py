# Створіть програму, яка приймає від користувача дві строки та 
# перетворює їх у список, де перший елемент — це перша літера першої 
# строки, другий елемент — друга літера першої строки, третій елемент — 
# перша літера другої строки, четвертий — друга літера другої строки і т.д. 
# Виведіть цей список.

str = 'Перший рядок про те як я сходив в банк'
str2 = 'другий рядок про те як я нагодував кота'

list = []

list.append(str[0])
list.append(str[1])
list.append(str2[0])
list.append(str2[1])
 
print(list)