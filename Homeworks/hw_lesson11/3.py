# Створіть програму, яка приймає від користувача строку
# та перетворює її у список, де кожен елемент — це слово зі строки. Виведіть цей список.


str = input("Введіть рядок:\n")

list = []
list_of_denied_chars = [',', '.', '?', '!']

for item in str:
    if item not in list_of_denied_chars:
        list.append(item)
      
list = ''.join(list).split()


print(list)